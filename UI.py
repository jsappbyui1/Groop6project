import arcade
import random
import os


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5

''' This is the opening menu screen, and it leads to the instructions view '''
class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.CARNELIAN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Bullet Hell", WIDTH/2, HEIGHT/2,
                         arcade.color.AQUAMARINE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to continue", WIDTH/2, HEIGHT/2-75,
                         arcade.color.AQUAMARINE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)

''' NEED TO UPDATE THIS- Change instructions depending on rules of the game '''
class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

''' CODE FOR GAME GOES HERE '''
class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_overview = GameOverView()
        self.window.show_view(game_overview)

    

       
        
        


          
''' Post Game goes here '''
class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

       

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()