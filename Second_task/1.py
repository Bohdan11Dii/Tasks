import json


def get_valid(names):
    names = names.split('=')[1].split(',')
    invalid_symbols = [str(n) for n in range(1, 11)]
    data = ''
    error = False
    error_message = None
    for name in names:
        for symbol in name:
            if symbol in invalid_symbols:
                error = True
                error_message = f'Ім"я {name} містить сисмвол:{symbol}'
                print(error_message)
                break
    if error is False and names == []:
        data = 'eto nikomy me nravitsa'
    elif error is False and len(names) == 2:
        data = f'{names[0]} and {names[1]} liked it' 
    elif error is False and len(names) == 3:
        data = f'{names[0]}, {names[1]}, {names[2]} liked it'
    elif error is False and len(names) > 3:
        data = f'{names[0]}, {names[1]} and more liked it'
        
    print(data)

    Response = [{
        'data': data,
        'error': error,
        'error_message': error_message
    }]
    json.dump(Response, open('Response.json', 'w'),ensure_ascii=False, indent=2)


first_url = "http://127.0.0.1:8000/likes?names=Андрей,Жанна,Катя,Макс"

second_url = 'http://127.0.0.1:8000/likes?names=Андрей_235,Жа__@$6SF?,Катя'

get_valid(first_url)
# get_valid(second_url)