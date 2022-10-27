#!/usr/bin/env python3

# Auteur : Abdallah YAMANI
# Derniere modification : 28/10/2022
# Script : script.py
# Version : 1.2
# Dercription : Script installation


import sys
import os

def check_result(result):
    # Verification du résultat
    if result == 0:
        print("Installation reussie !")
    else:
        print("Installation echouee... :(")
        # Arret de l'execution du programme en cas d'erreur
        sys.exit(result)

def install_web():
    print("Installation en cours...")
    # Installation d'apache sur le systeme
    result = os.system("sudo apt install apache2")
    check_result(result)
    print("Installation finie !")


def install_ssh():
    print("Installation en cours...")
    # Installation du serveur ssh
    result = os.system("sudo apt install ssh")
    check_result(result)
    # Generation d'une clef ssh par default
    print("Generation d'une clef ssh...")
    result = os.system("ssh-keygen")
    check_result(result)


def change_hostname():
    print("change_hostname")
    # Demande a l'utilisateur de choisir un hostname
    new_hostname = input("Choissez votre hostname: ")
    result = os.system("sudo hostname " + new_hostname )
    check_result(result)

def menu():
   # Association des options du menu avec leur fonction respective
    options = {
        1: ("Installer un server web", install_web),
        2: ("Installer un server ssh", install_ssh),
        3: ("Changer le hostname", change_hostname),
        0: ("Quitter", None)
    }
    print("Veuillez choisir une option:\n")
    # Affichage du menu
    for nb, option in options.items():
        print("{}. {}".format(nb, option[0]))
    print("") # Affiche une ligne vide

    value = None
    # Gestion du choix de l'utilisateur
    while value is None:
        value = input("Choisissez une option: ")
        # Gestion d'erreur
        try:
            value = int(value)
            # Verification que loption existe
            if value not in options.keys():
                print("{} option invalide".format(value))
                value = None
        except ValueError:
            print("{} n'est pas un chiffre".format(value))
            value = None
    print("Vous avez choisi: {}".format(options[value][0]))
    # Recuperation de la fonction choisie
    function = options[value][1]
    if function is None:
        print("Au revoir")
        return
    # Execution de la fonction
    function()
    print("")
    menu()

print("Bienvenue dans le script dinstallation")
# Ouverture du menu
menu()
