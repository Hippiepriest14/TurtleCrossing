from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1,6)
        if chance == 1:

            new_car = Turtle()
            new_car .color(random.choice(COLORS))
            new_car .shape("square")
            new_car .penup()
            new_car .shapesize(stretch_len=2)
            new_car .setposition(300,random.randint(-230,230))
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def update_speed(self):
        self.car_speed += MOVE_INCREMENT


