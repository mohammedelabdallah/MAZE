#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module : class Cell used to create a cell which compose a maze.

:author: `BART Sébastien / ELABDALLAH Mohammed / KROL Mikolaï`

:date: 2018, november.

Cells are objects 


"""

class Cell(object):
    """
    Creates a cell which compose a maze.
    
    >>> c = Cell()
    >>> c.set_wall_down()
    >>> c.set_wall_up()
    >>> c.get_walls()
    [True, False, True, False]
    >>> c.unset_wall_down()
    >>> c.get_walls()
    [True, False, False, False]
    """
    
    def __init__(self):
        """
        Creates an object cell with 4 attributes about the cell's walls:
        __wall_up: True if the top wall is set, False if not
        __wall_right: True if the right wall is set, False if not
        __wall_down: True if the left wall is set, False if not
        __wall_left: True if the bottom wall is set, False if not
        The object has 2 more attributes:
        __is_visited: True if the cell has been visited, False if not
        __display: if True the cell will display a cross in the maze's representation, if False the cell will be empty
        
        :return: a cell
        :rtype: Cell
        :UC: none
        
        Examples:
        
        >>> c = Cell()
        >>> c.get_walls()
        [False, False, False, False]
        >>> c.is_visited()
        False
        """
        self.__wall_up = False
        self.__wall_down = False
        self.__wall_left = False
        self.__wall_right = False
        self.__is_visited = False
        self.__display = False
        
#--- Modify the attribute __display --------------------------------------------------------------------------#    
        
    def display_on(self):
        """
        Sets the attribute __display at True
        """
        self.__display = True
        
    def display_off(self):
        """
        Sets the attribute __display at False
        """
        self.__display = False
 
#--- Get the value of the attribute __display -----------------------------------------------------------------#
 
    def is_displayed(self):
        """
        Returns the value of the attribute __display
        """
        return self.__display

#--- Set the walls of a cell ----------------------------------------------------------------------------------#
        
    def set_wall_up(self):
        """
        Sets the top wall of the cell by setting __wall_up at True.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_up()
        >>> c.get_walls()
        [True, False, False, False]
        """
        self.__wall_up = True
        
    def set_wall_down(self):
        """
        Sets the bottom wall of the cell by setting __wall_down at True.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_down()
        >>> c.get_walls()
        [False, False, True, False]
        """
        self.__wall_down = True
    
    def set_wall_right(self):
        """
        Sets the right wall of the cell by setting __wall_right at True.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_right()
        >>> c.get_walls()
        [False, True, False, False]
        """
        self.__wall_right = True
    
    def set_wall_left(self):
        """
        Sets the left wall of the cell by setting __wall_left at True.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_left()
        >>> c.get_walls()
        [False, False, False, True]
        """
        self.__wall_left = True

#--- Unset the walls ------------------------------------------------------------------------------------#
        
    def unset_wall_up(self):
        """
        Unsets the top wall of the cell by setting __wall_up at False.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_up()
        >>> c.get_walls()
        [True, False, False, False]
        >>> c.unset_wall_up()
        >>> c.get_walls()
        [False, False, False, False]
        """
        self.__wall_up = False
        
    def unset_wall_down(self):
        """
        Unsets the bottom wall of the cell by setting __wall_down at False.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_down()
        >>> c.get_walls()
        [False, False, True, False]
        >>> c.unset_wall_down()
        >>> c.get_walls()
        [False, False, False, False]
        """
        self.__wall_down = False
    
    def unset_wall_right(self):
        """
        Unsets the right wall of the cell by setting __wall_right at False.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_right()
        >>> c.get_walls()
        [False, True, False, False]
        >>> c.unset_wall_right()
        >>> c.get_walls()
        [False, False, False, False]
        """
        self.__wall_right = False
    
    def unset_wall_left(self):
        """
        Unsets the left wall of the cell by setting __wall_left at False.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        :Examples:
        >>> c = Cell()
        >>> c.set_wall_left()
        >>> c.get_walls()
        [False, False, False, True]
        >>> c.unset_wall_left()
        >>> c.get_walls()
        [False, False, False, False]
        """
        self.__wall_left = False
        
        
#--- Know which wall of the cells are set ---------------------------------------------------------------------------#
        
    def get_walls(self):
        """
        Returns a list of booleans representing the presence of the four walls.
        They are ordered clockwise in the list: (up, right, down, left).
        
        :return: a list of four boolean values
        :rtype: list
        :UC: None
        
        Examples:
        >>> c = Cell()
        >>> c.get_walls()
        [False, False, False, False]
        >>> c.set_wall_right()
        >>> c.get_walls()
        [False, True, False, False]
        >>> c.set_wall_left()
        >>> c.get_walls()
        [False, True, False, True]
        """
        return [self.__wall_up, self.__wall_right, self.__wall_down, self.__wall_left]


#--- Modify the attribute __is_visited ----------------------------------------------------------------------------------------#
    
    def set_visited(self):
        """
        Sets the cell as visited by setting the __is_visited attribute at True.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        Examples:
        >>> c = Cell()
        >>> c.is_visited()
        False
        >>> c.set_visited()
        >>> c.is_visited()
        True
        """
        self.__is_visited = True
             
    def reset_visited(self):
        """
        Sets the cell as not visited by setting the __is_visited attribute at False.
        
        :return: None
        :rtype: Nonetype
        :UC: None
        
        Examples:
        >>> c = Cell()
        >>> c.is_visited()
        False
        >>> c.set_visited()
        >>> c.is_visited()
        True
        >>> c.reset_visited()
        >>> c.is_visited()
        False
        """
        self.__is_visited = False
        
#--- Know if the cell is visited or not ---------------------------------------------------------------------------#
        
    def is_visited(self):
        """
        Returns the attribute __is_visited.
        
        :return: True if the cell has been visited, False otherwise
        :rtype: Bool
        :UC: None
        
        Examples:
        >>> c = Cell()
        >>> c.is_visited()
        False
        >>> c.set_visited()
        >>> c.is_visited()
        True
        """
        return self.__is_visited
       
