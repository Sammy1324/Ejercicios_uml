import os
import subprocess

def run_excercise(excercise_number):
    if excercise_number == 1:
        subprocess.run(['python', 'excercise1.py'])


def main():
    while True:
        print("Menu: ")
        print("1. Excercise 1")
        print("2. Exit")

        choice = int(input("Opciones: "))
        if choice == 1:
            run_excercise(1)
        if choice == 2:
            break
        else:
            print("Opción no válida")

if __name__ == '__main__':
    main()