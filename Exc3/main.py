from Replica import Replica

def main():
    la_gioconda_replica = Replica(
        title="La Gioconda Replica",
        author="Anonimo",
        chronological_ascription="1503 — 1516",
        technique="Oleo",
        sub_technique="Pincelada simple",
        support_material="Madera de nogal",
        description=("Existen muchas réplicas o copias de La Gioconda expuesta en el Museo Louvre de París, aunque ésta, que se encontraba en el Museo del Prado (Madrid) desde su inauguración, procedente de las Colecciones Reales, es la más antigua que se conoce. La conclusión del estudio efectuado en el Prado es que la réplica de Madrid fue realizada por un alumno de la escuela de Leonardo al mismo tiempo que el artista italiano pintaba su obra maestra. Por ello, las hipótesis sobre su autoría se ciñeron al círculo de discípulos que trabajaron con Leonardo. Su estado de conservación es mucho mejor que el de la obra original."),
        original_author="Leonardo Da Vinci",
        original_technique="Oleo",
        original_sub_technique="Sfumato",
        original_support_material="Madera de álamo",
        original_location="Museo Louvre, París")

    petition = input("¿Qué información de la obra desea conocer? ")

    if petition.lower() == "title":
        print(la_gioconda_replica.title)
    elif petition.lower() == "author":
        print(la_gioconda_replica.author)
    elif petition.lower() == "chronological ascription":
        print(la_gioconda_replica.chronological_ascription)
    elif petition.lower() == "technique":
        print(la_gioconda_replica.technique)
    elif petition.lower() == "sub technique":
        print(la_gioconda_replica.sub_technique)
    elif petition.lower() == "support material":
        print(la_gioconda_replica.support_material)
    elif petition.lower() == "description":
        print(la_gioconda_replica.description)
    elif petition.lower() == "original author":
        print(la_gioconda_replica.original_author)
    elif petition.lower() == "original technique":
        print(la_gioconda_replica.original_technique)
    elif petition.lower() == "original sub technique":
        print(la_gioconda_replica.original_sub_technique)
    elif petition.lower() == "original support material":
        print(la_gioconda_replica.original_support_material)
    elif petition.lower() == "original location":
        print(la_gioconda_replica.original_location)
    else:
        print("Petición no válida")
    

if __name__ == "__main__":
    main()