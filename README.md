# Practica 1
Hola
# CÓDIGO MÁQUINA DE MALTEADAS

El programa presentado es un código para una máquina de malteadas, la cual nos ofrece un menú de bienvenida,
un historial de compras y la opción de salir del menú como se mostrará más adelante.

## Main

Esta será script principal del programa, de aquí llamaremos a los demás modulos. La sintáxis para 
coordinar los demás módulos en main es la siguiente:

```python
from menu import menu_malteadas
from malteadas import pedido_malteadas
from historial import ver_historial
```

De igual forma se creó una función llamada *malteadas*, la cual lleva dentro un bucle *while* que nos
permite repetir el programa hasta que el usuario determine cuando lo quiere terminar, así mismo dentro del
*while* tendremos un *if* el cual nos permitirá acceder a los demás módulos del programa dependiendo la
opción seleccionada del usuario.

```python
def malteadas():
    while True:
        menu_malteadas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pedido_malteadas()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Gracias por su preferencia, vuelva pronto.")
            break
        else:
            print("Opción no válida, intente con alguna de las opciones propuestas.")
```
De igual forma como se puede observar en el código mostrado se está usando la función *imput* la cual nos
permite que el usuario elija qué opción del menú principal es la que va a usar.

Así mismo se puede observar un *break* el cual en este caso al seleccionar la opción 3 hará que nuestro
bucle *while* sea interrumpido y asi se termine el programa.

Por último, en la parte del *else* mandamos a pantalla un menaje de error por cualquier dato ingresado 
por el usuario ajeno a las opciones que le estamos proporcionando y regresando al bucle, de esta manera 
hacemos que el usuario solo elija las opciones proporcionadas.

## Menu

En este módulo crearemos una función del menú principal del programa, con *print* en este caso solo 
mandaremos a pantalla la lista del menú para que el usuario escoja entre una de ellas. 

```python
def menu_malteadas():
    print("\n Bienvenido a las Malteadas")
    print("1. Mostrar menú")
    print("2. Historial de compras")
    print("3. Salir")

```

## Malteadas

En este módulo mostraremos la variedad de malteadas a elegir, de igual forma lo haremos creando una función
la cual nos ayudará a estructurar de una mejor manera el código, ya que tendremos que poner condicionales
para la selección de los productos a mostrar. De la misma for que en *main* le pediremos al usuario mediante
la función *input* que tipo de malteada es la que va a pedir.

```python
def pedido_malteadas():
    print("\n Elija la malteada de su preferencia")
    print("1. Malteada de chocolate")
    print("2. Malteada de vainilla")
    print("3. Malteada de fresa")
    print("4. Malteada de galleta")

    opcion = input("Elija una opción: ")
```

De igual forma se añadió un *diccionario* en el cual están almacenadas todas las malteadas que se tienen
en existencia. Este mismo nos ayuda para:
1. Mandar a pantalla un mensaje con la selección de la malteada y diciendo que se está preparando.
2. Para la parte del historial de los pedidos, la información de las malteadas la obtendremos de ahí.

```python
malteadas = {
        "1" : "Chocolate",
        "2" : "Vainilla",
        "3" : "Fresa",
        "4" : "Galleta"
    }
```

En este módulo se integró la función *with open* dentro de una función *if*, la cual nos permitirá
dos cosas:
1. Mandar el mensaje a pantalla de la malteada elegida.
2. Usar *with open* para la creación de un archivo *.txt* en el cual se irán guardando los pedidos realizados

De igual forma se declaró una constante que nos ayudará a no estar repitiendo el nombre del archivo donde
queremos guardar los pedidos.
>*Nota: Se declara en mayúsculas porque es una constante y es parte de las buenas pŕacticas*
```python
ARCHIVO_PEDIDO = "pedidos.txt"

    if opcion in malteadas:
        malteada_elegida = malteadas[opcion]
        print("Ha elegido una malteada de " + malteada_elegida + ", su malteada esta siendo preparada")
        with open(ARCHIVO_PEDIDO, "a", encoding="utf-8") as archivo:
            archivo.write(malteada_elegida + "\n")
    else:
        print("Opción no válida, seleccione otra opción.")
```
>*En la parte del with tenemos una "a" la cual cuando se lee el código lo que hace es que va a escribir
sobre la útlima linea que tenga el archivo que se está creando.*
## Historial

Por último en el módulo del historial de igual forma usaremos una función para encapsular un *try y except*
con esto podemos "atrapar" errores que puedan surgir en la creación del archivo *.txt* o al momento de 
leer los pedidos realizados.

```python
ARCHIVO_PEDIDO = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de Pedidos")
        with open(ARCHIVO_PEDIDO, "r", encoding="utf-8") as archivo:
            malteadas = archivo.readlines()
            if malteadas:
                for i, pedido in enumerate(malteadas, start=1):
                    print(str(i) + ". " + pedido.strip())
            else:
                print("Aún no hay ningún pedido")
    except FileNotFoundError:
        print("No hay pedidos existentes")
```

> Como se puede observar se volvió a usar la constante *ARCHIVO_PEDIDO,* ya que es donde se van a almacenar
los pedidos hechos.

Lo que está dentro del *try* se tratará de hacer y en dado caso que no se realice el programa saldrá
por el *except* mandándonos en este caso un mensaje que dice *"No hay pedidos existentes"* en lugar de 
mandar el erro *FileNotFoundError*.

Como se puede observar en la parte del *with* después de la constante tenemos una *"r"* lo que nos da a
entender que lo que hará el programa es solo leer el archivo siempre y cuando exista uno
