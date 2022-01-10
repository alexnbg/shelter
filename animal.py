class Animal:

    def __init__(self,
                id = 0,
                date_create = None,
                shelter = '',
                animalType = None,
                name = '',
                age = 0,
                caretaker = 'Unassigned',
                aliveStatus = True
                ):

        self.id = id
        self.date_create = date_create
        self.shelter = shelter

        self.animalType = animalType
        self.name = name
        self.age = age
        self.caretaker = caretaker
        self.aliveStatus = aliveStatus
