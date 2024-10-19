W_width = 1280
W_height = 720

BLOCK_MAP = [
  '666666666666',
  '444444444444',
  '333333333333',
  '222222222222',
  '111111111111',
  '            ',
  '            ',
  '            ',
  '            '
]

COLOR_LEGEND = {
  '1': 'blue',
  '2': 'green',
  '3': 'red',
  '4': 'orange',
  '5': 'purple',
  '6': 'bronce',
  '7': 'grey'
}

GAP_SIZE = 2
B_height = W_height / len(BLOCK_MAP) - GAP_SIZE
B_width = W_width / len(BLOCK_MAP[0]) - GAP_SIZE