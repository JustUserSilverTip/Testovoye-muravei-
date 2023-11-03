from memory_profiler import profile
from func import (create_blank_image, move_ant, update_direction_and_pixel)

@profile
def ant_path(width, height):
    image = create_blank_image(width, height)
    pixels = image.load()
    x, y = width // 2, height // 2  # Начальные координаты муравья
    direction = 0  # Начальное направление (0 - вверх, 1 - вправо, 2 - вниз, 3 - влево)

    while 0 <= x < width and 0 <= y < height:
        direction = update_direction_and_pixel(x, y, direction, pixels)
        x, y = move_ant(x, y, direction)

    image.save("ant_path.png")
    return image

# Вызываем функцию с указанными размерами поля
image = ant_path(1024, 1024)

# Подсчитываем число черных клеток на изображении
black_pixels = sum(1 for pixel in image.getdata() if pixel == 0)
print(f"Число черных клеток на изображении: {black_pixels}")