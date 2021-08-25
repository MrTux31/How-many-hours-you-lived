#!/usr/bin/env python3
# coding:utf-8

#HOW MANY HOURS YOU LIVED v2.1

# Un programme dévellopé par MrTux31 (allias Tux31)
# MrTux31 git hub page : https://github.com/MrTux31
# HowManyHoursYouLived github page : https://github.com/MrTux31/How-many-hours-you-lived


# importer les composants nécessaires
import pypresence
from pypresence import Presence
from tkinter import *
from tkinter import Tk
from tkinter import messagebox

# on essai d'afficher le status de l'application su discord
try:
    # si discord est démarré alors on affiche le status
    rpc = Presence("878264252044030022")
    rpc.connect()
    rpc.update(details="Regarde combien \n d'heures il à vécu ", large_image="horloge_big")
# si discord est éteint alors on ignore le message d'erreur et on passe à la suite du programme
except:
    pypresence.exceptions.InvalidPipe


# on crée la fonction qui va calculer combien d'heures l'utilisateur à vécu
def calcul_age():

    # on efface les anciennes données affichées à l'écran
    age_show.config(text="")
    # ces variables check permettent de vérifier tout au long de la procédure si toute les infos que l'utilisateur
    # sont bien justes et que pour le programme n'exécute pas un calcul complètement faux.
    checkd1 = 0
    checkm1 = 0
    checka1 = 0
    checkd2 = 0
    checkm2 = 0
    checka2 = 0
    check1 = 0
    check2 = 0
    total_check = 0
    # RECUPERER LA DATE 1
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        date1 = int(date1_entry.get())
        date1 = date1 * 24
        checkd1 = 1
        print(date1)
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checkd1 = 0
        # si le jour est inférireure à 0 alors on affiche une erreur
    if int(date1_entry.get()) <= 0:
        age_show.config(text="")
        messagebox.showerror("ERREUR JOUR ACTUEL", "Erreur, le jour actuel que vous entrez doit être compris entre 1 et 31.")
        checkd1 = 0
        age_show.config(text="")
        # si l'utilisateur à rentré un jour supérieure à 31 alors on affiche un message d'erreur
    if int(date1_entry.get()) > 31:
        messagebox.showerror("ERREUR JOUR ACTUEL", "Erreur, le jour actuel que vous entrez doit être compris entre 1 et 31.")
        checkd1 = 0
        age_show.config(text="")

    # récupérer le mois 1
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        month1 = int(month1_entry.get())
        month1 = month1 * 730
        checkm1 = 1
        print(month1)
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checkm1 = 0

    # si le mois est inférireur à 0 alors on affiche une erreur
    if int(month1_entry.get()) <= 0:
        age_show.config(text="")
        messagebox.showerror("ERREUR MOIS ACTUEL", "Erreur, le mois actuel que vous entrez doit être compris entre 1 et 12.")
        age_show.config(text="")
        checkm1 = 0
    # si le mois est supérieur à 12 alors on affiche un message d'erreur
    if int(month1_entry.get()) > 12:
        age_show.config(text="")
        messagebox.showerror("ERREUR MOIS ACTUEL", "Erreur, le mois actuel que vous entrez doit être compris entre 1 et 12.")
        checkm1 = 0

    # récupérer l'année 1

    try:
        age_show.config(text="")
        # on essaye de faire le calcul
        year1 = int(year1_entry.get())
        year1 = year1 * 8760
        checka1 = 1
        print(year1)
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checka1 = 0

    # si l'année est inférireure à 1900 alors on affiche une erreur
    if int(year1_entry.get()) < 1900:
        age_show.config(text="")
        messagebox.showerror("ERREUR ANNE ACTUELLE", "Erreur, l'année actuelle que vous entrez doit être comprise entre 1900 et 9999.")
        checka1 = 0
    # si l'année est inférireure à 1900 alors on affiche une erreur
    if int(year1_entry.get()) > 9999:
        age_show.config(text="")
        messagebox.showerror("ERREUR ANNE ACTUELLE",
                                 "Erreur, l'année actuelle que vous entrez doit être comprise entre 1900 et 9999.")
        checka1 = 0

    # on fait le total des heures de la date actuelle
    total_hours1 = date1 + month1 + year1
    check1 = checkd1 + checkm1 + checka1

    # RECUPERER LA DATE 2
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        date2 = int(date2_entry.get())
        date2 = date2 * 24
        checkd2 = 1
        print(date2)
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checkd2 = 0

    # si la date est inférireure à 0 alors on affiche une erreur
    if int(date2_entry.get()) <= 0:
        age_show.config(text="")
        messagebox.showerror("ERREUR JOUR DE NAISSANCE", "Erreur, le jour de votre naissance que vous entrez doit être compris entre 1 et 31.")
        checkd2 = 0

    # si la date est supérieur à 31 alor on affiche un message d'erreur
    if int(date2_entry.get()) > 31:
        age_show.config(text="")
        messagebox.showerror("ERREUR JOUR DE NAISSANCE", "Erreur, le jour de votre naissance que vous entrez doit être compris entre 1 et 31.")
        checkd2 = 0

    # récupérer le mois 2
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        month2 = int(month2_entry.get())
        month2 = month2 * 730
        checkm2 = 1
        print(month2)
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checkm2 = 0

    # si le mois est inférireur à 0 alors on affiche une erreur
    if int(month2_entry.get()) <= 0:
        age_show.config(text="")
        messagebox.showerror("ERREUR MOIS DE NAISSANCE", "Erreur, le mois de votre naissance que vous entrez doit être compris entre 1 et 12.")
        checkm2 = 0
    # si le mois est supérieur à 12, alors on affiche une erreur
    if int(month2_entry.get()) > 12:
        age_show.config(text="")
        messagebox.showerror("ERREUR MOIS DE NAISSANCE", "Erreur, le mois de votre naissance que vous entrez doit être compris entre 1 et 12.")
        checkm2 = 0

   # récupérer l'année 2

    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        year2 = int(year2_entry.get())
        year2 = year2 * 8760
        checka2 = 1
        print(year2)

        # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass
        age_show.config(text="")
        messagebox.showerror("ERREUR",
                             "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checka2 = 0

    # si l'année est inférireure à 1900 alors on affiche une erreur
    if int(year2_entry.get()) < 1900:
        age_show.config(text="")
        messagebox.showerror("ERREUR ANNEE DE NAISSANCE",
                             "Erreur, l'année de votre naissance que vous entrez doit être comprise entre 1900 et 9999.")
        checka2 = 0
    # si l'année est inférireure à 1900 alors on affiche une erreur
    if int(year2_entry.get()) > 9999:
        age_show.config(text="")
        messagebox.showerror("ERREUR ANNEE DE NAISSANCE",
                                 "Erreur, l'année de votre naissance que vous entrez doit être comprise entre 1900 et 9999.")
        checka2 = 0

        # on fait le total des heures de la date de  naissance
    total_hours2 = date2 + month2 + year2
    # si le nombre d'heures de la date de naissance est supérireure à la date actuelle, il y a une erreur.
    if total_hours2 > total_hours1:
        age_show.config(text="")
        # on affiche l'erreur
        messagebox.showerror("ERREUR","Erreur, l'année de la date de naissance est plus grande que celle de l'année actuelle, merci de rectifier le problème.")
        checka2 = 0

    # total des checks
    check2 = checkd2 + checkm2 + checka2
    total_check = check1 + check2

    # CREER UNE VARIABLE QUI COMPTE LE NOMBRE DE REPS JUSTES
    if total_check == 6:
        # on fait la soustraction des heures de la date actuelle et de la date de naissance
        try:
            total_life_hours = total_hours1 - total_hours2
            total_days = total_life_hours / 24
            # on affiche combien d'heures l'utilisateur à vécu
            age_show.config(text=("Vous avez approximativement vécu  \n" + str(total_life_hours) + " heures" + " soit " + str(total_days) + " jours."),
                            font=("Arial", 20), bg='#52e8a9', fg='#051614')
            # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
        except ValueError:
            age_show.config(text="")
            messagebox.showerror("ERREUR",
                                 "Erreur, merci de remplir toutes les lignes seulement "
                                 "avec des nombres avant de valider.")




# on crée une fenetre

window = Tk()

# personaliser fenetre
window.title("How many hours have you lived")
window.geometry("1080x810")
window.minsize(480, 360)
window.iconbitmap("images/time.ico")
window.config(background='#52e8a9')

# creer la frame
frame = Frame(window, bg='#52e8a9')



# ajouter un texte
label_title = Label(frame, text= "Combien d'heures as tu vécu ?", font=("Arial", 30), bg='#52e8a9', fg='#051614' )
label_title.pack()

# JOUR ACTUEL

# ajouter un sous titre de la date 1
label_subtitle = Label(frame, text= "Entrez le jour actuel (sous la forme JJ)", font=("Arial", 20), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()

# creer un champ de la date 1
date1_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
date1_entry.pack()
# ajouter un sous titre du mois 1
label_subtitle = Label(frame, text= "Entrez le mois actuel (sous la forme MM)", font=("Arial", 20), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()
# creer un champ du mois 1
month1_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
month1_entry.pack()
# ajouter un sous titre de l'année 1
label_subtitle = Label(frame, text= "Entrez l'année actuelle (sous la forme AAAA)", font=("Arial", 20), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()
# creer un champ de l'année 1
year1_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
year1_entry.pack()

# DATE DE NAISSANCE

# ajouter un sous titre de la date 2
label_subtitle = Label(frame, text= "Entrez le jour de votre naissance (sous la forme JJ)", font=("Arial", 20), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()

# creer un champ de la date 2
date2_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
date2_entry.pack()
# ajouter un sous titre du mois 2
label_subtitle = Label(frame, text= "Entrez le mois de votre naissance (sous la forme MM)", font=("Arial", 20), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()
# creer un champ du mois 2
month2_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
month2_entry.pack()
# ajouter un sous titre de l'année 2
label_subtitle = Label(frame, text= "Entrez l'année de votre naissance (sous la forme AAAA)", font=("Arial", 20), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()
# creer un champ de l'année 2
year2_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
year2_entry.pack()




#ajouter un bouton
button_validate_age = Button(frame, text= "Valider", font=("Arial", 30), bg='#0adbc2', fg='#051614', command=calcul_age)
button_validate_age.pack(pady=15, fill=X)



#afficher le nombre d'heures vécues
age_show = Label(frame, text="" , font=("Arial", 25), bg='#52e8a9', fg='#051614')
age_show.pack()

# afficher une image
width = 150
height = 150
image = PhotoImage(file="images/sablier.png").zoom(2).subsample(3)
canvas = Canvas(frame, width=width, height=height, bg='#52e8a9', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
#canvas.grid(row=2, column=1, sticky=S)
canvas.pack()

# ajouter
frame.pack(expand=YES)

# afficher le tout
window.mainloop()

