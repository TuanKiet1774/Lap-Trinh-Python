import pygame, sys, time
from settings import *
from sprites import Player, Ball, Block, Upgrade, Projectile
from surfacemaker import SurfaceMaker
from random import choice, randint

class Game:
  def __init__(self):
    pygame.init()
    self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Breakout')
    self.bg = self.create_bg()
    self.all_sprites = pygame.sprite.Group()
    self.block_sprites = pygame.sprite.Group()
    self.upgrade_sprites = pygame.sprite.Group()
    self.projectile_sprites = pygame.sprite.Group()
    self.surfacemaker = SurfaceMaker()
    self.reset_game()

  def reset_game(self):
    self.all_sprites.empty()
    self.block_sprites.empty()
    self.upgrade_sprites.empty()
    self.projectile_sprites.empty()
    self.player = Player(self.all_sprites, self.surfacemaker)
    self.stage_setup()
    self.ball = Ball(self.all_sprites, self.player, self.block_sprites)
    self.heart_surf = pygame.image.load('./graphics/other/heart.png').convert_alpha()
    self.heart_surf = pygame.transform.scale(self.heart_surf, (20, 20))
    self.projectile_surf = pygame.image.load('./graphics/other/projectile.png').convert_alpha()
    self.can_shoot = True
    self.shoot_time = 0
    self.laser_sound = pygame.mixer.Sound('./sounds/laser.wav')
    self.laser_sound.set_volume(0.1)
    self.powerup_sound = pygame.mixer.Sound('./sounds/powerup.wav')
    self.powerup_sound.set_volume(0.1)
    self.laserhit_sound = pygame.mixer.Sound('./sounds/laser_hit.wav')
    self.laserhit_sound.set_volume(0.02)
    self.music = pygame.mixer.Sound('./sounds/music.wav')
    self.music.set_volume(0.1)
    self.music.play(loops=-1)

  def create_upgrade(self, pos):
    upgrade_type = choice(UPGRADES)
    Upgrade(pos, upgrade_type, [self.all_sprites, self.upgrade_sprites])

  def create_bg(self):
    bg_original = pygame.image.load('./graphics/other/bg.png').convert()
    scale_factor = WINDOW_HEIGHT / bg_original.get_height()
    scaled_width = int(bg_original.get_width() * scale_factor)
    scaled_height = int(bg_original.get_height() * scale_factor)
    scaled_bg = pygame.transform.scale(bg_original, (scaled_width, scaled_height))
    return scaled_bg

  def stage_setup(self):
    for row_index, row in enumerate(BLOCK_MAP):
      for col_index, col in enumerate(row):
        if col != ' ':
          x = col_index * (BLOCK_WIDTH + GAP_SIZE) + GAP_SIZE // 2
          y = TOP_OFFSET + row_index * (BLOCK_HEIGHT + GAP_SIZE) + GAP_SIZE // 2 + 5
          Block(col, (x, y), [self.all_sprites, self.block_sprites], self.surfacemaker, self.create_upgrade)

  def display_hearts(self):
    font = pygame.font.Font('Fonts/SVN-Determination Sans.otf', 20)
    text_surface = font.render("Your Life", True, (255, 255, 255))
    self.display_surface.blit(text_surface, (2, 0))
    for i in range(self.player.hearts):
      x = (text_surface.get_width() + 10) + i * (self.heart_surf.get_width() + 2)
      self.display_surface.blit(self.heart_surf, (x, 4))

  def upgrade_collision(self):
    overlap_sprites = pygame.sprite.spritecollide(self.player, self.upgrade_sprites, True)
    for sprite in overlap_sprites:
      self.player.upgrade(sprite.upgrade_type)
      self.powerup_sound.play()

  def create_projectile(self):
    self.laser_sound.play()
    for projectile in self.player.laser_rects:
      Projectile(
        projectile.midtop - pygame.math.Vector2(0, 30),
        self.projectile_surf,
        [self.all_sprites, self.projectile_sprites])

  def laser_timer(self):
    if pygame.time.get_ticks() - self.shoot_time >= 500:
      self.can_shoot = True

  def projectile_block_collision(self):
    for projectile in self.projectile_sprites:
      overlap_sprites = pygame.sprite.spritecollide(projectile, self.block_sprites, False)
      if overlap_sprites:
        for sprite in overlap_sprites:
          sprite.get_damage(1)
        projectile.kill()
        self.laserhit_sound.play()

  def game_over_screen(self):
    self.music.stop()
    
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.set_alpha(150)  # Độ trong suốt của nền (0 là trong suốt hoàn toàn, 255 là không trong suốt)
    overlay.fill((0, 0, 0))  # Màu nền (đen)
    self.display_surface.blit(overlay, (0, 0))
    
    font = pygame.font.Font('Fonts/SVN-Determination Sans.otf', 60)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    retry_text = pygame.font.Font('Fonts/SVN-Determination Sans.otf', 40).render("Press R to Restart or X to Exit", True, (255, 255, 255))
    # Tính toán vị trí để vẽ text
    game_over_text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    retry_text_rect = retry_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))

    # Vẽ text lên màn hình
    self.display_surface.blit(game_over_text, game_over_text_rect)
    self.display_surface.blit(retry_text, retry_text_rect)
    pygame.display.update()
    
    waiting = True
    while waiting:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
            self.reset_game()
            waiting = False
          elif event.key == pygame.K_x:
            pygame.quit()
            sys.exit()

  def run(self):
    last_time = time.time()
    while True:
      dt = time.time() - last_time
      last_time = time.time()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.ball.active = True
            if self.can_shoot:
              self.create_projectile()
              self.can_shoot = False
              self.shoot_time = pygame.time.get_ticks()

      if self.player.hearts <= 0:
        self.game_over_screen()

      self.display_surface.blit(self.bg, (0, 0))
      self.all_sprites.update(dt)
      self.upgrade_collision()
      self.laser_timer()
      self.projectile_block_collision()
      self.all_sprites.draw(self.display_surface)
      self.display_hearts()
      pygame.display.update()

if __name__ == '__main__':
  game = Game()
  game.run()
