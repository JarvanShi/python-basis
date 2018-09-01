import time

sentence = input('Please enter a sentence:')

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print('系统正在打印中...3')
time.sleep(1)
print('系统正在打印中...2')
time.sleep(1)
print('系统正在打印中...1')
time.sleep(1)

print(' ' * left_margin + '-' * box_width)
print(' ' * left_margin + ' ' * box_width)
print(' ' * ((screen_width - text_width) // 2) + sentence)
print(' ' * left_margin + ' ' * box_width)
print(' ' * left_margin + '-' * box_width)