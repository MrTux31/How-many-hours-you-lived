#!/usr/bin/env python3
# coding:utf-8

# HOW MANY HOURS YOU LIVED v2.5

# Un programme développé par MrTux31 (allias Tux31)
# MrTux31 git hub page : https://github.com/MrTux31
# HowManyHoursYouLived github page : https://github.com/MrTux31/How-many-hours-you-lived

# importer les composants nécessaires
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import datetime
from datetime import *
import pathlib
import os.path


# on crée la fonction qui va calculer combien d'heures l'utilisateur à vécu
def calcul_age():

    # on efface les anciennes données affichées à l'écran
    age_show.config(text="")
    # ces variables check permettent de vérifier tout au long de la procédure si toute les infos que l'utilisateur
    # sont bien justes et que pour le programme n'exécute pas un calcul complètement faux.
    checkd2 = 0
    checkm2 = 0
    checka2 = 0
    check2 = 0
    total_check = 0

    # RÉCUPÉRER LES DONNES DE TEMPS ACTUELLES (et conversion en heures)
    date1 = datetime.now()
    jour = date1.day * 24
    mois = date1.month * 730
    heure = date1.hour
    minute = date1.minute * 0.0166667
    seconde = date1.second * 0.000277778
    annee = date1.year * 8760
    total_hours1 = jour+mois+heure+minute+seconde+annee
    # RÉCUPÉRER LA DATE DE L'UTILISATEUR
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        date2 = int(date2_entry.get())
        date2 = date2 * 24
        checkd2 = 1
    except ValueError:
        # si l'utilisateur a rentré des caractères spéciaux, on affiche un message d'erreur
        pass  # todo
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de "
                                       "valider.")
        checkd2 = 0

    # si la date est inférieure à 0 alors on affiche une erreur
    if int(date2_entry.get()) <= 0:
        age_show.config(text="")
        messagebox.showerror("ERREUR JOUR DE NAISSANCE", "Erreur, le jour de votre naissance que vous entrez doit être "
                                                         "compris entre 1 et 31.")
        checkd2 = 0
    if int(date2_entry.get()) > 31:
        # si la date est supérieure à 31 alors on affiche un message d'erreur
        age_show.config(text="")
        messagebox.showerror("ERREUR JOUR DE NAISSANCE", "Erreur, le jour de votre naissance que vous entrez doit être "
                                                         "compris entre 1 et 31.")
        checkd2 = 0

    # récupérer le mois 2
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        month2 = int(month2_entry.get())
        month2 = month2 * 730
        checkm2 = 1
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        pass  # todo
        age_show.config(text="")
        messagebox.showerror("ERREUR", "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de "
                                       "valider.")
        checkm2 = 0

    # si le mois est inférireur à 0 alors on affiche une erreur
    if int(month2_entry.get()) <= 0:
        age_show.config(text="")
        messagebox.showerror("ERREUR MOIS DE NAISSANCE", "Erreur, le mois de votre naissance que vous entrez doit être "
                                                         "compris entre 1 et 12.")
        checkm2 = 0
    # si le mois est supérieur à 12, alors on affiche une erreur
    if int(month2_entry.get()) > 12:
        age_show.config(text="")
        messagebox.showerror("ERREUR MOIS DE NAISSANCE", "Erreur, le mois de votre naissance que vous entrez doit être "
                                                         "compris entre 1 et 12.")
        checkm2 = 0

    # récupérer l'année 2
    try:
        age_show.config(text="")
        # on essaie de faire le calcul
        year2 = int(year2_entry.get())
        year2 = year2 * 8760
        checka2 = 1
    except ValueError:
        # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
        pass  # todo
        age_show.config(text="")
        messagebox.showerror("ERREUR",
                             "Erreur, merci de remplir toutes les lignes seulement avec des nombres avant de valider.")
        checka2 = 0

    # si l'année est inférieure à 1900 alors on affiche une erreur
    if int(year2_entry.get()) < 1900:
        age_show.config(text="")
        messagebox.showerror("ERREUR ANNÉE DE NAISSANCE",
                             "Erreur, l'année de votre naissance que vous entrez doit être comprise entre 1900 et "
                             "9999.")
        checka2 = 0
    # si l'année est inférieure à 1900 alors on affiche une erreur
    if int(year2_entry.get()) > 9999:
        age_show.config(text="")
        messagebox.showerror("ERREUR ANNÉE DE NAISSANCE",
                             "Erreur, l'année de votre naissance que vous entrez doit être comprise entre 1900 et "
                             "9999.")
        checka2 = 0

        # on fait le total des heures de la date de  naissance
    total_hours2 = date2 + month2 + year2
    # si le nombre d'heures de la date de naissance est supérireure à la date actuelle, il y a une erreur.
    if total_hours2 > total_hours1:
        age_show.config(text="")
        # on affiche l'erreur
        messagebox.showerror("ERREUR", "Erreur, l'année de la date de naissance est plus grande que celle de l'année "
                                       "actuelle, merci de rectifier le problème.")
        checka2 = 0

    # total des checks
    check2 = checkd2 + checkm2 + checka2
    total_check = check2

    # CRÉER UNE VARIABLE QUI COMPTE LE NOMBRE DE REPS JUSTES
    if total_check == 3:
        # on fait la soustraction des heures de la date actuelle et de la date de naissance
        try:
            total_life_hours = total_hours1 - total_hours2
            total_life_hours = int(total_life_hours)
            total_days = total_life_hours / 24
            total_days = int(total_days)
            # on affiche combien d'heures l'utilisateur à vécu
            age_show.config(text=("Vous avez approximativement vécu  \n" + str(total_life_hours) + " heures" + " soit "
                                  + str(total_days) + " jours."),
                            font=("Arial", 20), bg='#52e8a9', fg='#051614')
            # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
        except ValueError:
            age_show.config(text="")
            messagebox.showerror("ERREUR",
                                 "Erreur, merci de remplir toutes les lignes seulement "
                                 "avec des nombres avant de valider.")


# on crée une fenêtre
window = Tk()

# personaliser fenêtre
window.title("How many hours have you lived")
window.geometry("1080x810")
window.minsize(480, 360)

path_to_images = os.path.abspath(str(pathlib.Path(__file__).parent.resolve()) + "/images")
window.iconphoto(False, PhotoImage(file=path_to_images + "/time.png"))

window.config(background='#52e8a9')

# créer la frame
frame = Frame(window, bg='#52e8a9')

# ajouter un texte
label_title = Label(frame, text="Combien d'heures as tu vécu ?", font=("Arial", 30), bg='#52e8a9', fg='#051614')
label_title.pack()


# DATE DE NAISSANCE

# ajouter un sous titre de la date 2
label_subtitle = Label(frame, text="Entrez le jour de votre naissance (sous la forme JJ)", font=("Arial", 20),
                       bg='#52e8a9', fg='#051614')
label_subtitle.pack()

# créer un champ de la date 2
date2_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
date2_entry.pack()
# ajouter un sous titre du mois 2
label_subtitle = Label(frame, text="Entrez le mois de votre naissance (sous la forme MM)", font=("Arial", 20),
                       bg='#52e8a9', fg='#051614')
label_subtitle.pack()
# créer un champ du mois 2
month2_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
month2_entry.pack()
# ajouter un sous titre de l'année 2
label_subtitle = Label(frame, text="Entrez l'année de votre naissance (sous la forme AAAA)", font=("Arial", 20),
                       bg='#52e8a9', fg='#051614')
label_subtitle.pack()
# créer un champ de l'année 2
year2_entry = Entry(frame, font=("Arial", 20), bg='#52e8a9', fg='#051614')
year2_entry.pack()

# ajouter un bouton
button_validate_age = Button(frame, text="Actualiser", font=("Arial", 30), bg='#0adbc2', fg='#051614',
                             command=calcul_age)
button_validate_age.pack(pady=15, fill=X)

# afficher le nombre d'heures vécues
age_show = Label(frame, text="", font=("Arial", 25), bg='#52e8a9', fg='#051614')
age_show.pack()

# afficher une image
width = 150
height = 150
image = PhotoImage(file="images/sablier.png").zoom(2).subsample(3)
canvas = Canvas(frame, width=width, height=height, bg='#52e8a9', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
# canvas.grid(row=2, column=1, sticky=S)
canvas.pack()

# ajouter
frame.pack(expand=YES)

# afficher le tout
window.mainloop()
