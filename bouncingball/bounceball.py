
import arcade
import math
import time


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

        self.ball = Ball(50, 50, 3, 3, 15, (180, 10, 10))
    def on_draw(self):

        arcade.start_render ()

        

        self.ball.draw()

    def update(self, delta_time):


        self.ball.update()


    






def main():


  




    window = MyGame(screen_width, screen_height, "Drawing Example")

    arcade.run()



main()






