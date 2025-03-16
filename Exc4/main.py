from Catedral import Catedral

def main():
    catedral_Santiago = Catedral(
        name="Catedral de Santiago de Compostela",
        city="Santiago de Compostela",
        community="Galicia",
        construction_beginning_year=1075,
        construction_material="Piedra",
        consecration_official_date="21 de abril de 1211")
    
    petition = input("¿Qué información de la catedral desea conocer? ")

    if petition.lower() == "name":
        print(catedral_Santiago.name)
    elif petition.lower() == "city":
        print(catedral_Santiago.city)
    elif petition.lower() == "community":
        print(catedral_Santiago.community)
    elif petition.lower() == "construction beginning year":
        print(catedral_Santiago.construction_beginning_year)
    elif petition.lower() == "construction material":
        print(catedral_Santiago.construction_material)
    elif petition.lower() == "consecration official date":
        print(catedral_Santiago.consecration_official_date)
    else:
        print("Petición no válida")

if __name__ == "__main__":
    main()