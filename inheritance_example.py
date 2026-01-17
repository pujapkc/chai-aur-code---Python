class Animal:
    def __init__(self):
        num_of_eyes = 2

    def breathe(self):
        print("Inhale,exhale")

class fish(Animal):
    def __init__(self):
        super().__init__()

memo = fish()

memo.breathe()