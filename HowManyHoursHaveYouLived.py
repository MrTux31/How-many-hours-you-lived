#!/usr/bin/env python3
# coding:utf-8

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
    rpc.update(details="Cherche le nombre d'heures qu'il à vécu", large_image="horloge_big")
except:
    # si discord est éteint alors on ignore le message d'erreur et on passe à la suite du programme
    pypresence.exceptions.InvalidPipe

# définir la fonction qui va calculer et afficher le nombre d'heures vécues
def get_age():
    # on vérifie si le calcul est possible
    try:
        # faire le calcul
        nombre_dheure = int(age_entry.get())* 8760
    # si l'utilisateur à rentré des caractères spéciaux, on affiche un message d'erreur
    except ValueError:
        messagebox.showerror("ERREUR", "Erreur, vous devez seulement rentrer des nombres.")

    # si l'age est inférireur à 0 alors on affiche une erreur
    if int(age_entry.get()) <=0:
        # on supprime l'affichage de l'ancien age
        age_show.config(text="")
        messagebox.showerror("ERREUR","Erreur, l'âge que vous entrez doit être compris entre 1 et 125 ans.")
    # si l'age est inférieur est compris entre 1 et 125 alors on peut passer au calcul et ainsi afficher le résultat
    elif int(age_entry.get()) <= 125:
            age_show.config(text=("Vous avez approximativement vécu  \n" + str(nombre_dheure) + " heures."), font=("Arial", 20),bg='#52e8a9', fg='#051614')
    # On prend 125 pour limite d'age max, bah oui lol, le record d'age le plus long c'est 122 ans
    # alors on prend 125 pour la marge x)
    if int(age_entry.get()) >125:
        # on supprime l'affichage de l'ancien age
        age_show.config(text="")
        messagebox.showerror("ERREUR","Erreur, l'âge que vous entrez doit être compris entre 1 et 125 ans. Mdr t'as crus que j'allais croire que tu as cet âge ? LOL")




# creer premiere fenetre

window = Tk()

# personaliser fenetre
window.title("How many hours have you lived")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("images/time.ico")
window.config(background='#52e8a9')

# creer la frame
frame = Frame(window, bg='#52e8a9' )


# ajouter un texte
label_title = Label(frame, text= "Combien d'heures as tu vécu ?", font=("Arial", 40), bg='#52e8a9', fg='#051614' )
label_title.pack()
# ajouter un sous titre

label_subtitle = Label(frame, text= "Entrez votre âge", font=("Arial", 25), bg='#52e8a9', fg='#051614' )
label_subtitle.pack()

# creer un champ
age_entry = Entry(frame, font=("Arial", 30), bg='#52e8a9', fg='#051614')
age_entry.pack()

#ajouter un bouton
button_validate_age = Button(frame, text= "Valider", font=("Arial", 30), bg='#0adbc2', fg='#051614', command=get_age)
button_validate_age.pack(pady=15, fill=X)
#afficher le nombre d'heures vécues
age_show = Label(frame, text="" , font=("Arial", 20), bg='#52e8a9', fg='#051614')
age_show.pack()
# afficher une image
width = 200
height = 200
image = PhotoImage(file="images/sablier.png").zoom(5).subsample(5)
canvas = Canvas(frame, width=width, height=height, bg='#52e8a9', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
#canvas.grid(row=2, column=1, sticky=S)
canvas.pack()

# ajouter
frame.pack(expand=YES)

# afficher
window.mainloop()









