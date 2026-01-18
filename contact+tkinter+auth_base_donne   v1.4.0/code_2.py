import tkinter as tk
import sqlite3 as bd
from tkinter import messagebox
import bcrypt

# ------------------------------------------- la fenetre principale ------------------------------------------------
window = tk.Tk()
window.title("CONTACT's PROGRAMME")
window.geometry("1000x600")
window.configure(bg="#F0F4F8")
principale_photo = tk.PhotoImage(file="C:\\Users\\admin\\Desktop\\SDIA - ENSAM MEKNES\\python\\projet contact VERSIONs\\contact+tkinter+auth v1.3.0\\photos\\unnamed.png")
id_utilisateur = None

# -------------------------------------------------- les fonctions ------------------------------------------------------
def navigation(page):
    page.tkraise()

def remove():
    window.destroy()

def create_principale_button(parent , text , navigertion_vers):
    return tk.Button(
        parent,
        text=text,
        fg="white",
        bg="#ED3629",
        font=("Comic Sans MS", 14, "bold"),
        activebackground="#684D12",
        activeforeground="white",
        relief="raised",
        command=lambda: navigertion_vers
    )

def afficher_photo(parent):
    label_img = tk.Label(parent, image=principale_photo, bg="#F0F4F8")
    label_img.pack(expand=True, fill="both")

def sign_up_fct(full_name, mail, password, verify_password):
    
    # verification des donnees 
    full_name = full_name.strip()
    mail = mail.strip()
    password = password.strip()
    verify_password = verify_password.strip()

    if not mail or not password or not verify_password or not full_name:
        messagebox.showerror("ERROR", "Please fill all fields")
        return

    if "@" not in mail or "." not in mail:
        messagebox.showerror("ERROR", "Invalid email format")
        return

    if password != verify_password:
        messagebox.showerror("ERROR", "Passwords do not match")
        return

    # creation et connection  a la base de donnee
    with bd.connect("contacts.db") as conn:
        cursor = conn.cursor()
        
        # creation de cableau si il nest pas exist 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
         
        # verifier l'existence du compte par email
        cursor.execute(
            "SELECT * FROM users WHERE email = ?",(mail,)
        )

        user = cursor.fetchone()

        # si l'email existe deja
        if user:
            messagebox.showerror("ERROR", "This email is already used")
            return

        # Hasher le mot de passe
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        # enregistrer l'utilisateur dans la base de donnees
        cursor.execute(
              "INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)",(full_name, mail, hashed_password.decode("utf-8"))
        )

        # valider les modifications
        conn.commit()
        messagebox.showinfo("SUCCESS", "Account created successfully!")
        navigation(Log_in)

def  log_in_fct(mail , password):

    mail = mail.strip()
    password_bytes = password.strip().encode("utf-8")

    global utilisateur, id_utilisateur , utilisateur_var

    # connection  a la base de donnee
    with bd.connect("contacts.db") as conn:
        cursor = conn.cursor()
         
        # verifier l'existence du compte par email
        cursor.execute(
            "SELECT * FROM users WHERE email = ?",(mail,)
        )

        user = cursor.fetchone()

        # si l'email nexist ps
        if not user:
            messagebox.showerror("ERROR", "This Account not fount ")
            return
      
        # email exist ( verifier si passord orrect )
        passwod_bd = user[3]
        if bcrypt.checkpw(password_bytes, passwod_bd.strip().encode()):
            messagebox.showinfo("Login Success", "Welcome to the Contact's programme")
            navigation(menu)

            id_utilisateur = user[0]
            utilisateur_var.set(f"Welcome Again {user[1]} !")

            return
        else:
            messagebox.showerror("Error", "Invalid password")
            return

def button(parent , text, naviger_vers):
    return tk.Button(
          parent, 
          text=text, 
          fg="white", 
          bg="#C04F40",
          font=("Comic Sans MS", 14, "bold"), 
          relief="raised",
          activebackground="#C15E0D", 
          activeforeground="white",
          command=lambda: navigation(naviger_vers)).pack(pady=10, ipadx=20, ipady=10)

def add_person_person(full_name, adress_email, numero):
         full_name = full_name.strip()
         adress_email = adress_email.strip()
         numero = numero.strip()
         global id_utilisateur

         # create table all_contact if not exist
         with bd.connect("contacts.db") as conn:
              cursor = conn.cursor()
              cursor.execute("""
              CREATE TABLE IF NOT EXISTS all_contact (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER NOT NULL,
                   full_name TEXT NOT NULL,
                   adress_email TEXT NOT NULL,
                   numero TEXT NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users(id)
              )
              """)

              # inserer la personne dans la table all_contact
              cursor.execute(
                   "INSERT INTO all_contact (user_id, full_name, adress_email, numero) VALUES (?, ?, ?, ?)",
                   (id_utilisateur, full_name, adress_email, numero)
              )

              conn.commit()
              messagebox.showinfo("SUCCESS", "Person added to your contact successfully!")

              # clear the entry fields
              add_person_fullName.delete(0, tk.END)
              add_person_adress_email.delete(0, tk.END)
              add_person_numero.delete(0, tk.END)

              response = messagebox.askyesno(
                "Success ,",
                 "Do you want to add another contact?")

              if response:  
                  navigation(add_person)  
              else:         
                  navigation(menu)

def remove_person_person(adress_email, numero):
            adress_email = adress_email.strip()
            numero = numero.strip()
            global id_utilisateur
    
            with bd.connect("contacts.db") as conn:
                cursor = conn.cursor()
    
                # verifier si la personne existe dans les contacts de l'utilisateur
                cursor.execute(
                    "SELECT * FROM all_contact WHERE user_id = ? AND adress_email = ? AND numero = ?",
                    (id_utilisateur, adress_email, numero)
                )
    
                person = cursor.fetchone()
    
                if not person:
                    messagebox.showerror("ERROR", "This person not found in your contacts")
                    return
    
                # supprimer la personne des contacts
                cursor.execute(
                    "DELETE FROM all_contact WHERE user_id = ? AND adress_email = ? AND numero = ?",
                    (id_utilisateur, adress_email, numero)
                )
    
                conn.commit()
                messagebox.showinfo("SUCCESS", "Person removed from your contact successfully!")
    
                # clear the entry fields
                remove_person_adress_email.delete(0, tk.END)
                remove_person_numero.delete(0, tk.END)
    
                response = messagebox.askyesno(
                    "Success ,",
                    "Do you want to remove another contact?")
    
                if response:  
                    navigation(remove_person)  
                else:         
                    navigation(menu)            
    
def afficher_contacts():
    global id_utilisateur
    with bd.connect("contacts.db") as conn:
        cursor = conn.cursor()
        
        # recuperer les contacts de l'utilisateur
        cursor.execute(
            "SELECT full_name, adress_email, numero FROM all_contact WHERE user_id = ?",
            (id_utilisateur,)
        )
        
        contacts = cursor.fetchall()
        if not contacts:
            contacts_frame_contenu.config(text="You have no contacts yet.")
            return
        
        contact_list = ""
        for contact in contacts:
            contact_list += f"Full Name: {contact[0]}\nEmail: {contact[1]}\nNumero: {contact[2]}\n\n\n"
        
        contacts_frame_contenu.config(text=contact_list.strip())

def delete_all_contact():
    response = messagebox.askyesno(
        "Verification",
        "Are you sure?\nYou want to remove all your contacts?"
    )
    if response:
        global id_utilisateur
        with bd.connect("contacts.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM all_contact WHERE user_id = ?",
                (id_utilisateur,)
            )
            conn.commit()
            messagebox.showinfo("SUCCESS", "All your contacts have been deleted successfully!")
    navigation(menu)

# ----------------------------------------------- la page principale ----------------------------------------------------
principale = tk.Frame(window, bg="#F0F4F8")
principale.place(x=0, y=0, relwidth=1, relheight=1)

gauche_principale = tk.Frame(principale, bg="#F0F4F8")
gauche_principale.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_principale = tk.Frame(principale, bg="#F0F4F8")
droite_principale.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Contenu gauche
tk.Label(gauche_principale,
         text="WELCOME TO YOUR CONTACT'S PROGRAM ",
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, 
         justify="center").pack(pady=(0, 20))

tk.Button(gauche_principale, 
          text="Sign Up", 
          fg="white", 
          bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), 
          relief="raised",
          activebackground="#C15E0D", 
          activeforeground="white",
          command=lambda: navigation(Sign_up)
          ).pack(pady=10, ipadx=20, ipady=10)

tk.Button(gauche_principale, 
          text="Log in", 
          fg="white", 
          bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), 
          relief="raised",
          activebackground="#C15E0D", 
          activeforeground="white",
          command=lambda: navigation(Log_in)
          ).pack(pady=10, ipadx=20, ipady=10)

tk.Button(gauche_principale, 
          text="EXIT", 
          fg="white", 
          bg="#C04F40",
          font=("Comic Sans MS", 14, "bold"), 
          relief="raised",
          activebackground="#C15E0D", 
          activeforeground="white",
          command=lambda: remove()).pack(pady=10, ipadx=20, ipady=10)

# Contenu droite (image)
afficher_photo(droite_principale)



# ================================================== La Page sign up ====================================================
Sign_up = tk.Frame(window, bg="#F0F4F8")
Sign_up.place(x=0, y=0, relwidth=1, relheight=1)

gauche_sign_up = tk.Frame(Sign_up, bg="#F0F4F8")
gauche_sign_up.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_sign_up = tk.Frame(Sign_up, bg="#F0F4F8")
droite_sign_up.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Contenu gauche
tk.Label(gauche_sign_up, text="SIGN UP TO YOUR CONTACT'S PROGRAMME",
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, justify="center").pack(pady=(0, 20))

tk.Label(gauche_sign_up, text="Full Name: ", bg="#F0F4F8").pack(anchor="w", pady=5)
sign_up_FullName = tk.Entry(gauche_sign_up, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
sign_up_FullName.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_sign_up, 
         text="Adress_Mail: ", 
         bg="#F0F4F8").pack(anchor="w", pady=5)

auth_mail_sign_up = tk.Entry(gauche_sign_up, 
                             font=("Arial", 14), 
                             bd=2, relief="groove", 
                             justify="center")
auth_mail_sign_up.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_sign_up, 
         text="Password: ", 
         bg="#F0F4F8").pack(anchor="w", pady=5)
auth_paswrd_sign_up = tk.Entry(gauche_sign_up, font=("Arial", 14), bd=2, relief="groove", justify="center", show="*")
auth_paswrd_sign_up.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_sign_up, 
         text="Verify Password: ", 
         bg="#F0F4F8").pack(anchor="w", pady=5)
auth_paswrd_verify = tk.Entry(gauche_sign_up, font=("Arial", 14), bd=2, relief="groove", justify="center", show="*")
auth_paswrd_verify.pack(pady=5, ipadx=50, ipady=5)

tk.Button(gauche_sign_up, text="Sign Up", fg="white", bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#C15E0D", activeforeground="white",
          command=lambda: sign_up_fct( sign_up_FullName.get(),
                                       auth_mail_sign_up.get(),
                                      auth_paswrd_sign_up.get(),
                                      auth_paswrd_verify.get())
          ).pack(pady=10, ipadx=20, ipady=10)

button(gauche_sign_up, "return to main menu", principale)

# Contenu droite (image)
afficher_photo(droite_sign_up)




# =================================================================== La Page Log in ===============================================================
Log_in = tk.Frame(window, bg="#F0F4F8")
Log_in.place(x=0, y=0, relwidth=1, relheight=1)

gauche_log_in = tk.Frame(Log_in, bg="#F0F4F8")
gauche_log_in.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_log_in = tk.Frame(Log_in, bg="#F0F4F8")
droite_log_in.pack(side="right", fill="both", expand=True, padx=20, pady=20)

tk.Label(gauche_log_in, text="LOG IN TO YOUR CONTACT'S PROGRAMME",
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, justify="center").pack(pady=(0, 20))

tk.Label(gauche_log_in, text="Adress Email: ", bg="#F0F4F8").pack(anchor="w", pady=5)
log_in_email = tk.Entry(gauche_log_in, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
log_in_email.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_log_in, text="Password: ", bg="#F0F4F8").pack(anchor="w", pady=5)
log_in_password = tk.Entry(gauche_log_in, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center", show="*")
log_in_password.pack(pady=5, ipadx=50, ipady=5)

tk.Button(gauche_log_in, text="Log In", fg="white", bg="#0CCCCF", 
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#C15E0D", activeforeground="white", 
          command=lambda: log_in_fct(log_in_email.get(), log_in_password.get())
          ).pack(pady=10, ipadx=20, ipady=10)

button(gauche_log_in, "return to main menu", principale)

# Contenu droite (image)
afficher_photo(droite_log_in)                                      




# =================================================================== La Page Menu ===============================================================
menu = tk.Frame(window, bg="#F0F4F8")
menu.place(x=0, y=0, relwidth=1, relheight=1)

gauche_menu = tk.Frame(menu, bg="#F0F4F8")
gauche_menu.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_menu = tk.Frame(menu, bg="#F0F4F8")
droite_menu.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# conenu gauche (boutons)
utilisateur_var = tk.StringVar()
utilisateur_var.set("Welcome Again")

tk.Label(gauche_menu,
         textvariable=utilisateur_var,
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, 
         justify="center").pack(pady=(0, 20))

btn1 = tk.Button(gauche_menu, text="Add person to your contact", fg="white", bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#9DEAFF", activeforeground="white",
          command=lambda: navigation(add_person)
          ).pack(pady=10, ipadx=20, ipady=10)

btn2 = tk.Button(gauche_menu, text="Remove person to your contact", fg="white", bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#9DEAFF", activeforeground="white",
          command=lambda: navigation(remove_person)
          ).pack(pady=10, ipadx=20, ipady=10)

btn3= tk.Button(gauche_menu, text="Display your contact", fg="white", bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#9DEAFF", activeforeground="white",
          command=lambda: (afficher_contacts(), navigation(display))
          ).pack(pady=10, ipadx=20, ipady=10)

btn4 = tk.Button(gauche_menu, text="Delete all your contact", fg="white", bg="#0CCCCF",
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#9DEAFF", activeforeground="white",
          command=lambda: navigation(delete_all_contact())
          ).pack(pady=10, ipadx=20, ipady=10)

button(gauche_menu, "return to main menu", principale)

# Contenu droite (image)
afficher_photo(droite_menu)





# =================================================================== La ADD PERSON ========================================================================
add_person = tk.Frame(window, bg="#F0F4F8")
add_person.place(x=0, y=0, relwidth=1, relheight=1)

gauche_add_person = tk.Frame(add_person, bg="#F0F4F8")
gauche_add_person.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_add_person = tk.Frame(add_person, bg="#F0F4F8")
droite_add_person.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# conenu gauche 

tk.Label(gauche_add_person,
         text = "ADD PERSON TO YOUR CONTACT'S PROGRAMME",
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, 
         justify="center").pack(pady=(0, 20))

tk.Label(gauche_add_person, text="Full Name: ", bg="#F0F4F8").pack(anchor="w", pady=5)
add_person_fullName = tk.Entry(gauche_add_person, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
add_person_fullName.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_add_person, text="Adress Email: ", bg="#F0F4F8").pack(anchor="w", pady=5)
add_person_adress_email = tk.Entry(gauche_add_person, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
add_person_adress_email.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_add_person, text="Numero : ", bg="#F0F4F8").pack(anchor="w", pady=5)
add_person_numero = tk.Entry(gauche_add_person, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
add_person_numero.pack(pady=5, ipadx=50, ipady=5)

tk.Button(gauche_add_person, text="Save", fg="white", bg="#0CCCCF", 
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#C15E0D", activeforeground="white", 
          command=lambda: add_person_person(add_person_fullName.get(), add_person_adress_email.get(), add_person_numero.get())
          ).pack(pady=10, ipadx=20, ipady=10)

button(gauche_add_person, "return to main menu", menu)

# Contenu droite (image)
afficher_photo(droite_add_person)



# =================================================================== REMOVE PERSON ========================================================================
remove_person = tk.Frame(window, bg="#F0F4F8")
remove_person.place(x=0, y=0, relwidth=1, relheight=1)

gauche_remove_person = tk.Frame(remove_person, bg="#F0F4F8")
gauche_remove_person.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_remove_person = tk.Frame(remove_person, bg="#F0F4F8")
droite_remove_person.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# conenu gauche
tk.Label(gauche_remove_person,
         text = "REMOVE PERSON FROM YOUR CONTACT'S PROGRAMME",
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, 
         justify="center").pack(pady=(0, 20))

tk.Label(gauche_remove_person, text="Adress Email: ", bg="#F0F4F8").pack(anchor="w", pady=5)
remove_person_adress_email = tk.Entry(gauche_remove_person, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
remove_person_adress_email.pack(pady=5, ipadx=50, ipady=5)

tk.Label(gauche_remove_person, text="Numero : ", bg="#F0F4F8").pack(anchor="w", pady=5)
remove_person_numero = tk.Entry(gauche_remove_person, 
                            font=("Arial", 14), 
                            bd=2, 
                            relief="groove", 
                            justify="center")
remove_person_numero.pack(pady=5, ipadx=50, ipady=5)

tk.Button(gauche_remove_person, text="Delete", fg="white", bg="#0CCCCF", 
          font=("Comic Sans MS", 14, "bold"), relief="raised",
          activebackground="#BCC854", activeforeground="white", 
          command=lambda: remove_person_person(remove_person_adress_email.get(), remove_person_numero.get())
          ).pack(pady=10, ipadx=20, ipady=10)

button(gauche_remove_person, "return to main menu", menu)

# Contenu droite (image)
afficher_photo(droite_remove_person)





# =================================================================== DISPLAY CONTACT ========================================================================
display = tk.Frame(window, bg="#F0F4F8")
display.place(x=0, y=0, relwidth=1, relheight=1)

gauche_display = tk.Frame(display, bg="#F0F4F8")
gauche_display.pack(side="left", fill="both", expand=True, padx=20, pady=20)

droite_display = tk.Frame(display, bg="#F0F4F8")
droite_display.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# conenu gauche
tk.Label(gauche_display,
         text = "DISPLAY CONTACTS",
         font=("Comic Sans MS", 20, "bold"), fg="#2E86AB", bg="#F0F4F8",
         wraplength=400, 
         justify="center").pack(pady=(0, 20))

div_contact = tk.Frame(gauche_display, bg="#F0F4F8")
div_contact.pack(pady=10)

canvas = tk.Canvas(div_contact, bg="white", width=600, height=400)  
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

button(gauche_display, "return to main menu", menu)


# contanu droite (image)
afficher_photo(droite_display)

# ================================================== Lancer la fenetre ====================================================
navigation(principale)
window.mainloop()