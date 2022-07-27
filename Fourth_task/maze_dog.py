import csv, os, sys, time


def get_maze(file):
    f = open(file, 'r')
    reader = csv.reader(f)
    maze = []
    for line in reader:
        maze.append(line)
    return maze

def display_maze(m, path):
    m2 = m[:]
    os.system('clear')

    for item in path:
        m2[item[0]][item [1]] = '.'
    m2[path[-1][0]][path[-1][1]] = "A"
    draw = ''

    for row in m2:
        for item in row:
            item = str(item).replace("1", "#")
            item = str(item).replace("0", " ")

            draw += item
        draw += '\n'

    print(draw)


def move(path):
    time.sleep(1)
    cur = path[-1]
    display_maze(maze, path)
    possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]
    print(possibles)


    for item in possibles:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] == '1':
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == 'B':
            path += (item, )
            display_maze(maze, path)
            input('Finish')
            os.system('clear')
            sys.exit()

        else:
            newpath = path + (item, )
            move(newpath)


maze = get_maze('maze.csv')

move(((1, 0), ))
display_maze(maze, [])


