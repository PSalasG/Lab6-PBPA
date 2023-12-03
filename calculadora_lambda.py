def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

# Se eliminaron los ifs ya que el callback ya presenta la operación deseada.
def ejecutar_operacion(user_input, callback):
    num1 = user_input[0]
    num2 = user_input[1]
    result = callback(num1, num2)
    
    print("Resultado:", result, "\n")

def main():
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        # Se creó la lista de operaciones que comprueba si se indicó una operación válida y entrega la función correspondiente.
        operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}

        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.\n")

if __name__ == "__main__":
    main()