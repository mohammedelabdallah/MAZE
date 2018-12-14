#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`maze` module : class Maze used to build a maze, solve it and write its description in a txt file.

:author: `BART Sébastien / ELABDALLAH Mohammed / KROL Mikolaï`

:date: 2018, november.

Mazes are objects 


"""

from random import *
from class_Cell import *
from stack import *
    
class Maze():
    """
    Creates a maze.
    
    Examples:
    >>> maze = Maze(3,4)
    >>> maze
    +-+-+-+
    |     |
    + + + +
    |     |
    + + + +
    |     |
    + + + +
    |     |
    +-+-+-+
    <BLANKLINE>
    >>> maze.get_height()
    4
    >>> maze.get_width()
    3
    >>> maze.get_cell(2,2).set_wall_down()
    >>> maze
    +-+-+-+
    |     |
    + + + +
    |     |
    + + + +
    |     |
    + + +-+
    |     |
    +-+-+-+
    <BLANKLINE>
    """
    
    def __init__(self, width, height):
        """
        Creates a maze of size width*height which none of the walls are set except the walls of the outline.
        
        :param height: height of the maze
        :type height: int
        :param width: width of the maze
        :type width: int
        
        :UC: width and height > 0
        
        Examples:
        >>> maze = Maze(5, 5)
        >>> maze.get_height()
        5
        >>> maze.get_width()
        5
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        """
        self.__height = height
        self.__width = width
        self.__grid = [[Cell() for i in range(self.__width)] for j in range(self.__height)]
        for cell in self.__grid[0]:
            cell.set_wall_up()
        for cell in self.__grid[-1]:
            cell.set_wall_down()
        for line in self.__grid:
            line[0].set_wall_left()
            line[-1].set_wall_right()
    
    
    def get_grid(self):
        """
        Returns the maze's grid.
        
        :return: grid
        :rtype: list
        """
        return self.__grid


    def get_height(self):
        """
        Returns the maze's height.
        
        :return: height
        :rtype: int
        
        Examples:
        >>> maze = Maze(5, 5)
        >>> maze.get_height()
        5
        """
        return self.__height

    
    def get_width(self):
        """
        Returns the maze's width.
        
        :return: height
        :rtype: int
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.get_width()
        5
        """
        return self.__width
    
    
    def all_visited(self):
        """
        Returns True if all of the cells of the maze has been visited, False if not.
        
        :return: True if all cells has been visited, False if not
        :rtype: bool
        
        Examples:
        >>> M = Maze(5, 5)
        >>> M.all_visited()
        False
        """
        for line in self.get_grid():
            for cell in line:
                if not cell.is_visited():
                    return False
        return True
    
    def reset_all_visited(self):
        """
        Sets the attribute is_visited for each cell of the maze at False.
       
        :return: None
        :rtype: NoneType
        """
        for line in self.get_grid():
            for cell in line:
                cell.reset_visited()
        
              
    def neighborhood(self,x, y):
        """
        Returns a list of coordinates of the cell's neighbors at position (x,y).
        The neighbors are ordered clockwise (up, right, down, left).
        If one of them doesn't exist, it is represented as an empty tuple.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
        :rtype: list of tuple
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.neighborhood(0,0)
        [(), (1, 0), (0, 1), ()]
        >>> maze.neighborhood(1,1)
        [(1, 0), (2, 1), (1, 2), (0, 1)]
        >>> maze.neighborhood(4,4)
        [(4, 3), (), (), (3, 4)]
        """
        assert x < self.get_width() and y < self.get_height()
        
        l = [(x,y-1), (x+1,y), (x,y+1), (x-1,y)]
        l2 = []
        
        for t in l:
            
            if 0 <= t[0] < self.get_width() and 0 <= t[1] < self.get_height():
                l2 += [t]
            
            else:
                l2 += [()]
        return l2


    def get_cell(self,x,y):
        """
        Returns the cell of position (x,y)
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinate (x,y)
        :rtype: Cell
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.get_cell(1,1).get_walls()
        [False, False, False, False]
        >>> maze.get_cell(0,1).get_walls()
        [False, False, False, True]
        """
        return self.get_grid()[y][x]

       
    def build_walls_up(self,x,y):
        """
        Builds the top wall in the cell of coordinate (x,y) by setting its attribute __wall_up at True, take into account the cell's top
        neighbor by building its bottom wall.
        
        :param x: x-coordinate of the cell
        :type x: int
        :param y: y-coordinate of the cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_up(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + +-+ + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        >>> maze.get_cell(1,0).get_walls()
        [True, False, True, False]
        >>> maze.get_cell(1,1).get_walls()
        [True, False, False, False]
        """
        self.get_cell(x, y).set_wall_up()
        coor_neighbor = Maze.neighborhood(self, x, y)[0]
        try:
            neighbor = self.get_cell(coor_neighbor[0], coor_neighbor[1])
            neighbor.set_wall_down()
        except IndexError:
            pass
    
    def build_walls_right(self,x,y):
        """
        Builds the right wall in the cell of coordinate (x,y) by setting its attribute __wall_right at True, take into account the cell's right
        neighbor by building its left wall.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_right(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |   |     |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        >>> maze.get_cell(1,1).get_walls()
        [False, True, False, False]
        >>> maze.get_cell(2,1).get_walls()
        [False, False, False, True]
        """
        self.get_cell(x, y).set_wall_right()
        coor_neighbor = Maze.neighborhood(self, x, y)[1]
        try:
            neighbor = self.get_cell(coor_neighbor[0], coor_neighbor[1])
            neighbor.set_wall_left()
        except IndexError:
            pass
             
        
    def build_walls_down(self,x,y):
        """
        Builds the bottom wall in the cell of coordinate (x,y) by setting its attribute __wall_down at True, take into account the cell's bottom
        neighbor by building its top wall.
        
        :param x: x-coordinate of the cell
        :type x: int
        :param y: y-coordinate of the cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_down(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |         |
        + +-+ + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        >>> maze.get_cell(1,1).get_walls()
        [False, False, True, False]
        >>> maze.get_cell(1,2).get_walls()
        [True, False, False, False]
        """
        self.get_cell(x,y).set_wall_down()
        coor_neighbor = Maze.neighborhood(self, x, y)[2]
        try:
            neighbor = self.get_cell(coor_neighbor[0], coor_neighbor[1])
            neighbor.set_wall_up()
        except IndexError:
            pass
        
        
    def build_walls_left(self,x,y):
        """
        Builds the left wall in the cell of coordinate (x,y) by setting its attribute __wall_left at True, take into account the cell's left
        neighbor by building its right wall.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the maze has been modified
        :rtype: Nonetype
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_left(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        | |       |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        >>> maze.get_cell(1,1).get_walls()
        [False, False, False, True]
        >>> maze.get_cell(0,1).get_walls()
        [False, True, False, True]
        """
        self.get_cell(x,y).set_wall_left()
        coor_neighbor = Maze.neighborhood(self,x, y)[3]
        try:
            neighbor = self.get_cell(coor_neighbor[0],coor_neighbor[1])
            neighbor.set_wall_right()
        except IndexError:
            pass


    def delete_walls_up(self,x,y):
        """
        Destroys the top wall in the cell of coordinate (x,y) by setting the attribute __wall_up at False, take into account the cell's top
        neighbor by destroying its bottom wall.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_up(1,1)
        >>> maze.delete_walls_up(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        """
        self.get_cell(x,y).unset_wall_up()
        coor_neighbor = Maze.neighborhood(self,x, y)[0]
        try:
            neighbor = self.get_cell(coor_neighbor[0],coor_neighbor[1])
            neighbor.unset_wall_down()
        except IndexError:
            pass
    
    
    def delete_walls_right(self,x,y):
        """
        Destroys the right wall in the cell of coordinate (x,y) by setting the attribute __wall_right at False, take into account the cell's right
        neighbor by destroying its left wall.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_right(1,1)
        >>> maze.delete_walls_right(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        """
        self.get_cell(x,y).unset_wall_right()
        coor_neighbor = Maze.neighborhood(self,x, y)[1]
        try:
            neighbor = self.get_cell(coor_neighbor[0],coor_neighbor[1])
            neighbor.unset_wall_left()
        except IndexError:
            pass
        
    def delete_walls_down(self,x,y):
        """
        Destroys the bottom wall in the cell of coordinate (x,y) by setting the attribute __wall_down at False, take into account the cell's bottom
        neighbor by destroying its top wall.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_down(1,1)
        >>> maze.delete_walls_down(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        """
        self.get_cell(x,y).unset_wall_down()
        coor_neighbor=Maze.neighborhood(self,x, y)[2]
        try:
            neighbor=self.get_cell(coor_neighbor[0],coor_neighbor[1])
            neighbor.unset_wall_up()
        except IndexError:
            pass
        
    def delete_walls_left(self,x,y):
        """
        Destroys the left wall in the cell of coordinate (x,y) by setting the attribute __wall_left at False, take into account the cell's left
        neighbor by destroying its right wall.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: None
        :rtype: Nonetype
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_left(1,1)
        >>> maze.delete_walls_left(1,1)
        >>> maze
        +-+-+-+-+-+
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        + + + + + +
        |         |
        +-+-+-+-+-+
        <BLANKLINE>
        """
        self.get_cell(x,y).unset_wall_left()
        coor_neighbor=Maze.neighborhood(self,x, y)[3]
        try:
            neighbor=self.get_cell(coor_neighbor[0],coor_neighbor[1])
            neighbor.unset_wall_right()
        except IndexError:
            pass
                  
    
    
    def __repr__(self):
        """
        Returns the external representation of an object Maze.
        
        :return: an external representation of maze self
        :rtype: str

        :Example:

        >>> Maze(3,3)
        +-+-+-+
        |     |
        + + + +
        |     |
        + + + +
        |     |
        +-+-+-+
        <BLANKLINE>
        """
        repr = ''
        line_haut = '+-' * self.get_width() + '+\n'
        repr += line_haut
        for y in range(self.get_height()):
            line_intermediaire1 = '|'
            line_intermediaire2 = '+'
            for x in range(self.get_width()):
                if self.get_grid()[y][x].get_walls()[1] and self.get_grid()[y][x].is_displayed():
                    line_intermediaire1 += 'x|'
                elif self.get_grid()[y][x].get_walls()[1]:
                    line_intermediaire1 += ' |'
                elif not self.get_grid()[y][x].get_walls()[1] and self.get_grid()[y][x].is_displayed():
                    line_intermediaire1 += 'x '
                else:
                    line_intermediaire1 += '  '
                if self.get_grid()[y][x].get_walls()[2]:
                    line_intermediaire2 += '-+'
                else:
                    line_intermediaire2 += ' +'
            repr += line_intermediaire1 + '\n' + line_intermediaire2 + '\n'
        return repr
            
    
    def to_txt(self, file):
        """
        Writes in the file in parameter the description of self.
        
        :param file: the file name to be written in
        :type file: str
        :return: None
        """
        height = self.get_height()
        width = self.get_width()
        with open(file, 'w') as out_stream:
            out_stream.write(str(width) + '\n')
            out_stream.write(str(height) + '\n')
            out_stream.write(str(self))                 
                    
        
    def choose_unvisited_random_neighbor(self,x,y):
        """
        Returns the coordinates of a random and unvisited neighbor of the cell of coordinates (x,y).
        If the cell has no unvisited neighbor, it returns an empty tuple.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: a tuple of coordinates
        :rtype: tuple
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        
        Examples:
        >>> maze = Maze(3,3)
        >>> maze.get_cell(0,1).set_visited()
        >>> maze.get_cell(1,0).set_visited()
        >>> maze.choose_unvisited_random_neighbor(0,0)
        ()
        """
        neighbor = self.neighborhood(x,y)
        possibilities = []
        for elem in neighbor:
            if elem != () and not self.get_cell(elem[0],elem[1]).is_visited():
                possibilities.append(elem)
        if possibilities == []:
            return ()
        else:
            return choice(possibilities)
        
    
    def is_there_a_wall(self, tuple1, tuple2):
        """
        Returns True if there is a wall between the cell of coordinatess tuple1 and the cell of coordinate tuple2, False if not.
        
        :param tuple1: (x,y) coordinatess of a cell
        :type tuple1: tuple
        :param tuple2: (x,y) coordinate of a neighbor of the cell of coordinate tuple1
        :type tuple2: tuple
        
        :UC: elements of tuple1 and tuple2 must be integers, tuple1 != tuple2 and cells of coordinates tuple1 and tuple2 must be neighbors 
        
        Examples:
        >>> maze = Maze(5,5)
        >>> maze.build_walls_left(1,1)
        >>> maze.is_there_a_wall((0,1),(1,1))
        True
        """
        (x1, y1) = tuple1
        (x2, y2) = tuple2
        walls = self.get_cell(x1, y1).get_walls()
        if x2 < x1:
            return walls[3]
        elif x2 > x1:
            return walls[1]
        elif y2 < y1:
            return walls[0]
        elif y2 > y1:
            return walls[2]
        
        
    def choose_possible_move(self, x, y):
        """
        Returns the coordinates of a cell which is possible to move into, from the cell of coordinate (x,y). It's possible to move into a
        cell if there is not a wall between the actual cell and the next cell, and if the next cell has not been visited yet.
        If there is no possible moves, it returns an empty tuple.
        
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: a tuple of coordinates
        :rtype: tuple
        
        :UC: 0 <= x < maze.get_width() and 0 <= y < maze.get_height()
        """
        neighbors = self.neighborhood(x, y)
        possibilities = []
        for elem in neighbors:
            if elem != () and not self.get_cell(elem[0],elem[1]).is_visited():
                if not self.is_there_a_wall((x,y), elem):
                    possibilities.append(elem)
        if possibilities == []:
            return ()
        else:
            return choice(possibilities)
  
                
    def solve(self):
        """
        Returns the maze self with the solution displayed if there is one, returns "No solution..." if not.
        
        :return: the maze with the solution displayed or "No solution..."
        :rtype: Maze or str
        """
        x, y = 0, 0
        stack = Stack()
        stack.push((x,y))
        while (x,y) != (self.get_width()-1, self.get_height()-1):
            self.get_cell(x,y).set_visited()
            self.get_cell(x,y).display_on()
            next_coor = self.choose_possible_move(x,y)
            if next_coor != ():
                stack.push((x,y))
                x, y = next_coor
            else:
                self.get_cell(x,y).display_off()
                try:
                    (x,y) = stack.pop()
                except StackEmptyError:
                    return "No solution..."
        self.get_cell(x,y).display_on()
        return self

    