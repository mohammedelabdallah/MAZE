#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script used to build a handmade maze.
Use the function handmade_maze.

:author: `BART Sébastien / ELABDALLAH Mohammed / KROL Mikolaï`

:date: 2018, november.


"""

from class_Maze import *


def handmade_maze():
    """
    Function used to build a handmade maze.
    Returns a maze that you build step by step.
    
    :return: a maze
    :rtype: Maze
    """
    height = int(input('Hauteur du labyrinthe ? '))
    width = int(input('Largeur du labyrinthe ? '))
    
    maze = Maze(width, height)
    
    for y in range(maze.get_height()):
        for x in range(maze.get_width()):
            cell = maze.get_cell(x,y)
            walls = cell.get_walls()
            print(maze)
            print('Case n°{:d} de la ligne {:d}'.format(x,y))
            
            if len(walls)>0 and not walls[0]:
                if input('Construire un mur en haut ? (o/n) ')=='o':
                    maze.build_walls_up(x,y)
                    print(maze)
            
            if len(walls)>0 and not walls[1]:
                if input('Construire un mur à droite ? (o/n) ')=='o':
                    maze.build_walls_right(x,y)
                    print(maze)
            
            if len(walls)>0 and not walls[2]:
                if input('Construire un mur en bas ? (o/n) ')=='o':
                    maze.build_walls_down(x,y)
                    print(maze)
            
            if len(walls)>0 and not walls[3]:
                if input('Construire un mur à gauche ? (o/n) ')=='o':
                    maze.build_walls_left(x,y)
                    print(maze)
            
    print('Labyrinthe terminé !')
    return maze


            
