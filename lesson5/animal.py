class Animal:
    COLOR = 'grey'
    def __init__(self, name='Animal', age=0, weight=0):
        self.name = name
        self.age = age
        self.weight = weight
        print('Create object of Animal class')

    def print_info(self):
        print(f'Name animal is {self.name} with weight {self.weight} and age {self.age}')

    # def get_name(self):
    #     return self.__name if self.__name else None
    #
    # def set_name(self, name):
    #     self.__name = name
    #     self.COLOR = 'blue'
