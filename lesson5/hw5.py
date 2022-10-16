from animal import Animal
from dog import Dog
from cat import Cat
from lesson5.gibrid import Gibrid

animal = Animal(name="Tuzik", weight=10, age=2)
print(animal.__dict__)
# print(animal.name)
animal.print_info()
print(animal.COLOR)
print(Animal.COLOR)
# animal.set_name('Lelik')
# animal.print_info()
# print(animal.COLOR)
# print(Animal.COLOR)


dog1 = Dog('Barbos', 5, 10, 'Dvorterrer')
print(dog1.__dict__)


dog1.print_info()
dog1.is_barking()

cat1 = Cat('Vasya', 12, 11)
print(cat1.__dict__)
cat1.print_info()

# cat2 = Cat('Georgii')
# print(cat2.__dict__)

gibrid = Gibrid('Puch', 12, 25, 'manul')
gibrid.print_create()
print(gibrid.__dict__)
print(gibrid.breed)

