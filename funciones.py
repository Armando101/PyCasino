import usuario
from getpass import getpass
from os import system

listaDeUsuarios=[]

def crearCuenta():
	nombre = input("Ingrese el nombre de usuario ")
	edad = int(input("Ingrese su edad "))
	password1 = getpass("Ingrese su nuevo password ")
	password2 = getpass("Ingrese su password una vez mas ")
	
	if password1==password2 and edad>=17:
		nuevo = usuario.Usuario(nombre, password1, edad)
		listaDeUsuarios.append(nuevo)
		print("Su cuenta ha sido creada con éxito")
		system('clear')
	else:
		if edad<18:
			print("Su edad es menor a 18 años por lo que no es posible hacer crear una cuenta")
		else:
			print("Sus contraseñas no coinciden o ")

def iniciarSesion(nom, pas):
	system('clear')
	for i in listaDeUsuarios:
		if i.getNombre() == nom and i.getPasword() == pas:
			print('Bienvenido, ha iniciado sesion correctamente')
			i.Cuenta()
			return 
	print('Su nombre de usuario o password son incorrectos')
			

def imprimirDatos():
	if len(listaDeUsuarios) == 0:
		print('No hay cuentas registradas')
		return
	for i in listaDeUsuarios:
		i.getInfo()
