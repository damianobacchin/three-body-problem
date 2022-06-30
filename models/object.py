class Object:
    def __init__(self, name, id, mass, pos, vel):
        self.name = name
        self.id = id
        self.mass = mass
        self.pos = {
            'x': pos[0],
            'y': pos[1],
            'z': pos[2]
        }
        self.vel = {
            'x': vel[0],
            'y': vel[1],
            'z': vel[2]
        }
    
    def distance(self, obj):
        return (
            obj.pos['x'] - self.pos['x'],
            obj.pos['y'] - self.pos['y'],
            obj.pos['z'] - self.pos['z']
        )