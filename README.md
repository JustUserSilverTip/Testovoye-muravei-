# Testovoye-muravei

from PIL import Image
import numpy as np

def ant_path(width, height):
    pixels = [[1 for _ in range(width)] for _ in range(height)] # Cоздаем поле
    x, y = width // 2, height // 2  # Начальные координаты муравья
    direction = 0  # Начальное направление (0 - вверх, 1 - вправо, 2 - вниз, 3 - влево)

    while 0 <= x < width and 0 <= y < height:
        if pixels[y][x] == 1:  # Если клетка белая
            direction = (direction + 1) % 4  # Поворачиваем на 90° по часовой стрелке
            pixels[y][x] = 0  # Инвертируем пиксель (черный)
        else:  # Если клетка черная
            direction = (direction - 1) % 4  # Поворачиваем на 90° против часовой стрелки
            pixels[y][x] = 1  # Инвертируем пиксель (белый)

        # Перемещаем муравья вперед на одну клетку в зависимости от направления
        if direction == 0:  # Вверх
            y -= 1
        elif direction == 1:  # Вправо
            x += 1
        elif direction == 2:  # Вниз
            y += 1
        elif direction == 3:  # Влево
            x -= 1

    # Создаем изображение из списка пикселей
    image = Image.new("1", (width, height))
    image.putdata([pixel for row in pixels for pixel in row])
    image.save("ant_path.png")
    return image
    
# Вызываем функцию с указанными размерами поля
image = ant_path(1024, 1024)

# Подсчитываем число черных клеток на изображении
black_pixels = sum(1 for pixel in image.getdata() if pixel == 0)
print(f"Число черных клеток на изображении: {black_pixels}")
