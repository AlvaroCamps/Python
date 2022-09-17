#Opcion de ejercicio Lab04 Tar1

from secrets import choice

"""def ingreso_lado():
	lado = float (input ("Ingresa el tamaño del lado:\t"))
	return lado	"""

def e1():
	print("*********************************")
	print("************  ROMBO *************")
	print("*******Con 4 lados iguales*******")
	print("*********************************")

	lado = float (input ("Ingresa el tamaño del lado:\t"))
	diagmay = float (input ("Ingrese la diagonal mayor:\t"))
	diagmen = float (input ("Ingrese la diagonal menor:\t"))

	def area_rombo(diagmay, diagmen):
		area = (1/2)*diagmay*diagmen
		return area
	def perimetro_rombo(l):
		perimetro=4*l
		return perimetro

	print("\nEl perimetro es:\t\t",perimetro_rombo(lado),
		"\nEl area es:\t\t\t", area_rombo(diagmay, diagmen))

def e2():
	print("*********************************")
	print("************ HEXÁGONO ***********")
	print("************ Regular ************")
	print("*********************************")
	lado = float (input ("Ingresa el tamaño del lado:\t"))

	def area_hexa(l):
		#area = (3/2)*(l**2)*pow(3)
		#https://appgametutoriales.com/raiz-cuadrada-en-python-sqrt-python/
		area = (3/2)*(l**2)*(3**0.5)
		return area
	def perimetro_hexa(l):
		perimetro=6*l
		return perimetro

	print("\nEl perimetro es:\t\t",perimetro_hexa(lado),
		"\nEl area es:\t\t\t", area_hexa(lado))
	
	respuesta_continuar = input("¿Desea volver al menu principal?: ")

	while respuesta_continuar != "S" and respuesta_continuar != "s":
		respuesta_continuar = main()

#Menu
def mostrar_menu(opciones):
	print("\nDigita el numero de ejercicio a tener: ")
	for clave in sorted(opciones):
		print(f'{clave}) {opciones[clave][0]}')

#Genera menu
def generar_opciones(opcion, opcion_salida):
	opcion = None
	while opcion != opcion_salida:


#Operacion
#Menu principal
def menu_principal():
	print ("**********************************")
	print ("***** EJERCICIOS Lab04 Tar1 ******")
	print ("**********************************")
	opciones = {
		'1': ('1. Ejercicio 1: Perimetro y area de un rombo', e1),
		'2': ('2. Ejercicio 2: Perimetro y area de un hexagono', e2),
		'3': ('3',salir)
	}

	generar_opciones( opciones, '3')

def main():
	choice = input("\nDigita el numero de ejercicio a tener: ...(1/2)")

	if choice == '1':
		e1()
	if choice == '2':
		e2()
	else:
		print("Diga NO PARA CONTINUAR")
		respuesta = input("")

if __name__ == "__main__":
	main()