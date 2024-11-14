import random

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def generate_block_map():
    block_map = []
    num_random_rows=5
    total_rows=9
    length=12
    # Tạo các chuỗi ngẫu nhiên
    for _ in range(num_random_rows):
        random_string = ''.join(random.choice('1234567') for _ in range(length))
        block_map.append(random_string)
    
    # Thêm các chuỗi khoảng trắng
    for _ in range(total_rows - num_random_rows):
        block_map.append(' ' * length)  # Tạo chuỗi khoảng trắng với độ dài cố định
    return block_map
  
# Sử dụng hàm để tạo BLOCK_MAP
BLOCK_MAP = generate_block_map()

COLOR_LEGEND = {'1': 'blue', '2': 'green', '3': 'red',	'4': 'orange', '5': 'purple', '6': 'bronce', '7': 'grey',}

GAP_SIZE = 2
BLOCK_HEIGHT = WINDOW_HEIGHT / len(BLOCK_MAP) - GAP_SIZE
BLOCK_WIDTH = WINDOW_WIDTH / len(BLOCK_MAP[0]) - GAP_SIZE
TOP_OFFSET = WINDOW_HEIGHT // 30

UPGRADES = ['speed','laser','heart','size']