import pygame, sys, time
from settings import *
from sprites import Player, Ball, Block


class Game: 
  def __init__(self):
    #Khởi động Pygame tạo ra một cửa sổ với chiều dài và chiều rộng
    pygame.init()
    self.display = pygame.display.set_mode((W_width,W_height))
    pygame.display.set_caption("BreakOut")
    
    #Background
    self.gb = self.create_bg()
    
    #cài đặt nhóm Sprite
    self.all_sprites = pygame.sprite.Group()
    self.block_sprites = pygame.sprite.Group()
    
    #Cài đặt
    self.player = Player(self.all_sprites)
    self.ball = Ball(self.all_sprites,self.player,self.block_sprites)
    self.stage_setup()
    
  #tạo background cho game
  def create_bg(self):
    bg_original = pygame.image.load('BreakOut/Images/bg.png').convert()
    bg = pygame.transform.scale(bg_original,(W_width,W_height))
    return bg
  
  #Tạo các khối
  def stage_setup(self):
    #chu kỳ qua tất cả các hàng và cột của BLOCK MAP
    for row_index, row in enumerate(BLOCK_MAP):
      for col_index, col in enumerate(row):
        if col !=' ':
          #tìm vị trí x và y cho từng khối riêng lẻ
          x = col_index * (B_width + GAP_SIZE) + GAP_SIZE // 2
          y = row_index * (B_height + GAP_SIZE) + GAP_SIZE // 2
          Block(col,(x,y),[self.all_sprites,self.block_sprites])
    
    
    
  def run(self):
    last_time = time.time()
    while True:
      #Thời gian delta để cập nhật mọi phần tử trong cửa sổ ng chơi
      dt = time.time() - last_time
      last_time = time.time()
      
      
      for sk in pygame.event.get():
        if sk.type == pygame.QUIT: #Đóng cửa sổ
          pygame.quit()
          sys.exit()
        if sk.type == pygame.KEYDOWN:
          if sk.key == pygame.K_SPACE: #bóng rời đĩa
            self.ball.active = True
       
      #Vẽ khung
      self.display.blit(self.gb,(0,0))
      self.all_sprites.draw(self.display)
      
      #cập nhật sửa sổ
      self.all_sprites.update(dt)
      pygame.display.update() 
      
      
      
if __name__ == '__main__':
  game = Game()
  game.run()
    