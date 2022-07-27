data = [{
    'counter': "Австрия",
}]




for i in data:
    for item in list(i.values()):
        # print(item)
        pass

def get_small_names():
    your_input = input('Input your change: \n').split(' ')
    # print(your_input)
    for i in your_input:
        i = list(i)
        print(i)
        if your_input in data:
            pass
get_small_names()