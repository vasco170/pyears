#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

import getopt, sys, ipaddress, os
from ftplib import FTP


def aide():
    print("\n###################################################################################\n")
    print("     -d, --dictionnaire          Dictionaire de mots de passe à utiliserl pour l'attaque")
    print("     -h, --help                  Afficher cet aide pour utiliser l'outil")
    print("     -p, --protocole             Protocole sur lequel lancer l'attaque")
    print("     -u, --utilisateur           Utilisateur avec lequel on lance l'attaque")
    print("\n###################################################################################\n")

def is_protocole(protocole):
    protocole_list = [('ssh','22'),('ftp','21'),('http','80'),('https','443')]
    for nom_protocole, num_protocole  in protocole_list:
        if (protocole.lower()==nom_protocole or protocole.lower()==num_protocole):
            return int(num_protocole)
    print("\nLe protocole renseigné n'est pas pris en charge. Utiliser la commande -help ou -h pour plus de details. Merci.")
    return False

def is_chemin_fichier(chemin):
    try:
        if (os.path.isfile(chemin)):
            return True
    except FileNotFoundError:
        print("\nLe fichier specifie est introuvable ou l'utilisateur n'a pas les droits de lecture.")
        return False

def is_cible(cible):
    try:
        _cible = ipaddress.IPv4Address(cible)
        return True
    except ValueError:
        print("\nLa cible n'est pas une Addresse IPv4.")
        return False

def is_utilisateur(cible):
    if " " in cible:
        return False
    else:
        return True

def main():
    try:
        """ Ref :
        https://docs.python.org/2/library/getopt.html
        https://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/scripts_and_streams/command_line_arguments.php
        """
        # pour les drapeaux suivis d'un : comme c:, cela veut dire que l'on attend un argument derrière l'option. 
        opts, args = getopt.getopt(sys.argv[1:], "hp:s:u:", ["chemin=","cible=","help","protocole=","sortie=","utilisateur="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print (err)  # will print something like "option -a not recognized"
        aide()
        sys.exit(2)

    for option, argument in opts:
        # On a un tuples (opts) contenant l'option et l'argument.
        if option in ("-h", "--help"):
            aide()
            sys.exit()

        elif option == "--chemin":
            etat_chemin = is_chemin_fichier(argument)
            if etat_chemin != True:
                aide()
                sys.exit()
            else:
                chemin = argument

        elif option == "--cible":
            etat_cible = is_cible(argument)
            if etat_cible != True:
                aide()
                sys.exit()
            else:
                cible = argument

        elif option in ("-u","--utilisateur"):
            etat_utilisateur = is_utilisateur(argument)
            if etat_utilisateur != True:
                aide()
                sys.exit()
            else:
                utilisateur = argument

        elif option in ("-p", "--protocole"):
            etat_protocole = is_protocole(argument)
            if etat_protocole == False:
                aide()
                sys.exit()
            else:
                 protocole = etat_protocole

    print(protocole)

if __name__ == "__main__":
    main()
