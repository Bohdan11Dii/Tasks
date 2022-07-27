import json
path_d = {
    '0_r': {'u': 'wall', 'd': 'wall', 'l': 'wall', 'r': 'correct'},
    '1_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '2_r': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '3_l': {'u': 'wall', 'd': 'incorect path', 'l': 'correct', 'r': 'coward'},
    '4_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '5_l': {'u': 'wall', 'd': 'incorect path', 'l': 'correct', 'r': 'coward'},
    '6_d_n': {'u': 'coward', 'd': 'incorect path', 'l': 'wall', 'r': 'wall'},
    '7_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '8_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '9_u_n': {'u': 'incorect path', 'd': 'coward', 'l': 'wall', 'r': 'wall'},
    '10_d': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '11_u_n': {'u': 'incorect path', 'd': 'coward', 'l': 'wall', 'r': 'wall'},
    '12_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '13_l_n': {'u': 'wall', 'd': 'wall', 'l': 'incorect path', 'r': 'coward'},
    '14_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '15_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '16_d_n': {'u': 'coward', 'd': 'incorect path', 'l': 'wall', 'r': 'wall'},
    '17_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '18_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '19_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '20_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '21_l': {'u': 'wall', 'd': 'wall', 'l': 'correct', 'r': 'coward'},
    '22_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '23_r_n': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'incorect path'},
    '24_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '25_l': {'u': 'wall', 'd': 'wall', 'l': 'correct', 'r': 'coward'},
    '26_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '27_l': {'u': 'wall', 'd': 'wall', 'l': 'incorect path', 'r': 'coward'},
    '28_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '29_d': {'u': 'coward', 'd': 'correct', 'l': 'wall', 'r': 'wall'},
    '30_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
    '31_r': {'u': 'wall', 'd': 'wall', 'l': 'wall', 'r': 'correct'},
}

json.dump(path_d, open('Response.json', 'w'),ensure_ascii=False, indent=2)


move = ('Move through the maze:\n'
                'u - up\n'
                'd - down\n'
                'l - left\n'
                'r - right\n')
print(move)


# count = 0



# for i in path_d:
#     inp = input('Enter your path: \n')
#     result = path_d.values()
#     # print(result)
#     if inp in path_d.keys() and inp == 'correct':
#             count += 1
#             print('The Sharyk found the right path')
#             print(count)
            
    # elif i == 'wall':
    #     print('Sharyk hit the wall')
    #     break
    # elif i == 'coward':
    #     print('Sharyk shook and ran away')
    #     break
    # elif i == 'incorect path':
    #     print('Sharyk got lost')
    #     break
    # else:
    #     print('Finish game')
    #     break
    # # else:
    #     print('You entered the wrong move')
            
    # print(i)
    # result = list(path_d.values())[i]
    # while inp != result['correct']:
        
        # pass
       
    # if inp in result:
        # print(result[inp])
        # pass
        
    
    
# //////////////////////////////////////////////////


# from itertools import count


# path_d = {
#     '0_r': {'u': 'wall', 'd': 'wall', 'l': 'wall', 'r': 'correct'},
#     '1_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
#     '2_r': {'u': 'wall', 'd': 'correct', 'l': 'coward', 'r': 'wall'},
#     '3_d': {'u': 'coward', 'd': 'incorect path', 'l': 'correct', 'r': 'wall'},
# }

# count = 0
# while True:
#     inp = input('Enter your path: ')
    
#     result = list(path_d.values())[count]
#     # print(type(result))
#     if inp not in result.keys():
#         print('You entered the wrong move')
#         continue
#     print(result[inp])
#     if result[inp] == 'correct':
#         count += 1
#         print('The Sharyk found the right path')
#     elif result[inp] == 'wall':
#         print('Sharyk hit the wall')
#     elif result[inp] == 'coward':
#         print('Sharyk shook and ran away')
#     elif result[inp] == 'incorect path':
#         print('Sharyk got lost')
#     else:
#         print('You entered the wrong move')
       
#     if count == len(list(path_d.values())):
#         print('Congratulation! Finish!')
#         break
      
        
        
        
# path_d = {
#     '0_r': {'u': 'wall', 'd': 'wall', 'l': 'wall', 'r': 'correct'},
#     '1_r': {'u': 'wall', 'd': 'wall', 'l': 'coward', 'r': 'correct'},
#     '2_r': {'u': 'wall', 'd': 'correct', 'l': 'coward', 'r': 'wall'},
#     '3_d': {'u': 'coward', 'd': 'incorect path', 'l': 'correct', 'r': 'wall'},
# }

# counter = 0
# while True:
#     inp = input('Input step: ')
#     result = list(path_d.values())[counter]
#     print(result[inp])
#     if result[inp] == 'correct':
#         counter += 1
#     if counter == len(list(path_d.values())):
#         print('Congratulation! Finish!')
#         break