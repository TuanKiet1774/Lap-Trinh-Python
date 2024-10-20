import pygame
from settings import *
from random import choice

class Player(pygame.sprite.Sprite):
  def __init__(self, groups):
    super().__init__(groups)
    
    #cài đặt đĩa đở bi
    self.image = pygame.Surface((W_width // 10,W_height // 20))
    self.image.fill('red')
    
    #cài đặt chuyển động của đĩa
    self.rect = self.image.get_rect(midbottom = (W_width // 2, W_height - 20))
    self.old_rect = self.rect.copy()
    self.direction = pygame.math.Vector2()
    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.speed = 300
  
  #điều khiển sprites
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
      self.direction.x = 1
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
    else:
      self.direction.x = 0
  
  #Giới hạn khung
  def screen_constraints(self):
    if self.rect.right > W_width:
      self.rect.right = W_width
      self.pos.x = self.rect.x
    if self.rect.left < 0:
      self.rect.left = 0
      self.pos.x = self.rect.x

  def update(self,dt):
    self.old_rect = self.rect.copy()
    self.input()
    self.pos += self.direction * self.speed * dt
    self.rect.x = round(self.pos.x)
    self.screen_constraints()
    
class Ball(pygame.sprite.Sprite):
  def __init__(self, groups, player,blocks):
    super().__init__(groups)
    
    #đối tượng va chạm
    self.player = player
    self.blocks = blocks
    
    #Giao diện trái bóng
    self.image = pygame.image.load('BreakOut/Images/ball.png').convert_alpha()
    
    #Cài đặt chuyển động
    self.rect = self.image.get_rect(midbottom = player.rect.midtop)
    self.old_rect = self.rect.copy()
    self.direction = pygame.math.Vector2((choice((1,-1)),-1))
    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.speed = 400
    
    self.active = False
  
  #Va chạm trong cửa sổ
  def window_collision(self,direction):
    if direction == 'horizontal':
      if self.rect.left < 0:
        self.rect.left = 0
        self.pos.x = self.rect.x
        self.direction.x *= -1
        
      if self.rect.right > W_width:
        self.rect.right = W_width 
        self.pos.x = self.rect.x
        self.direction.x *= -1
        
    if direction == 'vertical':
      if self.rect.top < 0:
        self.rect.top = 0
        self.pos.y = self.rect.y
        self.direction.y *= -1
        
      if self.rect.bottom > W_height:
        self.active = False
        self.direction.y = -1
  
  def collision(self,direction):
    #Tìm các đối tượng chồng chéo
    overlap_sprites = pygame.sprite.spritecollide(self,self.blocks, False)
    if self.rect.colliderect(self.player.rect):
      overlap_sprites.append(self.player)
      
    if overlap_sprites:
      if direction == 'horizontal':
        for sprite in overlap_sprites:
          if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
            self.rect.right = sprite.rect.left - 1
            self.pos.x = self.rect.x
            self.direction.x *= -1
            
          if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
            self.rect.left = sprite.rect.right + 1
            self.pos.x = self.rect.x
            self.direction.x *= -1
          
      if direction == 'vertical':
        for sprite in overlap_sprites:
          if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
            self.rect.bottom = sprite.rect.top - 1
            self.pos.y = self.rect.y
            self.direction.y *= -1
            
          if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
            self.rect.top = sprite.rect.bottom + 1
            self.pos.y = self.rect.y
            self.direction.y *= -1
    
  def update(self,dt):
    if self.active:
      
      if self.direction.magnitude() != 0:
        self.direction = self.direction.normalize()
        
      #Tạo old rect
      self.old_rect = self.rect.copy()
      
      
      #chuyển động ngang + va chạm
      self.pos.x += self.direction.x * self.speed * dt
      self.rect.x = round(self.pos.x)
      self.collision('horizontal')
      self.window_collision('horizontal') 
      
      #chuyển động thẳng đứng + va chạm
      self.pos.y += self.direction.y * self.speed * dt
      self.rect.y = round(self.pos.y)
      self.collision('vertical')
      self.window_collision('vertical') 
    else:
      self.rect.midbottom = self.player.rect.midtop
      self.pos = pygame.math.Vector2(self.rect.topleft)
      
class Block(pygame.sprite.Sprite):
  def __init__(self, block_type, pos ,groups):
    super().__init__(groups)
    self.image = pygame.Surface((B_width,B_height))
    self.rect = self.image.get_rect(topleft = pos)
    self.old_rect = self.rect.copy()
    
    