from data.objects import objects
from models.object import Object
from models.system import System


def calc(system):
    for elem in system.objects:
        for pair in system.objects:
            if (elem.id == pair.id):
                continue
            d = elem.distance(pair)
            print(d)
            

if __name__ == '__main__':
    # Inizializing system
    system = System(name='Three Body Problem')
    for elem in objects:
        system.add_object(Object(
            name=elem['name'],
            id=elem['id'],
            mass=elem['mass'],
            pos=elem['pos-i'],
            vel=elem['vel-i']
        ))

    calc(system)
