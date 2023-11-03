from memory_profiler import profile
from PIL import Image

def create_blank_image(width, height):
    return Image.new("1", (width, height), color=1)

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

def update_direction_and_pixel(x, y, direction, pixels):
    if pixels[x, y] == 1:  # Если клетка белая
        direction = (direction + 1) % 4  # Поворачиваем на 90° по часовой стрелке
        pixels[x, y] = 0  # Инвертируем пиксель (черный)
    else:  # Если клетка черная
        direction = (direction - 1) % 4  # Поворачиваем на 90° против часовой стрелки
        pixels[x, y] = 1  # Инвертируем пиксель (белый)
    return direction

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