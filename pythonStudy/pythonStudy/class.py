class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name} {self.age}')

shark = Monster('상어', 8)
wolf = Monster('늑대', 3)

shark.say()
wolf.say()