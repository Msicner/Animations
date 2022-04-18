"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from os import linesep
from typing import List
from random import random
from constants import *
from math import sin, cos, pi
from turtle import *


__author__ = ""  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction


    def tick(self):
        self.location = self.location.add(self.direction)
        self.pen = Turtle()
        #self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(self.location.x, self.location.y)
        self.pen.pendown()
        self.pen.color(COLOR)
        self.pen.dot(CELL_RADIUS)
        #print("print")


    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"

class Line:
    """An individual subject in the simulation."""
    location: Point
    opacity: float

    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"

class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            self.population.append(Cell(start_loc, start_dir))
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        n = 0
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
            print(n)
            n += 1

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * BOUNDS_WIDTH - MAX_X
        start_y = random() * BOUNDS_HEIGHT - MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x >= MAX_X or cell.location.x <= MIN_X:
            cell.direction.x = cell.direction.x * (-1)
        if cell.location.y >= MAX_Y or cell.location.y <= MIN_Y:
            cell.direction.y = cell.direction.y * (-1)


    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False