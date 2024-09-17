import os


def cadastra_usuario():
    try:
        user_name = str(input("Nombre de usuario: "))
        user_password = str(input("Contraseña de usuario: "))

        with open("datos.txt", "r") as f:
            empty = len(f.read()) == 0
            f.close()
        
        if empty:
            print("vazio")

        with open("datos.txt", "w") as f:
            f.write(user_name)
            f.write(", ")
            f.write(user_password)
            f.close()
        
        input("Continuar...")
    except Exception as e:
        print(f"Exception: {e}")
        input("Continuar")

def visualiza_usuarios():
    with open("datos.txt", "r") as f:
        print(len(f.read()))
        input("Continuar...")

def menu():
    os.system("cls")
    print('''
          1- Cadastrar
          2- Visualizar
            ''')
    return input("O quê deseja fazer: ")
    
while True:
    r = menu()
    match r:
        case '1':
            cadastra_usuario()
        case '2':
            visualiza_usuarios()
        case _:
            print("Não existe essa opção!")