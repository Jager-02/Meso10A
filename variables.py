#Numero entero
entero = 10
#Numero decimal
decimal = 10.5
#String
nombre = "Juan"
#Booleano
booleano = True
#Lista
lista = [1,2,3,4,5]
#Lista con nombres
listaNombres = ["Juan","Pedro","Maria"]

#Funciones

def suma(a,b):
    resultado = a+b
    return resultado

def resta(a,b):
    resultado = a-b
    return resultado

def multiplicacion(a,b):
    resultado = a*b
    return resultado

# a+b*c-d
a = input("Ingrese el primer numero: ")
b = input("Ingrese el segundo numero: ")
c = input("Ingrese el tercer numero: ")
d = input("Ingrese el cuarto numero: ")

#Conversion de texto a decimal

num1 = float(a)
num2 = float(b)
num3 = float(c)
num4 = float(d)

#Operaciones

resultMult = multiplicacion(num2,num3)
resultSuma = suma(num1,resultMult)
resultResta = resta(resultSuma,num4)

print("El resultado es: ",resultResta)