
""" Class Bullet"""
class Bullet(arcade.Sprite):

    def __init__(self):
        self.bullet_list = None

    def setup(self):
        self.bullet_list = arcade.SpriteList()

    def createBullet(self,start_x,start_y,angle,owner):

        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
        bullet.center_x = start_x
        bullet.center_y = start_y
        # Angle the bullet sprite
        bullet.angle = math.degrees(angle)

        #Owner
        bullet.owner = owner

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED
        
        self.bullet_list.append(bullet)

    def update(self,enemy,player):
        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()
                        # Check this bullet to see if it hit a coin
            if(bullet.owner == """player"""):
                hit_list = arcade.check_for_collision_with_list(bullet, enemy)
            else:
                hit_list = arcade.check_for_collision_with_list(bullet, player)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            #self.score += 1 # <-- For every coin we hit, add to the score and remove the coin

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()
    
    def draw(self):
        self.bullet_list.draw()
