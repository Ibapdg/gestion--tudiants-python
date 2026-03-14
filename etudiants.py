etudiant = [ ]
while True: 
    print("\n1. Ajouter un étudiant")
    print("2. Afficher les étudiants")
    print("3. Quitter")
    choix = input("Entrez votre choix: ")
    if choix == "1":
        nom = input("Entrez le nom de l'étudiant: ")
        prenom = input("Entrez le prénom de l'étudiant: ")
        etudiant.append((nom, prenom))
    elif choix == "2":
        print("\nListe des étudiants:")
        for i, (nom, prenom) in enumerate(etudiant, start=1):
            print(f"{i}. {nom} {prenom}")
    elif choix == "3":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")