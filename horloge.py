import time

# 1er Janvier 1970 à 00h00

"""
                localtime()
(TIMESSTAMP)------------------> structure de temps
            <-----------------
                mktime()
"""



"""
%d : jour (01 à 31)
%m : mois (01 à 12)
%Y : année(ex : 2023) - %y(00 à 99)
%H : heures (00 à 23)
%M : minutes (00 à 59)
%S : secondes (00 à 59)
%I :12h
%p : AM/PM

%A :jour semaine / %a (jour abrégé)
%B : mois / %b (mois abrégé)
%Z : fuseau horaire timezone
"""
"""
tuple parametre
time.sleep()
    .time()
    .localtime()
    .mktime()
    .strftime()

Création de tuple : mon_tuple = ()#Vide
                    mon_tuple = 17, #Une seul valeur
                    mon_tuple = (17,) #Idem qu'au-dessus
                    mon_tuple = (4,6) #Plusieurs valeurs

Accés aux valeur : mon_tuple[x]        #Valeur d'indice X




import time
import threading

def afficher_heure():
    heure_actuelle = time.localtime()
    heure_formattee = time.strftime("%H:%M:%S",heure_actuelle)
    print(heure_formattee, end='\r')

def afficher_heure(heures, minutes, secondes):
    if heures < :



try:
    while True:
        afficher_heure()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nArrêt du programme.")

"""





import time

# Fonction pour afficher l'heure au format hh:mm:ss
def afficher_heure(heure):
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format, end="\r")  # Le \r permet de mettre à jour la ligne actuelle dans la console

# Fonction pour régler l'heure
def regler_heure(heures, minutes, secondes):
    return (heures, minutes, secondes)

# Fonction pour régler l'alarme
def regler_alarme(heures, minutes, secondes):
    return (heures, minutes, secondes)

# Fonction pour vérifier et afficher l'alarme
def verifier_alarme(heure_actuelle, alarme):
    if heure_actuelle == alarme:
        print("\nWAKE UP !")
        time.sleep(5)


def regler_heure_affichee(heure):
    afficher_heure(heure)

# Programme principal
if __name__ == "__main__":
    # Initialisation de l'heure et de l'alarme
    heure_actuelle = regler_heure(16, 59, 50)
    alarme = regler_alarme(17, 0, 0)

    try:
        while True:
            afficher_heure(heure_actuelle)
            verifier_alarme(heure_actuelle, alarme)
            time.sleep(1)  # Pause d'une seconde
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)

            # Si les secondes atteignent 60, réinitialiser les secondes et ajouter une minute
            if heure_actuelle[2] == 60:
                heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)

            # Si les minutes atteignent 60, réinitialiser les minutes et ajouter une heure
            if heure_actuelle[1] == 60:
                heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])

            # Si les heures atteignent 23, réinitialiser les heures
            if heure_actuelle[0] == 23:
                heure_actuelle = (0, heure_actuelle[1], heure_actuelle[2])

    except KeyboardInterrupt:
        print("\nArrêt du programme.")
