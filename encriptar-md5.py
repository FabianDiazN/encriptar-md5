
import hashlib


class estilo():
    VERDE = '\033[32m'
    AZUL = '\33[34m'
    ROJO = '\33[31m'
    BLANCO = '\33[37m'


print(estilo.VERDE+""" 
+---------------------------------------------------------------------------------------+
| MMMMMMMM               MMMMMMMM     DDDDDDDDDDDDD             555555555555555555      |
| M:::::::M             M:::::::M     D::::::::::::DDD          5::::::::::::::::5      |
| M::::::::M           M::::::::M     D:::::::::::::::DD        5::::::::::::::::5      |
| M:::::::::M         M:::::::::M     DDD:::::DDDDD:::::D       5:::::555555555555      |
| M::::::::::M       M::::::::::M       D:::::D    D:::::D      5:::::5                 |
| M:::::::::::M     M:::::::::::M       D:::::D     D:::::D     5:::::5                 |
| M:::::::M::::M   M::::M:::::::M       D:::::D     D:::::D     5:::::5555555555        |
| M::::::M M::::M M::::M M::::::M       D:::::D     D:::::D     5:::::::::::::::5       |
| M::::::M  M::::M::::M  M::::::M       D:::::D     D:::::D     555555555555:::::5      |
| M::::::M   M:::::::M   M::::::M       D:::::D     D:::::D                 5:::::5     |
| M::::::M    M:::::M    M::::::M       D:::::D     D:::::D                 5:::::5     |
| M::::::M     MMMMM     M::::::M       D:::::D    D:::::D      5555555     5:::::5     |
| M::::::M               M::::::M     DDD:::::DDDDD:::::D       5::::::55555::::::5     |
| M::::::M               M::::::M     D:::::::::::::::DD         55:::::::::::::55      |
| M::::::M               M::::::M     D::::::::::::DDD             55:::::::::55        |
| MMMMMMMM               MMMMMMMM     DDDDDDDDDDDDD                  555555555          |
+---------------------------------------------------------------------------------------+     

""")

palabra = input(estilo.AZUL + "Ingresa una cadena a incriptar en MD5: ")
resultado = hashlib.md5(palabra.encode())
print("")

print(estilo.BLANCO +"El valor de la cadena :"+"|"+palabra+"|"+estilo.BLANCO+" en MD5 es: ", end="")
print(estilo.ROJO+resultado.hexdigest())

print("")



