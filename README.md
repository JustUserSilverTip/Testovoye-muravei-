# Testovoye-muravei

Решение #1 (используем двумерные списки для создания поля)
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    28                                         def ant_path(width, height):
    29     24.4 MiB      1.0 MiB           1       image = create_blank_image(width, height)
    30     33.6 MiB      9.2 MiB     1051651       pixels = [[1 for _ in range(width)] for _ in range(height)]
    31     33.6 MiB      0.0 MiB           1       x, y = width // 2, height // 2  # Начальные координаты муравья
    32     33.6 MiB      0.0 MiB           1       direction = 0  # Начальное направление (0 - вверх, 1 - вправо, 2 - вниз, 3 - влево)
    33
    34     33.6 MiB      0.0 MiB       35694       while 0 <= x < width and 0 <= y < height:
    35     33.6 MiB      0.0 MiB       35693           direction = update_direction_and_pixel(x, y, direction, pixels)
    36     33.6 MiB      0.0 MiB       35693           x, y = move_ant(x, y, direction)
    37
    38     33.6 MiB    -35.9 MiB        1025       for y in range(height):
    40     33.6 MiB -36726.8 MiB     1048576               image.putpixel((x, y), pixels[y][x])
    41     34.6 MiB      0.9 MiB           1       image.save("ant_path.png")
    42     34.6 MiB      0.0 MiB           1       return image
```
Решение #2 (используем объект изображения PIL)
```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    27     23.2 MiB     23.2 MiB           1   @profile
    28                                         def ant_path(width, height):
    29     24.2 MiB      1.0 MiB           1       image = create_blank_image(width, height)
    30     24.2 MiB      0.0 MiB           1       pixels = image.load()
    31     24.2 MiB      0.0 MiB           1       x, y = width // 2, height // 2  # Начальные координаты муравья
    32     24.2 MiB      0.0 MiB           1       direction = 0  # Начальное направление (0 - вверх, 1 - вправо, 2 - вниз, 3 - влево)
    33
    34     24.2 MiB      0.0 MiB       35694       while 0 <= x < width and 0 <= y < height:
    35     24.2 MiB      0.0 MiB       35693           direction = update_direction_and_pixel(x, y, direction, pixels)
    36     24.2 MiB      0.0 MiB       35693           x, y = move_ant(x, y, direction)
    37
    38     25.1 MiB      0.9 MiB           1       image.save("ant_path.png")
    39     25.1 MiB      0.0 MiB           1       return image
```
Число черных клеток на изображении: 3683
![Screenshot](ant_path.png)
Инструкция для запуска:

1) Клонирование репозитория
```
git clone https://github.com/JustUserSilverTip/Testovoye-muravei-.git
```
2) Установка зависимостей
```
pip install -r requirements.txt
```
3) Запуск варианта с list comprehension:
```
python main.py
```
4) Запуск варианта с объектом изображения PIL:
```
python main2.py
```
