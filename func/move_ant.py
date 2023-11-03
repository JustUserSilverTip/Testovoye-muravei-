def move_ant(x, y, direction):
    if direction == 0:  # Вверх
        y -= 1
    elif direction == 1:  # Вправо
        x += 1
    elif direction == 2:  # Вниз
        y += 1
    elif direction == 3:  # Влево
        x -= 1
    return x, y