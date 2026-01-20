# ejercicio 1 ( funsion para saludar ) 

def saludar (nombre):
    return f"hola {nombre}"

nombre = input ("cual es tu nombre?: ").strip().lower()
print (saludar(nombre))

# ejercicio 2 ( funsion para verificar edad )

def edad (edad):
    if edad >= 18:
        return True
    else: 
        return False

edad = int (input ("cual es tu edad?: ").strip())
print (edad(edad))

# ejercicio 3 ( funcion para calcular operaciones matematicas ) 

def sumar (a,b):
    return a + b

def restar (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def dividir (a,b):
    if b == 0:
        return None
    return a / b

resultados = sumar (5,2), restar (5,2), multiplicar (5,2), dividir (5,2)
print (resultados)  

# ejercicio 4 ( funcion para verificar experiencia del usuario )

def años_de_experiencia (años):
   
    if años >= 3:   
        return "avanzado"
    elif años <= 3 and años >= 2:
        return "intermedio"
    else:
        return "principiante"

años = int (input ("cual es tu experiencia como panadero?: ").strip())
print (años_de_experiencia(años))   