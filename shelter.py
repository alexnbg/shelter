import datetime
from animal import Animal
from id_gen import id_gen

class Shelter:
    
    list_animals = []

    def __init__(self,
                name,
                id_counter_0 = 0
                ):
        self.name = name
        self.id_counter = id_gen(id_counter_0)


# Methods

    def add_animal_manual(self):
        curent_animal = Animal(self.id_counter.id,
                            datetime.date.today().isoformat(),
                            self.name,
                            input("Animal type: "),
                            input("Animal name: "),
                            input("Age of the animal: "),
                            input("Caretaker name: "))
        self.list_animals.append(curent_animal)

    def add_animal(self,
                    animal_type = None,
                    name = '',
                    age = 0,
                    caretaker = 'Unassigned',
                    alive_status = True
                    ):
        curent_animal = Animal(self.id_counter.id,
                            datetime.date.today().isoformat(),
                            self.name,
                            animal_type,
                            name,
                            age,
                            caretaker,
                            alive_status)
        self.list_animals.append(curent_animal)
    
    def remove_animal(self, id):
        for item in self.list_animals:
            if item.id == id:
                self.list_animals.remove(item)
    
    def print_list(self):
        print (
                '\n', 
                f'List of the animals in {self.name}\n')
        print (
                'ID'.rjust(4),
                'Date added'.ljust(11),
                'Type'.ljust(8),
                'Name'.ljust(12),
                'Age'.ljust(5),
                'Caretaker'.ljust(12),
                'Status'.ljust(10))
        for item in self.list_animals:
            print (
                str(item.id).rjust(4),
                item.date_create.ljust(11),
                item.animal_type.ljust(8),
                item.name.ljust(12),
                str(item.age).ljust(5),
                item.caretaker.ljust(12),
                'Alive' if item.alive_status else 'Deceased')
        print('\n')
