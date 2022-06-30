from data.objects import objects
from models.object import Object
from models.system import System


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

    print(system.objects)
