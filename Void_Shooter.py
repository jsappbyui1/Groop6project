"""Welcome to the Game"""

import random
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Void Shooter"

MOVEMENT_SPEED = 5


class Game (arcade.Window):

    def __init__(self):
        # Call parent class and set up the window, probably from the arcade library.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set background color.
        arcade.set_background_color(arcade.csscolor.BLACK)

        # variables that hold sprite lists initialization
        self.player_list = None
        self.bullet_list = None
        self.boss_list = None
        
        # player info initialization
        self.player_sprite = None

        # Track current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # No cursor shown
        self.set_mouse_visible(False)

    def setup(self):
        """Call this function to restart the game."""
        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip3_orange.png")
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """Render the Screen"""
        # This command has to happen before drawing starts.
        arcade.start_render()
       
        # Draw all the sprites
        self.player_list.draw()

    def on_update(self, detla_time):
        """Movement and game logic"""
        # Calculate speed based on keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = - MOVEMENT_SPEED
        
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = - MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
        
        # Call update to move the sprite
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed"""
        # If key is pressed, update the speed
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when user releases key"""
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


class Player(arcade.Sprite):
    
    def update(self):
        # Move player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top  =SCREEN_HEIGHT - 1


class BadguySprite(arcade.Sprite):
    pass


def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
