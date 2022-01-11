
class id_gen:


    def __init__(self, id=0):
        self.id_0 = id

    def gen(self):
        self.id_0 += 1
        yield self.id_0
    
    @property
    def id(self):
        gen_id = self.gen()
        for i in gen_id:
            return i
            break
