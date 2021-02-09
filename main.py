from time import sleep
from PIL import ImageDraw, Image, ImageFont

print('\n'*100)

while True:
    try:
        size = int(input('How big would you like the magic square to be: '))
    except ValueError:
        print('\n     Invalid, please provide a number larger than 3\n')
        sleep(1.5)
        continue

    if size < 3:
        print('\n     Invalid, please provide a number larger than 3\n')
        sleep(1.5)
        continue

    break

grid = {}
for i in range(size):
    grid[i] = []
    for x in range(size):
        grid[i].append(0)

# Square Generation
if size%2==0: #even
    pass


else: #odd
    center = int(size/2)
    x = center
    y = 0
    value = 1
    running = True
    
    while running:
        grid[y][x]=value
        value += 1

        x += 1
        y -= 1

        if y < 0:
            y = size -1
        if x > size -1:
            x = 0

        while True:
            if grid[y][x] != 0:
                y -= 1
            if y < 0:
                y = size -1
            else:
                break

        if grid[y][x] != 0:
            running = False

    print('\n'*3)
    for row in grid:
        print(grid[row])
    input('\n'*3)

# Export
