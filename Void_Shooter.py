"""Welcome to the Game"""

import random
import arcade
import math
import os

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Void Shooter"

SPRITE_SCALING_LASER = 0.8

MOVEMENT_SPEED = 5
BULLET_SPEED = 5


class Game (arcade.Window):

    def __init__(self):
        self.boss = Boss()
        self.frame_count = 0

        # Call parent class and set up the window, probably from the arcade library.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set background color.
        arcade.set_background_color(arcade.csscolor.BLACK)

        # variables that hold sprite lists initialization
        self.player_list = None
        self.bullet_list = None
        
        # player info initialization
        self.player_sprite = None
        
        #Sounds
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")

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
        self.bullet_list = arcade.SpriteList()


        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip3_orange.png")
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)

        self.boss.settup()

    def on_draw(self):
        """Render the Screen"""
        # This command has to happen before drawing starts.
        arcade.start_render()
       
        # Draw all the sprites
        
        self.boss.draw()
        self.player_list.draw()
        self.bullet_list.draw()


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
        self.boss.update(self.frame_count,self.player_sprite)

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

class Boss(arcade.Sprite):

    def __init__(self):
        self.boss_sprite = None
        self.cycleLen = 100

    def settup(self):
        self.boss_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.75)
        self.boss_sprite.center_x = 500
        self.boss_sprite.center_y = SCREEN_HEIGHT - (self.boss_sprite.height / 8)
        self.boss_sprite.angle = 180
        

    def update(self,timer,player):
        self.timer = timer
        self.player_sprite = player
        self.aimAtPlayer()
        if self.timer % self.cycleLen == 0:
            self.chooseLocation()
            
            self.chooseAttack()
            #pattern = self.attack()
            #self.attack(pattern)
            if self.cycleLen > 100:
                self.cycleLen -= 100
                print(f"cycle lengnth is {self.cycleLen}")

    def aimAtPlayer(self):
        #aims the boss sprite at the player

        start_x = self.boss_sprite.center_x  #   <-- identifies boss's x position
        start_y = self.boss_sprite.center_y  #   <-- identifies boss's y position

        dest_x = self.player_sprite.center_x #   <-- identifies player's x position
        dest_y = self.player_sprite.center_y #   <-- identifies player's y position

        x_diff = dest_x - start_x            #   <-- compares the two x positions
        y_diff = dest_y - start_y            #   <-- compares the two y positions
        angle = math.atan2(y_diff, x_diff)   #   <-- calculates the angle difference

        self.boss_sprite.angle = math.degrees(angle)-90 #   <-- sets the boss's new faceing

    def chooseAttack(self):
        choiceList = ['basic','split','random']
        choice = random.choice(choiceList)
        if choice == 'basic':
            print("basic attack")
        if choice == 'split':
            print("split attack")
        if choice == 'random':
            print("ranodm attack")

    def chooseLocation(self):
        choiceList = ['top','left','right','bottom']
        choice = random.choice(choiceList)
        if choice == 'top':
            print("boss going to top")
            self.boss_sprite.center_x = SCREEN_WIDTH/2
            self.boss_sprite.center_y = SCREEN_HEIGHT - (self.boss_sprite.height / 8)
        if choice == 'left':
            print("boss going to left")
            self.boss_sprite.center_x = (self.boss_sprite.width / 8)
            self.boss_sprite.center_y = SCREEN_HEIGHT/2
        if choice == 'right':
            print("boss going to right")
            self.boss_sprite.center_x = SCREEN_WIDTH - (self.boss_sprite.width / 8)
            self.boss_sprite.center_y = SCREEN_HEIGHT/2 
        if choice == 'bottom':
            print("boss going to bottom")
            self.boss_sprite.center_x = SCREEN_WIDTH/2
            self.boss_sprite.center_y = (self.boss_sprite.height / 8)

    def draw(self):
        self.boss_sprite.draw()

    def attack(self, pattern):
        pass

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
