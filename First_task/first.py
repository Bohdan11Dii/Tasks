import requests
import json

GET_JOKES = 'https://v2.jokeapi.dev/joke/Any?type=single'
NECESSARY_KEY = 'code'
NUMBER_OF_REQUESTS = 4


requests_amount = 0
saved_jokes_amount = 0
invalid_jokes_amount = 0
valid_jokes_amount = 0
storage = []


for i in range(NUMBER_OF_REQUESTS):
    response = requests.get(url=GET_JOKES)
    response = response.json()
    key = f'joke_{i}'
    value = response['joke']
    joke_for_saving = {
        key: value
    }
    storage.append(joke_for_saving)

    if len(value) > 60:
        saved_jokes_amount +=1

        if NECESSARY_KEY in value:
            valid_jokes_amount += 1

    else:
        invalid_jokes_amount += 1
    requests_amount += 1


data_json = [
    {
        'data': storage
    },
    {"requests_amount": requests_amount},
    {"saved_jokes_amount": saved_jokes_amount},
    {"invalid_jokes_amount": invalid_jokes_amount},
    {"valid_jokes_amount": valid_jokes_amount}
]


json.dump(data_json, open('result.json', 'w'), indent=2)










