def update_direction_and_pixel(x, y, direction, pixels):
    if pixels[y][x] == 1:  # Если клетка белая
        direction = (direction + 1) % 4  # Поворачиваем на 90° по часовой стрелке
        pixels[y][x] = 0  # Инвертируем пиксель (черный)
    else:  # Если клетка черная
        direction = (direction - 1) % 4  # Поворачиваем на 90° против часовой стрелки
        pixels[y][x] = 1  # Инвертируем пиксель (белый)
    return direction
