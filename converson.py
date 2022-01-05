#pesos = input("¿Cuantos pesos colombianos tienes?:  ")
#pesos = float(pesos)
#valor_dolar = 3875
#dolares = pesos / valor_dolar
#dolares = round(dolares, 2)
#dolares = str(dolares)
#print("Tienes $" + dolares + " dolares")

#Programa si es mayor de edad 
#edad = input("¿Cuantos años tienes?: ")
#edad = int(edad)
#if edad > 18 and edad <29 :
#    print("Genial... haz cagado tu vida, eres adulto")
#elif edad == 29:
#    print("Comienza la chaborruques :O XD")
#elif edad == 17:
#    print("Ya casi eres adulto...")
#elif edad < 17:
#    print(":) Aun eres un niño")
#else:
#    print("Cada dia eres mas grande")

#Conversion por paises
#moneda = input("Si pesos mexicanos=1, pesos argentinos=2 y pesos colombianos = 3; ¿que moneda quieres covertir a dolares?: ")
#moneda = float(moneda)
#mxn = 1
#arg = 2
#col = 3
#if moneda == mxn: 
#    dolares = input("¿Cuantos pesos mexicanos tienes?: ")
#    valor_dolares = 20
#elif moneda == arg: 
#    dolares = input("¿Cuantos pesos argentinos tienes?: ")
#    valor_dolares = 300
#elif moneda == col: 
#    dolares = input("¿Cuantos pesos colombianos tienes?: ")
#    valor_dolares = 2000
#else:
#    dolares = moneda
#    valor_dolares = 0
#    print("No tenemos la conversion de dolares a esa moneda :P")
#
#if valor_dolares > 0:    
#    dolares = float(dolares)
#    conversion = str(dolares / valor_dolares)
#    print("La conversion es de $" + conversion + " dolares")



#COMO FUNCIONAN LAS FUNCIONES

#def imprimir_mensaje():
#    print("Mensaje especial: ")
#    print("¡Estoy aprendiendo a usar funciones!")
#
#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

#def conversacion(mensaje):
#    print("hola")
#    print("¿Como estas?")
#    print(mensaje)
#    print("Adios")
#
#opcion = int(input("Elige una opcion (1, 2 o 3): "))
#if opcion == 1:
#    conversacion("Elegiste la opcion 1")
#elif opcion == 2:
#    conversacion("Elegiste la opcion 2")
#elif opcion == 3:
#    conversacion("Elegiste la opcion 3")
#else:
#    print("Escribe la opcion correcta")




#Modularizando conversor de monedas
#   EJEMPLO
#def suma(a, b):
#    print("Se suman dos nùmeros")
#    resultado = a + b
#    return resultado
#
#sumatoria = suma(1, 4)
#print(sumatoria)


#def conversion(tipo_moneda, valor_dolar):
#    pesos = float(input("¿Cuantos pesos " + tipo_moneda + " tienes?: "))
#    dolares = pesos / valor_dolar
#    dolares = round(dolares, 2)
#    dolares = str(dolares)
#    print("Tienes $" + dolares + " dolares")
#
#menu = """ 
#    Bienvenido al conversor de monedas, ingresa el numero de una opcion
#
#        1.- Pesos mexicanos
#        2.- Pesos argentinos
#        3.- Pesos colombianos
#    
#    Ingresa el numero: """
#
#opcion = int(input(menu))
#
#if opcion == 1: 
#    conversion("mexicanos", 20)
#elif opcion == 2:
#    conversion("argentinos", 6358)
#elif opcion == 3:
#    conversion("colombianos", 656)
#else:
#    opcion_erronea = """ 
#    Esa opcion no la tenemos :P
#    """
#    print(opcion_erronea)


def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): 
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Enter point - punto de entrada de un programa de python 
    #Cuando python se encuentra ocn esto comenza a correr todo lo que hay debajo

if __name__ == '__main__':
    run()




