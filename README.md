# PyCasino  


El proyecto consiste en diseñar una interfaz que simulará
un casino.
Los jugadores van a necesitar crear una cuenta para
poder acceder, cuando inicie el programa, los jugadores
van a poder escoger una de dos opciones, crear una
cuenta o usar una existente. Para crear una cuenta, el
usuario va a necesitar ingresar nombre, contraseña y
edad. Estos datos van a ser almacenados en una lista de
listas, donde cada lista va a tener los datos de cada
usuario creado. Si el usuario tiene menos de 18 años, la

cuenta no se va a crear y va a mandar un mensaje diciendo
que el usuario debe ser mayor de edad. Si se escoge usar
una cuenta ya existente. Se va a buscar esta información
en la lista donde se están guardando los datos de los
usuarios y si se encuentra un usuario que tenga ese
nombre y esa contraseña, se va a poder ingresar al casino
con éxito, en caso contrario, se desplegará un mensaje
indicando que no se reconoció ese nombre o esa
contraseña. En la lista donde se están almacenando las
listas de cada usuario, se va a necesitar almacenar los
nombres de los usuarios, sus contraseñas y la cantidad de
fichas que posean. Por default, cuando se crea un nuevo
usuario, este iniciará con 100 fichas.
Una vez ingresado con éxito, los usuarios podrán escoger
entre:
● Juego 1  
● Juego 2  
● Consultar fichas  
● Comprar fichas  
● Salir  
Van a tener que diseñar dos juegos de casino y estos se
van a poder jugar, modificando las fichas del usuario
conforme sea necesario.
Una vez que se desea salir, se deberá actualizar los datos
de la lista de usuarios. Modificando la cantidad de fichas a
la cantidad que tiene el usuario al momento de salir.
