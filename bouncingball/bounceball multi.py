
import arcade
import math
import time
import random


screen_width = 1000
screen_height = 500


class Ball:

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self .position_x = position_x
        self .position_y = position_y
        self .change_x = change_x
        self .change_y = change_y
        self .radius = radius
        self .color = color

    def draw(self):

        arcade.draw_circle_filled(self .position_x, self .position_y, self .radius, self .color)


    def update(self):

        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.change_x *= -1
            
        
        if self.position_x > screen_width - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > screen_height - self.radius:
            self.change_y *= -1





class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super() .__init__(width,height,title)

        arcade.set_background_color((200,200,220))

        self.balls_list =[]
        for i in range(150):
            ball = Ball(random.randrange(50,200), random.randrange(50,200), random.randrange(1,10) * (random.random() * 2), random.randrange(1,10) * (random.random() * 2), random.randrange(10,20) * (random.random() * 2), (random.randrange(1,255),random.randrange(1,255), random.randrange(1,255),random.randrange(1,255) ))
            self.balls_list.append(ball)

        
        
    def on_draw(self):
        arcade.start_render()

        for ball in self.balls_list:
            ball.draw()

        


    def on_update(self, delta_time):



        for ball in self.balls_list:
            ball.update()


    






def main():


  




    window = MyGame(screen_width, screen_height, "Drawing Example")

    arcade.run()



main()






