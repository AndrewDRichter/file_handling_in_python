import os
from pathlib import Path

def continue_input(func):
    
    def does_it(*args, **kwargs):
        func(*args, **kwargs)
        input("Continuar...")
    
    return does_it

@continue_input
def empty_file(filepath:str="") -> bool:
    print(Path(__file__).parent)

@continue_input
def file_exists():
    try:
        existe = Path(__file__).parent.joinpath("files").exists()
        
    except Exception as e:
        print(e)

@continue_input
def cadastra_usuario():
    try:
        user_name = str(input("Nombre de usuario: "))
        user_password = str(input("Contraseña de usuario: "))

        with open("datos.txt", "r") as f:
            empty = len(f.read()) == 0
            f.close()
        
        if empty:
            print("vazio")

        with open(str(Path(__file__).parent) + r"\files\datos.txt", "w") as f:
            f.write(user_name)
            f.write(", ")
            f.write(user_password)
            f.close()
        
        # input("Continuar...")
    except Exception as e:
        print(f"Exception: {e}")
        # input("Continuar")

@continue_input
def visualiza_usuarios():
    try:
        with open("datos.txt", "r") as f:
            print(len(f.read()))
            # input("Continuar...")
    except Exception as e:
        print(e)

def menu():
    os.system("cls")
    print('''
          1- Cadastrar
          2- Visualizar
            ''')
    return input("O quê deseja fazer: ")
    
while True:
    r = menu()
    # empty_file()
    file_exists()
    match r:
        case '1':
            cadastra_usuario()
        case '2':
            visualiza_usuarios()
        case _:
            print("Não existe essa opção!")
            input("Continuar...")