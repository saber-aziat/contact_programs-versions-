import tkinter as tk
from tkinter import messagebox

# ========================== Fenetre principale ==========================
window = tk.Tk()
window.title("CONTACT's PROGRAMME")
window.geometry("600x700")
window.configure(bg="#F0F4F8")
nom_utilisateur = "" 

# ========================== LES FONCTIONNALITE  ==========================
def navigation(page):
    page.tkraise()  

def remove():
    window.destroy()

def create_menu_button(parent):
    return tk.Button(
        parent,
        text="BACK TO MENU",
        fg="white",
        bg="#ED3629",
        font=("Comic Sans MS", 14, "bold"),
        activebackground="#684D12",
        activeforeground="white",
        relief="raised",
        command=lambda: navigation(menu)
    )

def delete_all_contact():
    print("delete all contact")
    response = messagebox.askyesno(
            "Verificaton",
            "Are you sure !!!!\n\nyou want to remove all your contact?"
        )

    if response:
        with open("C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact.txt", "w") as fichier:
            fichier.write("")  
        messagebox.showinfo("Success", "All contacts have been deleted successfully!")
        navigation(menu)
    else:
            navigation(menu)
# ========================== PAGE MENU ==========================
menu = tk.Frame(window, bg="#F0F4F8")
menu.place(x=0, y=0, relwidth=1, relheight=1)




menu_label = tk.Label(
    menu,
    text="", 
    font=("Comic Sans MS", 24, "bold"),
    fg="#2E86AB",
    bg="#F0F4F8",
    wraplength=500,
    justify="center"
)
menu_label.pack(pady=(30, 20))

menu_btn1 = tk.Button(
    menu,
    text="ADD PERSON TO CONTACTS",
    fg="white",
    bg="#2E86AB",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#1B4F72",
    activeforeground="white",
    relief="raised",
    command=lambda: navigation(add_contact)
).pack(pady=(10, 10), ipadx=20, ipady=10)

menu_btn2 = tk.Button(
    menu,
    text="REMOVE PERSON TO CONTACTS",
    fg="white",
    bg="#2E86AB",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#1B4F72",
    activeforeground="white",
    relief="raised",
    command=lambda: navigation(remove_contact)
).pack(pady=(10, 10), ipadx=20, ipady=10)

menu_btn3 = tk.Button(
    menu,
    text="DISPLAY CONTACT",
    fg="white",
    bg="#2E86AB",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#1B4F72",
    activeforeground="white",
    relief="raised",
    command=lambda: navigation(display_contact)
).pack(pady=(10, 10), ipadx=20, ipady=10)

menu_btn4 = tk.Button(
    menu,
    text="DELETE ALL CONTACT",
    fg="white",
    bg="#2E86AB",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#1B4F72",
    activeforeground="white",
    relief="raised",
    command= delete_all_contact
).pack(pady=(10, 10), ipadx=20, ipady=10)

menu_btn5 = tk.Button(
    menu,
    text="EXIT",
    fg="white",
    bg="#ED3629",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#684D12",
    activeforeground="white",
    relief="raised",
    command=lambda: remove()
).pack(pady=(10, 10), ipadx=20, ipady=10)

# ========================== PAGE PRINCIPALE ==========================
principale = tk.Frame(window, bg="#F0F4F8")
principale.place(x=0, y=0, relwidth=1, relheight=1)

principale_label = tk.Label(
    principale,
    text="WELCOME TO YOUR CONTACT'S PROGRAMME",
    font=("Comic Sans MS", 26, "bold"),
    fg="#2E86AB",
    bg="#F0F4F8",
    wraplength=500,
    justify="center"
)
principale_label.pack(pady=(30, 20))
principale_photo = tk.PhotoImage(file="C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\Projet T-kinder + fichier v1.2.0\\photos\\unnamed.png")

principale_image_label = tk.Label(principale, image=principale_photo, bg="#F0F4F8")
principale_image_label.pack(pady=(10, 20))

# Champ pour le nom
name_utilisateur = tk.Entry(
    principale,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
name_utilisateur.pack(pady=(0, 15), ipadx=50, ipady=5) 

# Fonction bouton NEXT
def verifier_et_naviguer():
    global nom_utilisateur
    nom = name_utilisateur.get().strip()
    if nom == "":
        print("Veuillez entrer votre nom !")
    else:
        nom_utilisateur = nom 
        menu_label.config(text=f"Hello {nom_utilisateur}, welcome to the menu!")
        navigation(menu) 

# Bouton NEXT
btn_principale = tk.Button(
    principale,
    text="NEXT",
    fg="white",
    bg="#2E86AB",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#1B4F72",
    activeforeground="white",
    relief="raised",
    command=verifier_et_naviguer
)
btn_principale.pack(pady=(0, 20), ipadx=20, ipady=10)


# ========================== PAGE ADD CONTACT ============================
add_contact = tk.Frame(window, bg="#F0F4F8")
add_contact.place(x=0, y=0, relwidth=1, relheight=1)

add_contact_label = tk.Label(
    add_contact,
    text="\"ADD CONTACT\"",
    font=("Comic Sans MS", 26, "bold"),
    fg="#2E86AB",
    bg="#F0F4F8",
    wraplength=500,
    justify="center"

)
add_contact_label.pack(pady=(30, 20))

# Label de prenom
label_first_name = tk.Label(
    add_contact,
    text="First Name of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)


# Entry de prenom
add_contact_first_name_person = tk.Entry(
    add_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
add_contact_first_name_person.pack(pady=(10, 10), ipadx=20, ipady=10)

# Label de nom
label_last_name = tk.Label(
    add_contact,
    text="Last Name of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)

# Entry de nom
add_contact_last_name_person = tk.Entry(
    add_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
add_contact_last_name_person.pack(pady=(10, 10), ipadx=20, ipady=10)
# Label de mail
label_mail = tk.Label(
    add_contact,
    text="Email of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)


# Entry de mail
add_contact_mail = tk.Entry(
    add_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
add_contact_mail.pack(pady=(10, 10), ipadx=20, ipady=10)

# Label de numero
label_numero = tk.Label(
    add_contact,
    text="Num of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)


# Entry de numero
add_contact_numero = tk.Entry(
    add_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
add_contact_numero.pack(pady=(10, 10), ipadx=20, ipady=10)

# fonction de save_contact

def save_contact():

    # Verifier le prenom
    if not add_contact_first_name_person.get().strip().isalpha():
        messagebox.showerror("Error", "Please enter a valid first name")
        return

    # Verifier le nom
    if not add_contact_last_name_person.get().strip().isalpha():
        messagebox.showerror("Error", "Please enter a valid last name")
        return

    # Verifier l email
    email = add_contact_mail.get()
    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Please enter a valid email")
        return

    # verifier le numero
    numero = add_contact_numero.get()
    if not (numero.isdigit() and len(numero) == 10 and (numero.startswith("07") or numero.startswith("06") or numero.startswith("05"))):
        messagebox.showerror("Error", "Please enter a valid phone number")
        return

    # Si tout est correct open ficher et verifir si la personne exit deja sinon ajouter le 
    with open("C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact.txt" , "r") as fichier :
        contenu = fichier.readlines()
        exist = False
        for ligne in contenu:
            if add_contact_first_name_person.get().strip().lower() in ligne and add_contact_last_name_person.get().strip().lower() in ligne and add_contact_mail.get().strip() in ligne and add_contact_numero.get().strip() in ligne:
                exist = True
                break

        if exist:
            messagebox.showinfo("Info", "This contact already exists")
        else:
            with open("C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact.txt" , "a") as fichier_ajout :
                fichier_ajout.write(f"{add_contact_first_name_person.get().strip().lower()} | {add_contact_last_name_person.get().strip().lower()} | {add_contact_mail.get().strip()} | {add_contact_numero.get().strip()}\n")
            messagebox.showinfo("Success", "Contact added successfully!")
            response = messagebox.askyesno(
                "Success ,",
                 "Do you want to add another contact?")

            if response:  
                navigation(add_contact)  
            else:         
                navigation(menu) 


btn_enregistrer = tk.Button(
    add_contact,
    text="SAVE CONTACT",
    fg="white",
    bg="#2E86AB",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#1B4F72",
    activeforeground="white",
    relief="raised",
    command=save_contact
).pack(pady=(20, 10), ipadx=20, ipady=10)

btn_menu = create_menu_button(add_contact)
btn_menu.pack(pady=(10, 10), ipadx=20, ipady=10)


# ========================================================= PAGE REMOVE CONTACT ================================================================
remove_contact = tk.Frame(window, bg="#F0F4F8")
remove_contact.place(x=0, y=0, relwidth=1, relheight=1)

remove_contact_label = tk.Label(
    remove_contact,
    text="\"REMOVE CONTACT\"",
    font=("Comic Sans MS", 26, "bold"),
    fg="#2E86AB",
    bg="#F0F4F8",
    wraplength=500,
    justify="center"
)
remove_contact_label.pack(pady=(30, 20))

# Label de prenom
label_first_name = tk.Label(
    remove_contact,
    text="First Name of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)

# Entry de prenom
remove_contact_first_name_person = tk.Entry(
    remove_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
remove_contact_first_name_person.pack(pady=(10, 10), ipadx=20, ipady=10)

# Label de nom
label_last_name = tk.Label(
    remove_contact,
    text="Last Name of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)

# Entry de nom
remove_contact_last_name_person = tk.Entry(
    remove_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
remove_contact_last_name_person.pack(pady=(10, 10), ipadx=20, ipady=10)

# Label de numero
label_numero = tk.Label(
    remove_contact,
    text="Num of person :",
    font=("Arial", 14),
    bg="#F0F4F8"
).pack(pady=(10, 10), ipadx=20, ipady=10)

# Entry de numero
remove_contact_numero = tk.Entry(
    remove_contact,
    font=("Arial", 14),
    bd=2,
    relief="groove",
    justify="center"
)
remove_contact_numero.pack(pady=(10, 10), ipadx=20, ipady=10)

# foncion de remove 
def remove_contact_function():
    with open("C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact.txt", "r") as fichier:
        contenu = fichier.readlines()

    found = False
    new_contenu = []

    first = remove_contact_first_name_person.get().strip().lower()
    last = remove_contact_last_name_person.get().strip().lower()
    numero = remove_contact_numero.get().strip()

    for ligne in contenu:
        if first in ligne.lower() and last in ligne.lower() and numero in ligne:
            found = True   
        else:
            new_contenu.append(ligne)

    if found:
        with open("C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact.txt", "w") as fichier_modif:
            fichier_modif.writelines(new_contenu)

        response = messagebox.askyesno(
            "Success",
            "Contact removed successfully!\n\nDo you want to remove another contact?"
        )

        if response:
            navigation(remove_contact)
        else:
            navigation(menu)
    else:
        messagebox.showinfo("Oops", "This contact does not exist!")

# bouton de remove contact
btn_remove_contact = tk.Button(
    remove_contact,
    text="REMOVE CONTACT",
    fg="white",
    bg="#0CCCCF",
    font=("Comic Sans MS", 14, "bold"),
    activebackground="#C1790D",
    activeforeground="white",
    relief="raised",    
    command=remove_contact_function
)
btn_remove_contact.pack(pady=(20, 10), ipadx=20, ipady=10)

# bouton de menu
btn_menu_remove = create_menu_button(remove_contact)
btn_menu_remove.pack(pady=(10, 10), ipadx=20, ipady=10)

# ========================================================= PAGE DISPLAY CONTACT ================================================================
display_contact = tk.Frame(window, bg="#F0F4F8")
display_contact.place(x=0, y=0, relwidth=1, relheight=1)

display_contact_label = tk.Label(
    display_contact,
    text="\"DISPLAY CONTACT\"",
    font=("Comic Sans MS", 26, "bold"),
    fg="#2E86AB",
    bg="#F0F4F8",
    wraplength=500,
    justify="center"
)
display_contact_label.pack(pady=(30, 20))

div_contact = tk.Frame(display_contact, bg="#F0F4F8")
div_contact.pack(pady=10)

canvas = tk.Canvas(div_contact, bg="white", width=600, height=500)  
canvas.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(div_contact, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

contacts_frame = tk.Frame(canvas, bg="white", width=580)  
canvas.create_window((0, 0), window=contacts_frame, anchor="n")

contacts_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Titre centre
contacts_frame_label_titre = tk.Label(
    contacts_frame,
    text="Here are all your contacts:",
    font=("Comic Sans MS", 16, "bold"),
    fg="#0C5BED",
    bg="white",
    justify="center"
)
contacts_frame_label_titre.pack(pady=(10, 20), anchor="center")

contacts_frame_contenu = tk.Label(
    contacts_frame,
    text="",
    font=("Arial", 14),
    fg="black",
    bg="white",
    wraplength=500,
    justify="left"
)
contacts_frame_contenu.pack(pady=(10, 20))

def afficher_contacts():
    try:
        with open("C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact.txt", "r") as fichier:
            contenu = fichier.readlines()

            if len(contenu) == 0:
                contacts_frame_contenu.config(text="No contacts found ")
            else:
                contacts_text = ""
                for ligne in contenu:
                    contacts_text += f"FULL NAME : {ligne.split('|')[0].strip().title()} {ligne.split('|')[1].strip().title()}\nEMAIL : {ligne.split('|')[2].strip()}\nNUM : {ligne.split('|')[3].strip()}\n\n -------------------------------------------------------------------- \n\n"
                contacts_frame_contenu.config(text=contacts_text)
           
    except FileNotFoundError:
        contacts_frame_contenu.config(text="No contacts found ")
afficher_contacts()
# le buton de menu
btn_menu_display = create_menu_button(display_contact)
btn_menu_display.pack(pady=(10, 10), ipadx=20, ipady=10)


# ========================== Lancer la fenetre ==========================
navigation(principale)
window.mainloop()
