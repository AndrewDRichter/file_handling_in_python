import os
from pathlib import Path

def clear_terminal():
    os.system("cls")

def file_is_empty(filepath) -> bool:
    with open(filepath, "r") as file:
        return False if len(file.read()) > 0 else True

def file_exists(path):
    return Path(__file__).parent.joinpath("files").exists()

def handle_exceptions(func):
    def exception_handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error handler: {e}")
    return exception_handler

# criação de arquivo
@handle_exceptions
def create_file(path):
    # try:
    #     os.mkdir(path)
    #     print(f"Created directory at >> {path}")
    # except Exception as e:
    #     print(f"CREATE_FILE Error: {e}")
    os.mkdir(path)
    print(f"Created directory at >> {path}")


# leitura de arquivo
@handle_exceptions
def read_file(path):
    with open(path, "r") as file:
        print(file.read())
        file.close()


# escrita e sobrescrita de arquivo
@handle_exceptions
def write_file(path, message, override: bool = False):
    # eval('with open(path, "w") as file: file.write("banana")') if override else eval('with open(path, "a") as file: file.append("abacaxi")')
    if override:
        mode = "w"
    else:
        mode = "a"
    with open(path, mode) as file:
        file.write(message)
        file.close()

def testando():
    file_path = Path(__file__).parent.joinpath(r"files\data.txt")
    create_file(Path(__file__).parent.joinpath(r"files\data\blabla.txt"))
    input()
    empty = True if file_is_empty(file_path) else False
    write_file(file_path, "olá", True)

if __name__ == "__main__":
    testando()