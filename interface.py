#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script used to display mazes in the graphic interface.

:author: `BART Sébastien / ELABDALLAH Mohammed / KROL Mikolaï`

:date: 2018, november.


"""

from tkinter import *
import sys
from perfect_maze import perfect_maze
from class_Maze import *

def usage():
    """
    Show how to use interface.py correctly.
    """
    print('---------------------------------------------------------------------')
    print("Utilisation de interface.py:")
    print("python3 interface.py <WIDTH> <HEIGHT> <TYPE>")
    print("<WIDTH> = (int) width of the wanted maze")
    print("<HEIGHT> = (int) height of the wanted maze")
    print("<TYPE> = (str) type of the wanted maze (perfect or handmade)")
    print('---------------------------------------------------------------------')

CAN_WIDTH = 800
CAN_HEIGHT = 600
BG_COLOR = 'SkyBlue3'
GRID_COLOR = 'ivory2'

def handmade_maze_interface(width, height, canvas, DX, DY):
    """
    Function used to build a handmade maze.
    Asks the dimension of your maze.
    Asks for each cell which wall you want to build.
    """
    maze = Maze(width, height)
    for y in range(maze.get_height()):
        for x in range(maze.get_width()):
            cell = maze.get_cell(x,y)
            walls = cell.get_walls()
            print('Case n°{:d} de la ligne {:d}'.format(x,y))
            if len(walls)>0 and not walls[0]:
                if input('Construire un mur en haut ? (o/n) ')=='o':
                    maze.build_walls_up(x,y)
                    canvas.create_line(x * DX, y * DY,
                                   (x + 1) * DX, y * DY,
                                   fill=GRID_COLOR, width=1)
                    canvas.update()
            if len(walls)>0 and not walls[1]:
                if input('Construire un mur à droite ? (o/n) ')=='o':
                    maze.build_walls_right(x,y)
                    canvas.create_line((x+1) * DX, (y+1) * DY,
                                       (x+1) * DX, y * DY,
                                   fill=GRID_COLOR, width=1)
                    canvas.update()
            if len(walls)>0 and not walls[2]:
                if input('Construire un mur en bas ? (o/n) ')=='o':
                    maze.build_walls_down(x,y)
                    canvas.create_line(x * DX, (y+1) * DY,
                                       (x+1) * DX, (y+1) * DY,
                                   fill=GRID_COLOR, width=1)
                    canvas.update()
            if len(walls)>0 and not walls[3]:
                if input('Construire un mur à gauche ? (o/n) ')=='o':
                    maze.build_walls_left(x,y)
                    canvas.create_line(x * DX, y * DY,
                                   x * DX, (y + 1) * DY,
                                   fill=GRID_COLOR, width=1)
                    canvas.update()
    print('Labyrinthe terminé !')
    return maze

def draw_circle(canvas, event):
    ray = 5
    x, y = event.x, event.y
    canvas.create_oval(x - ray, y - ray,
                       x + ray, y + ray,
                       fill = 'red')
    canvas.update()
    
def draw_grid(canvas, width, height, nom_fonction):
    """
    Draw the maze in the canvas and asks if the solution is wanted or not. If yes, shows it.
    :param canvas: a canvas
    :param width: the width of the wanted maze
    :param height: the height of the wanted maze
    :param nom_fonction: the name of the fonction that will be used to make the maze. (either handmade or perfect)
    :return: None
    :side effect: the canvas shows the maze and the solution if it was wanted.
    """
    DX = CAN_WIDTH // width
    DY = CAN_HEIGHT // height
    if nom_fonction == 'perfect':
        MAZE = perfect_maze(width, height)
        for y in range(height):
            for x in range(width):
                if MAZE.get_cell(x, y).get_walls()[0] == True:
                    canvas.create_line(x * DX, y * DY,
                                       (x + 1) * DX, y * DY,
                                       fill=GRID_COLOR, width=1)
                if MAZE.get_cell(x, y).get_walls()[3] == True:
                    canvas.create_line(x * DX, y * DY,
                                       x * DX, (y + 1) * DY,
                                       fill=GRID_COLOR, width=1)
    elif nom_fonction == 'handmade':
        MAZE = handmade_maze_interface(width, height, canvas, DX, DY)
    canvas.create_line(0, height * DY - 1,  width * DX - 1, height * DY - 1,
                       fill=GRID_COLOR, width=1)
    canvas.create_line(width * DX - 1, 0,  width * DX - 1, height * DY - 1,
                       fill=GRID_COLOR, width=1)    
    want_solution(canvas, MAZE)
    
    
def want_solution(canvas, maze):
    """
    Used to ask if the user want the solution of his maze.
    :param canvas: the canvas used in draw_grid, it is showig maze
    :param maze: the maze represented with the canvas
    :return: None
    :side effect: modify the canvas if the user wants a solution.
    """
    ask = input('Do you want the solution of your Maze ? (o/n) ')
    if ask == 'n':
        pass
    elif ask == 'o':
        width = maze.get_width()
        height = maze.get_height()
        DX = CAN_WIDTH // width
        DY = CAN_HEIGHT // height
        solved_maze = maze.solve()
        if solved_maze == 'No solution...':
            canvas.create_text(CAN_WIDTH//2, CAN_HEIGHT//2,
                               text = "Il n'y a aucune solution pour ce labyrinthe",
                               fill = 'black',
                               font = ('Times', '24'))
        else:
            for y in range(height):
                for x in range(width):
                    if solved_maze.get_cell(x, y).is_displayed():
                        canvas.create_oval(x*DX+DX*0.8, y*DY+DY*0.8, (x+1)*DX-DX*0.8, (y+1)*DY-DY*0.8,fill='salmon')
                        canvas.update()
        
def main():
    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        nom_fonction = sys.argv[3]
        assert nom_fonction == 'perfect' or nom_fonction == 'handmade'
        win = Tk()
        win.title('Labyrinthe')
        can = Canvas(win, bg=BG_COLOR, width=CAN_WIDTH, height=CAN_HEIGHT)
        can.bind('<Button-1>',
                 lambda event: draw_circle(can,
                                           event))
        can.pack()
        draw_grid(can, width, height, nom_fonction)
        win.mainloop()
    except:
        usage()
    
    
if __name__ == '__main__':
    main()
