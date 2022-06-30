class System:
    def __init__(self, name):
        self.name = name
        self.objects = []
    
    def add_object(self, new_object):
        self.objects.append(new_object)