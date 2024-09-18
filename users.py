from file_handling import create_file, clear_terminal, testando


def continue_input(func):
    def does_it(*args, **kwargs):
        input(f"Seguir para: {func.__name__.capitalize()}")
        return func(*args, **kwargs)
    return does_it


# TODO: A lot to do.
def create_user():
    try:
        user_name = str(input("User's name: "))
        user_password = str(input("User's password: "))
        confirm_user_password = str(input("Confirm User's password: "))

        if confirm_user_password != user_password:
            print("Password and confirmation do not match!")

        # Below this comment: Call a function to handle user creation.


        # TODO: create_user should only handle user creation (cannot handle files or anything else)

        # with open("datos.txt", "r") as f:
        #     empty = len(f.read()) == 0
        #     f.close()
        
        # if empty:
        #     print("vazio")

        # with open(str(Path(__file__).parent) + r"\files\datos.txt", "w") as f:
        #     f.write(user_name)
        #     f.write(", ")
        #     f.write(user_password)
        #     f.close()
    
    except Exception as e:
        print(f"Exception: {e}")

def read_users():
    try:
        # TODO: In the future, change file system to database system
        with open("data.txt", "r") as f:
            print(len(f.read()))
            # input("Continuar...")
    except Exception as e:
        print(e)

@continue_input
def menu():
    clear_terminal()
    print('''
          1- Cadastrar
          2- Visualizar
            ''')
    return input("O quê deseja fazer: ")
    
while True:
    # r = str(menu())
    testando()
    # match r:
    #     case '1':
    #         create_user()
    #     case '2':
    #         read_users()
    #     case _:
    #         print("Não existe essa opção!")
    #         input("Continuar...")