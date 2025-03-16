import os
import subprocess

def run_Excercise(Excercise_number):
    if Excercise_number == 1:
        subprocess.run(["python", "Exc1/main.py"])
    if Excercise_number == 2:
        subprocess.run(["python", "Exc2/main.py"])
    if Excercise_number == 3:
        subprocess.run(["python", "Exc3/main.py"])
    if Excercise_number == 4:
        subprocess.run(["python", "Exc4/main.py"])


def main():
    while True:
        print("Menu: ")
        print("1. Excercise_1")
        print("2. Excercise_2")
        print("3. Excercise_3")
        print("4. Excercise_4")
        print("5. Exit")

        choice = input("Seleccione ejercicio a ejecutar: ")
        if choice == "1":
            run_Excercise(1)
        if choice == "2":
            run_Excercise(2)
        if choice == "3":
            run_Excercise(3)
        if choice == "4":
            run_Excercise(4)
        if choice == "5":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()