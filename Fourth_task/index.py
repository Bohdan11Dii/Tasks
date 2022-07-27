# import csv, os, sys, time
# from copy import copy
#
# def get_maze(file):
#     f = open(file, 'r')
#     reader = csv.reader(f)
#     maze = []
#     for line in reader:
#         maze.append(line)
#     return maze
#
# def display_maze(m, path):
#     m2 = copy(m)
#     # os.system('clear')
#
#     for item in path:
#         m2[item[0]][item[1]] = '.'
#     m2[path[-1][0]][path[-1][1]] = "A"
#     draw = ''
#
#     for row in m2:
#         for item in row:
#             item = str(item).replace("1", "#")
#             item = str(item).replace("0", " ")
#
#             draw += item
#         draw += '\n'
#
#     print(draw)
#
#
#
#
#
#
# def move(path):
#     # time.sleep(1)
#     cur = path[-1]
#     display_maze(maze, path)
#     # possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]
#     possibles = [(cur[0], cur[1] + 1)]
#     print(f'Your coordinates: {possibles}')
#
#     for item in possibles:
#         # if buttons == '1' or '2' or '3' or '4' and maze[item[0]][item[1]] != '1':
#         #         continue
#         if maze[item[0]][item[1]] == '1':
#             print('Шарик ударился о стену, игра закончена')
#             break
#         if item in path:
#             continue
#         elif maze[item[0]][item[1]] == 'B':
#             path += (item,)
#             display_maze(maze, path)
#             input('Finish')
#
#
#
#             # os.system('clear')
#             # sys.exit()
#
#         else:
#             newpath = path + (item, )
#             move(newpath)
#
#
#
# # display_maze(maze, [])
#
#
# if __name__ == '__main__':
#     # while True:
#     # buttons = input('Введіть ваші дії: \n'
#     #                 '1 - вверх \n'
#     #                 '2 - вниз \n'
#     #                 '3 - вправо \n'
#     #                 '4 - вліво \n')
#     # if buttons == '1':
#     #     pass
#
#     maze = get_maze('maze.csv')
#
#     move(((1, 0),))
#
#
#
#
#
#
#


print('Добро пожаловать в игру Лабиринт')
print('Чтобы выбрать куда направится,введите одно слово из заключенных в кавычки')
room = 1
while room > 0:
    if room == 1:
        print('Вы находитесь в пещере на развилке. Вы можете пойти «налево», «направо» или «прямо».')
        direction = input()
        while direction != 'налево' and direction != 'прямо' and direction != 'направо':
            direction = input()
        if direction == 'налево':
            print('Вы пошли налево.')
            room = 2
        elif direction == 'прямо':
            print('Вы увидели пирата,который прятал своё сокровище.')
            room = -1
        elif direction == 'направо':
            print('Вы зашли в тёмную комнату,через некоторое время вы упали к тоннелям')
            room = -1
    elif room == 2:
        print('Вы выберете «левый» или «правый»? Или повернёте «назад»?')
        direction = input()
        while direction != 'левый' and direction != 'правый' and direction != 'назад':
            direction = input()
        if direction == 'левый':
            print('Вы вернулись в тёмную комнату')
            room = -1
        elif direction == 'правый':
            print('Вы смело вошли в правый тоннель. Но за ней вас поджидал пират,который вас убил')
            room = -2
        elif direction == 'назад':
            print('Вы отправились к начальной развилке.')
            room = 1