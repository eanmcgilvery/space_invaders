import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import h_score
from ship import Ship
import game_functions as gf
from main_menu import Start
from alien import UFO


def run_game():
    clock = pygame.time.Clock()

    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    high_score_button = h_score(ai_settings, screen, "HIGH SCORES")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    start = Start(screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    bunkers = Group()
    ufos = UFO(ai_settings, screen)

    gf.create_fleet(ai_settings, screen, aliens)
    gf.create_bunkers(ai_settings, screen, bunkers)

    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, alien_bullets, start)
        if stats.game_active and stats.game_pause:
            ufos.update(screen)
            alien_bullets.update()
            gf.alien_bullet(ai_settings, screen, aliens, alien_bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, aliens, bullets, bunkers, alien_bullets, ufos)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, alien_bullets)

        ship.update(stats)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets,
                         play_button, high_score_button, bunkers, start, ufos)
        clock.tick(60)


run_game()
