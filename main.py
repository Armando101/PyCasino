import funciones
from os import system
from getpass import getpass

if __name__ == "__main__":
	print("Bienvenido")
	while True:
		op=input("Seleccione el número de opción\n1)Iniciar Sesión\n2)Crear cuenta\n3)Ver la información de los usuarios\n4)Limpiar consola\n5) Salir del programa ")
		if op=="1":
			nom = input('Ingrese su nombre de usuario ')
			ps = getpass('Ingrese su nombre de password ')
			funciones.iniciarSesion(nom, ps)
		elif op == "2":
			system('clear')
			funciones.crearCuenta()
		elif op == "3":
			system('clear')
			funciones.imprimirDatos()		
		elif op == "4":
			system('clear')
		elif op == "5":
			break
		else:
			print("Opción inválida")
		
		#funciones.listaDeUsuarios[0].getInfo()