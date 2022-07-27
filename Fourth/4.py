import json


class Dog:
    def get_file(self):
        with open('Response.json', 'r', encoding='utf-8') as f:
            path_d = json.load(f)
            return path_d

    def help_move(self):
        move = ('Move through the maze:\n'
                'u - up\n'
                'd - down\n'
                'l - left\n'
                'r - right\n')
        return move

    def move_maze(self):
        move = Dog.get_file(self)
        count = 0
        name = input('Tell me please, what is your name:\n ')
     
        while True:
            inp = input('Enter your path: ')
            result = list(move.values())[count]

            if inp not in result.keys():
                print('You entered the wrong move')
                continue
            print(result[inp])
            
            if result[inp] == 'Sharyk found the right path':
                count += 1
                print(count)
            
            elif result[inp] == 'Sharyk got lost' or result[inp] == 'Sharyk hit the wall' or result[inp] == 'Sharyk shook and ran away':
                print("You lose.\n Do you want to save the result of the game?")
                break

            if count == len(list(move.values())):
                print('Congratulation! Finish!')
                break
        
        name_saves = input('Select y or n: \n')
        if name_saves == 'y':
            value = {
                'Name': name,
                'Saved move': count
            }
            
            json.dump(value, open('result.json', 'w'), indent=2)
        else:
            print('Your result has not been saved') 


d = Dog()
print(d.help_move())
print(d.move_maze())
