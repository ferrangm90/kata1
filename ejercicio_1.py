#realizar un programa muestre segun la opcion +(suma), -(resta), *(Multiplicacion), /(Division)
#de dos numeros ingresados nos pedira ingrese el primer numero, ingrese el segundo,
#ingrese la operacion, el programa debe para solo si al final de la operacion escribo la palabra salir,
#usar funciones

def calculadora(num1:float,num2:float,operacion:str)->float:

    if operacion == "+":
        print(f"El resultado de la suma es: {num1 + num2}")
    elif operacion == "-":
        print(f"El resultado de la resta es: {num1 - num2}")
    elif operacion == "*":
        print(f"El resultado de la multiplicación es: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"El resultado de la división es: {num1 / num2}")
        else:
            print("Error: División por cero.")
            return None
    else:
        print("Operación no válida.")
        return None
continuar = True
while continuar:

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    operacion = input("Ingrese la operacion (+, -, *, /): ")
    calculadora(num1, num2, operacion)

    seguir = input("Desea realizar otra operacion? (s/n): ")
    if seguir.lower() == "n":
        continuar = False


