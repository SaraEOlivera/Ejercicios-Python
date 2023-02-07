""" def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(400)) """

""" def festejar(opciones):
    match opciones:
        case 1:
            return "Muy caro"
        case 2:
            return "Barato pero lejos"
        case 3:
            return "Opiniones pobres"
        case 4:
            return "Excelente!!"
        case _: 
            return "No lo conozco"

print(festejar(3)) """

""" def festejar(opciones):
    match opciones:
        case 1 | 2 | 3:
            return "Mala opcion"
        case 4:
            return "Excelente!" 

print(festejar(4)) """

""" point = (x=0, y=0)

match point:
    case point(x=0, y=0):
        print("Origin")
    case point(x=0, y=y):
        print(f"Y={y}")
    case point(x=x, y=0):
        print(f"X={x}")
    case point():
        print("Somewhere else")
    case _:
        print("Not a point") """

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


