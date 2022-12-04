import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing!")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.up, "Up")
car = CarManager()
scoreboard = Scoreboard()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.update_scoreboard()
        car.update_speed()
        player.next_level()





screen.exitonclick()


