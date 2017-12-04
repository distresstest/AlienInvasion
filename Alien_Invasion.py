import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf



def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship and alien.
    ship = Ship(ai_settings, screen)
    #alien = Alien(ai_settings, screen)
    
    # Make a groups to store bullets and aliens in.
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Check for events.  
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # Update ship, bullets, aliens position.
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        
        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))
        
        # Update the screen.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
 
        
run_game()
 
