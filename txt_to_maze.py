#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script used to build a maze from a .txt file.
Use the function file_to_maze.

:author: `BART Sébastien / ELABDALLAH Mohammed / KROL Mikolaï`

:date: 2018, november.


"""

from class_Maze import *


def str_to_list_wall_right(s, width):
    """
    Function used in fichier_to_maze.
    Creates a list of verticals walls from a string.
    
    :param s: the string representation of a line of a maze
    :type s: str
    :param width: width of the maze
    :type width: int
    """
    res=s[2:]
    l=[res[2*x] for x in range(width)]
    return l


def str_to_list_wall_down(s, width):
    """
    Function used in fichier_to_maze.
    Creates a list of horizontals walls from a string.
    
    :param s: the string representation of a line of a maze
    :type s: str
    :param width: width of the maze
    :type width: int
    """
    res=s[1:]
    l=[res[2*x] for x in range(width)]
    return l


def file_to_maze(file):
    """
    Returns a maze build from a description in a txt file.
    
    :param file: the description of a maze is written in it
    :type file: str
    
    :UC: the file must be located in the folder ../txt and must be a valid description of a maze.
    
    Example:
    >>> file_to_maze('maze_5_5_0.txt')
    +-+-+-+-+-+
    |       | |
    + + +-+-+ +
    | |   |   |
    + +-+ + +-+
    |   | |   |
    +-+ +-+ +-+
    |     | | |
    +-+ + + + +
    |   |     |
    +-+-+-+-+-+
    <BLANKLINE>
    """
    with open('../txt/'+file, 'rt') as stream:
        width=int(stream.readline())
        height=int(stream.readline())
        maze=Maze(width, height)
        stream.readline()
        
        for y in range(height):
            ligne1=stream.readline()
            ligne1=str_to_list_wall_right(ligne1, width)
            ligne2=stream.readline()
            ligne2=str_to_list_wall_down(ligne2, width)
            
            for x in range(width):
                if ligne1[x]=='|':
                    maze.build_walls_right(x,y)
                if ligne2[x]=='-':
                    maze.build_walls_down(x,y)
        return maze