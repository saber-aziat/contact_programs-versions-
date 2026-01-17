# la class contact
class Contact:

    #constructeur 
    def __init__(self , nom , prenom , email , numeroTel):
        # verfifcation de type
        assert isinstance(nom , str) and nom != "" , "Le nom doit etre une chaine de caractere non vide"
        assert isinstance(prenom , str) , "Le prenom doit etre une chaine de caractere non vide"
        assert isinstance(email , str) and "@" in email , "L'email doit etre une chaine de caractere valide"
        assert isinstance(numeroTel , str) and numeroTel.isdigit() and len(numeroTel) == 10 and (numeroTel.startswith("05") or numeroTel.startswith("06") or numeroTel.startswith("07")) , "Le numero de telephone non  valide"

        # initialisation des attributs
        self.nom = nom.lower()
        self.prenom = prenom.lower()
        self.email = email
        self.numeroTel = numeroTel
        
# class AdressBook qui herite class contact
class AdressBook(Contact):
    # constructeur 
    def __init__(self, nom, prenom, email, numeroTel):
        super().__init__(nom, prenom, email, numeroTel)

    # la methode addcontact
    def AddContact(self):
        with open("contact.txt", "a+") as fichier:
            fichier.seek(0)
            lignes = fichier.readlines()

            for ligne in lignes:
                if self.nom in ligne and self.prenom in ligne and self.email in ligne:
                    print(f"{self.nom} {self.prenom} existe deja dans le carnet")
                    return

            fichier.write(f"{self.nom} | {self.prenom} | {self.email} | {self.numeroTel}\n")
            print(f"{self.nom} {self.prenom} ajoute avec succes")    

    # la methode RemouveContact
    def RemouveContact(self , nom_sup , prenom_sup):
        nom_sup = nom_sup.lower()
        prenom_sup = prenom_sup.lower()
        exist = False
        nouvel_data = []

        with open("contact.txt" , 'a+') as fichier:
            fichier.seek(0)
            lignes = fichier.readlines()

            for ligne in lignes:
                if nom_sup in ligne and prenom_sup in ligne :
                    exist = True
                else:
                    nouvel_data.append(ligne)

            if exist :
                nouvel_contenu_dans_fichier = open("contact.txt" , "w")
                nouvel_contenu_dans_fichier.writelines(nouvel_data)
                nouvel_contenu_dans_fichier.close()
                print(f"Le contact {nom_sup} {prenom_sup} a ete supprime avec succes")
            else:
                print(f"Le contact {nom_sup} {prenom_sup} n'existe pas dans le carnet")

    # la methode desplay 
    def desplayData(self):
        with open("contact.txt","r") as fichier:
            fichier.seek(0)
            lignes = fichier.readlines()

            if lignes == []:
                print("Le carnet d'adresse est vide")
            else:
                print("Les contacts dans le carnet d'adresse sont :")
                for ligne in lignes:
                    print(f"NOM : {ligne.split('|')[0].strip()} , PRENOM : {ligne.split('|')[1].strip()} , EMAIL : {ligne.split('|')[2].strip()} , NUMERO DE TELEPHONE : {ligne.split('|')[3].strip()}")

# la description de programme 
print("---------------------------- BIENVENU SUR TON CONTACT ---------------------------- ")
choix = 0

while choix != 4 :
    print("\n========   MENU   ========")
    print("1 : Add Contact \n2 : Remouve Contact \n3 : Afficher Contact \n4 : Quitter")
    choix = input(" - Ton Choix : ")

    while isinstance(choix , str) and int(choix) not in [1,2,3,4]:
        choix = input(" - Ton choix : ")

    else:
      match int(choix):
        
        case 1 :
            nom = input(" - Saisir le nom du contact : ")
            prenom = input(" - Saisir le prenom du contact : ")
            email = input(" - Saisir l'email du contact : ")
            numeroTel = input(" - Saisir le numero de telephone du contact : ")

            while not (isinstance(nom , str) and nom != "" and 
                       isinstance(prenom , str) and prenom != "" and 
                       isinstance(email , str) and "@" in email and 
                       isinstance(numeroTel , str) and numeroTel.isdigit() and len(numeroTel) == 10 and (numeroTel.startswith("05") or numeroTel.startswith("06") or numeroTel.startswith("07"))):
                nom = input(" - Saisir le nom du contact : ")
                prenom = input(" - Saisir le prenom du contact : ")
                email = input(" - Saisir l'email du contact : ")
                numeroTel = input(" - Saisir le numero de telephone du contact : ")

            contact = AdressBook(nom , prenom , email , numeroTel)
            contact.AddContact()
            
        case 2 :
            contact = AdressBook("user" , "user" , "user@gmail.com" , "0712345671")
            NomASuprimer = str(input(" - Saisir le nom du contact a supprimer : "))
            PrenomASuprimer = str(input(" - Saisir le prenom du contact a supprimer : "))

            contact.RemouveContact(NomASuprimer , PrenomASuprimer)

        case 3 : 
            contact = AdressBook("user" , "user" , "user@gmail.com" , "0712345671")
            contact.desplayData()
            
        case 4 : 
              print(" - A bientot ! ")
              break        



    


