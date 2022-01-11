class Animal:

    def __init__(self,
                id = 0,
                date_create = '',
                shelter = '',
                animal_type = '',
                name = '',
                age = 0,
                caretaker = 'Unassigned',
                alive_status = True
                ):

        self.id = id
        self.date_create = date_create
        self.shelter = shelter

        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.caretaker = caretaker
        self.alive_status = alive_status
