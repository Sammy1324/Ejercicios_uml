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
    if Excercise_number == 5:
        subprocess.run(["python", "Exc5/main.py"])
    if Excercise_number == 6:
        subprocess.run(["python", "Exc6/main.py"])
    if Excercise_number == 7:
        subprocess.run(["python", "Exc7/main.py"])
    if Excercise_number == 8:
        subprocess.run(["python", "Exc8/main.py"])
    if Excercise_number == 9:
        subprocess.run(["python", "Exc9/main.py"])
    if Excercise_number == 10:
        subprocess.run(["python", "Exc10/main.py"])
    if Excercise_number == 11:
        subprocess.run(["python", "Exc11/main.py"])
    if Excercise_number == 12:
        subprocess.run(["python", "Exc12/main.py"])
    if Excercise_number == 13:
        subprocess.run(["python", "Exc13/main.py"])
    if Excercise_number == 14:
        subprocess.run(["python", "Exc14/main.py"])
    if Excercise_number == 15:
        subprocess.run(["python", "Exc15/main.py"])
    if Excercise_number == 16:
        subprocess.run(["python", "Exc16/main.py"])
    if Excercise_number == 17:
        subprocess.run(["python", "Exc17/main.py"])
    if Excercise_number == 18:
        subprocess.run(["python", "Exc18/main.py"])
    if Excercise_number == 19:
        subprocess.run(["python", "Exc19/main.py"])
    if Excercise_number == 20:
        subprocess.run(["python", "Exc20/main.py"])
    if Excercise_number == 21:  
        subprocess.run(["python", "Exc21/main.py"])
    if Excercise_number == 22:
        subprocess.run(["python", "Exc22/main.py"])
    if Excercise_number == 23:
        subprocess.run(["python", "Exc23/main.py"])
    if Excercise_number == 24:
        subprocess.run(["python", "Exc24/main.py"])
    if Excercise_number == 25:
        subprocess.run(["python", "Exc25/main.py"])
    if Excercise_number == 26:
        subprocess.run(["python", "Exc26/main.py"])
    if Excercise_number == 27:
        subprocess.run(["python", "Exc27/main.py"])
    if Excercise_number == 28:
        subprocess.run(["python", "Exc28/main.py"])
    if Excercise_number == 29:
        subprocess.run(["python", "Exc29/main.py"])


def main():
    while True:
        print("Menu: ")
        print("1. Excercise_1")
        print("2. Excercise_2")
        print("3. Excercise_3")
        print("4. Excercise_4")
        print("5. Excercise_5")
        print("6. Excercise_6")
        print("7. Excercise_7")
        print("8. Excercise_8")
        print("9. Excercise_9")
        print("10. Excercise_10")
        print("11. Excercise_11")
        print("12. Excercise_12")
        print("13. Excercise_13")
        print("14. Excercise_14")
        print("15. Excercise_15")
        print("16. Excercise_16")
        print("17. Excercise_17")
        print("18. Excercise_18")
        print("19. Excercise_19")
        print("20. Excercise_20")
        print("21. Excercise_21")
        print("22. Excercise_22")
        print("23. Excercise_23")
        print("24. Excercise_24")
        print("25. Excercise_25")
        print("26. Excercise_26")
        print("27. Excercise_27")
        print("28. Excercise_28")
        print("29. Excercise_29")
        print("30. Exit")

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
            run_Excercise(5)
        if choice == "6":
            run_Excercise(6)
        if choice == "7":
            run_Excercise(7)
        if choice == "8":
            run_Excercise(8)
        if choice == "9":
            run_Excercise(9)
        if choice == "10":
            run_Excercise(10)
        if choice == "11":
            run_Excercise(11)
        if choice == "12":
            run_Excercise(12)
        if choice == "13":
            run_Excercise(13)
        if choice == "14":
            run_Excercise(14)
        if choice == "15":
            run_Excercise(15)
        if choice == "16":
            run_Excercise(16)
        if choice == "17":
            run_Excercise(17)
        if choice == "18":
            run_Excercise(18)
        if choice == "19":
            run_Excercise(19)
        if choice == "20":
            run_Excercise(20)
        if choice == "21":
            run_Excercise(21)
        if choice == "22":
            run_Excercise(22)
        if choice == "23":
            run_Excercise(23)
        if choice == "24":
            run_Excercise(24)
        if choice == "25":
            run_Excercise(25)
        if choice == "26":
            run_Excercise(26)
        if choice == "27":
            run_Excercise(27)
        if choice == "28":
            run_Excercise(28)
        if choice == "29":
            run_Excercise(29)
        if choice == "30":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()