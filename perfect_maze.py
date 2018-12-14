#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script used to build a perfect maze.
Use the function perfect_maze.

:author: `BART Sébastien / ELABDALLAH Mohammed / KROL Mikolaï`

:date: 2018, november.


"""

from stack import *
from class_Maze import *


def full_maze(width, height):
    """
    Returns a maze which all of its walls are build.
    
    :param width: width of the maze
    :param height: height of the maze
    :type width: int
    :type height: int
    :return: the maze of size width*height wich all of its walls are build
    :rtype: Maze
    
    :UC: width and height > 1
    
    :Examples:
    >>> full_maze(5,5)
    +-+-+-+-+-+
    | | | | | |
    +-+-+-+-+-+
    | | | | | |
    +-+-+-+-+-+
    | | | | | |
    +-+-+-+-+-+
    | | | | | |
    +-+-+-+-+-+
    | | | | | |
    +-+-+-+-+-+
    <BLANKLINE>
    """
    maze = Maze(width, height)
    for ligne in maze.get_grid():
        for case in ligne:
            case.set_wall_right()
            case.set_wall_down()
            case.set_wall_up()
            case.set_wall_left()
    return maze
    
    
def remove_walls(maze, tuple1, tuple2):
    """
    Removes the wall between cell of coordinates tuple1 and cell of coordinates tuple2.
    
    :param maze: a maze
    :type maze: Maze
    :type tuple1: a tuple of coordinates
    :type tuple1: tuple
    :type tuple2: a tuple of coordinates
    :type tuple2: tuple
    
    :UC: elements of tuple1 and tuple2 must be integers, tuple1 != tuple2 and cells of coordinates tuple1 and tuple2 must be neighbors 
    
    :Examples:
    >>> maze = full_maze(3,3)
    >>> remove_walls(maze, (1,1), (0,1))
    >>> maze
    +-+-+-+
    | | | |
    +-+-+-+
    |   | |
    +-+-+-+
    | | | |
    +-+-+-+
    <BLANKLINE>
    """
    x1, x2, y1, y2 = tuple1[0], tuple2[0], tuple1[1], tuple2[1]
    if x2 < x1:
        maze.delete_walls_left(x1, y1)
    elif x2 > x1:
        maze.delete_walls_right(x1, y1)
    elif y2 < y1:
        maze.delete_walls_up(x1, y1)
    elif y2 > y1:
        maze.delete_walls_down(x1, y1)
            
            
def perfect_maze(width, height):
    """
    Returns a perfect maze of size width*height.
    
    :param width: the width of the wanted maze
    :type width: int
    :param height: the heught of the wanted maze
    :type height: int
    :return: the perfect maze
    :rtype: Maze
    
    :UC: width and height > 1
    """
    x, y = randint(0, width-1), randint(0, height-1)
    stack = Stack()
    maze = full_maze(width, height)
    while not maze.all_visited():
        maze.get_cell(x, y).set_visited()
        next_coor = maze.choose_unvisited_random_neighbor(x, y)
        if next_coor == ():
            (x, y) = stack.pop()
        else:
            stack.push((x, y))
            (next_x, next_y) = next_coor
            remove_walls(maze, (x,y), (next_x, next_y))
            (x, y) = (next_x, next_y)
    maze.reset_all_visited()
    return maze