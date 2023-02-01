#imports
import pygame as pg
import time

#-----------------------------------------------------------
# global variables, for easy modifications

# dimensions of the game board
DIMENSIONS = [20, 20]

# Whether the game board allows wrapping around the edges
WRAP = False

# the numbers of adjacent live cells which allow a live cell to survive
SURVIVE = [2, 3]

# The numbers of adjacent live cells which allow a dead cell to become alive
REPRODUCE = [3]

# The side length of each cell, in px
CELLSIZE = 20

# The time it takes for a generation step, in seconds
STEPTIME = 0.25

#-----------------------------------------------------------
# Class for the game board
class Board:
    # Constructor - initialize instance variables
    def __init__(self, dimx, dimy, wrap, cellsize):
        
        # Want to store each cell as a boolean, for whether it is alive or dead
        # Should have the correct dimensions
        self.cells = []
        
        self.dimx = dimx
        self.dimy = dimy
        self.wrap = wrap
        self.cellsize = cellsize
    
    # Returns the number of live adjacent cells around a specific coordinate
    def get_live_adjacents(self, x, y):
        
        # variable for the total number of adjacent live cells
        live_total = 0
        
        # Find the number of live adjacents
        
        return live_total
    
    # toggle a specific cell alive/dead
    def toggle_cell(self, x, y):
        pass
    
    # clear the board
    def clear(self):
        pass
    
    # step to the next generation
    def update(self):
        
        # empty array of cells, to be edited
        newcells = []
        
        # populate the new generation
        
        #sets the array to the updated version
        self.cells = newcells
        
    # Returns a pygame.Surface to be displayed
    def render(self):
        
        #create a pygame Surface with dimensions corresponding to the dimensions of the board
        surface = pg.Surface((200,200))
        
        # fill with gray
        
        # loop through each cell
       
                #if the cell is alive, draws a corresponding white square
                
                    # calculate pixel coordinate for its drawing position
                    
                    #create a Rect object to draw; cellsize-1 so a grid is recognizable
                    
                    #draw the Rect object
                    
                    
                #draw a black square if cell is dead
                
                    # calculate pixel coordinates for its drawing position
                    
                    #create a Rect object to draw; cellsize-1 so a grid is recognizable
                    
                    #draw the Rect object

        return surface

#-----------------------------------------------------------
# Main function (will be run when the entire program is run)
def main():
    
    # Lets us modify global variables in this scope
    global DIMENSIONS, WRAP, SURVIVE, REPRODUCE, CELLSIZE, STEPTIME
    # initialize the pygame module
    pg.init()
    # load and set the caption
    pg.display.set_caption("Conway's Game of Life")
    
    # create a surface on screen with dimensions corresponding to the size of the board
    screen = pg.display.set_mode((DIMENSIONS[0]*CELLSIZE, DIMENSIONS[1]*CELLSIZE))
     
    # define variables to control the main loop
    running = True
    pause = True
    
    #create the board
    board = Board(DIMENSIONS[0], DIMENSIONS[1], WRAP, CELLSIZE)
    
    # render and display the board
    screen.blit(board.render(), (0,0))
    pg.display.flip()
    
    # timer for knowing when to update the board automatically
    prevtime = 0
    
    # main loop
    while running:
        # event handling, gets all events from the event queue
        for event in pg.event.get():
            
            # Do something if the event is of type QUIT (if the red x button is clicked)
            if event.type == pg.QUIT:
                
                # exit the main loop
                running = False
            
            # If mouse is clicked, toggle the corresponding square
            if event.type == pg.MOUSEBUTTONDOWN:
                
                # get x and y position of click in pixels
                
                # find board x and y of the corresponding cell
                
                #toggle the cell
                
                # update the display
                screen.blit(board.render(), (0,0))
                pg.display.flip()
            
            #keypress events
            if event.type == pg.KEYDOWN:
                
                # if space is pressed, toggle pause
                if event.key == pg.K_SPACE:
                    pause = not pause
                    
                # when paused, right arrow key allows you to go to the next generation
                if event.key == pg.K_RIGHT and pause:
                    # step to the next generation
                    board.update()
                    
                    # re-render
                    screen.blit(board.render(), (0,0))
                    pg.display.flip()
                
                # Up arrow increases the step time, making the automatic playing slower
                if event.key == pg.K_UP:
                    STEPTIME += 0.05
                    
                # Down arrow decreases the step time, making the automatic playing faster
                if event.key == pg.K_DOWN:
                    STEPTIME -= 0.05
                    
                # If delete is pressed, the board is cleared
                if event.key == pg.K_DELETE:
                    
                    # clear the board
                    board.clear()
                    # re-render
                    screen.blit(board.render(), (0,0))
                    pg.display.flip()
                    
                # If p key is pressed, print cell array to shell (for saving patterns)
                if event.key == pg.K_p:
                    print(board.cells)
        
        # when not paused, let GOL play automatically
        if not pause: 
            
            # if current time minus the time at the last step is greater than STEPTIME, then render again
            if time.time() - prevtime >= STEPTIME:
                board.update()
                screen.blit(board.render(), (0,0))
                pg.display.flip()
                
                # log the time the board was last rendered
                prevtime = time.time()
    
    # quit the pygame instance (closes the window)
    pg.quit()
     
#-----------------------------------------------------------
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()