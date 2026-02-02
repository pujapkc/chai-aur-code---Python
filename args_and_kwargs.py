def calculate(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)


calculate(key = 3,value = 2)