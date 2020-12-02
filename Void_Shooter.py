"""Welcome to the Game"""

import random
import arcade
import math

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Void Shooter"

MOVEMENT_SPEED = 5

class Game (arcade.Window):

    def __init__(self):

        self.frame_count = 0

        # Call parent class and set up the window, probably from the arcade library.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set background color.
        arcade.set_background_color(arcade.csscolor.BLACK)

        # variables that hold sprite lists initialization
        self.player_list = None
        self.boss_list = None
        
        # player info initialization
        self.player_sprite = None
        self.boss_sprite = None

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
        self.enemy_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip3_orange.png")
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        # Add top-left enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

    def on_draw(self):
        """Render the Screen"""
        # This command has to happen before drawing starts.
        arcade.start_render()
       
        # Draw all the sprites
        self.enemy_list.draw()
        
        self.player_list.draw()


    def on_update(self, detla_time):
        """Movement and game logic"""
        # Calculate speed based on keys pressed
        self.frame_count += 1
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

        for enemy in self.enemy_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle)-90


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




def main():
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
