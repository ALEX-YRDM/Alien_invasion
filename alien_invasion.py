import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    #
    # # 设置背景色
    # bg_color = (230, 230, 230)

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    play_button = Button(ai_settings, screen, "play")

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.Update()
            # bullets.update()

            # 删除已经消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # print(len(bullets))
        gf.update_events(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
