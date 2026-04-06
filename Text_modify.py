# saisie un texte
texte = input(" entrez une phrase ou une paragraphe : ")
# Nombre total des caracteres
nb_caracteres = len(texte)
# Nombres total des mots
mots = texte.split()
nb_mots = len(mots)
# texte en majuscules
texte_maj = texte.upper()
# texte en miniscules
texte_min = texte.lower()
#recherche un caractere
caractere = input(" entrez un caractere a rechercher : ")
nb_occurence = texte.count(caractere)
# verifier la palandrome
texte_nettoye= texte.replace(" ","").lower()
est_palaindrome = texte_nettoye==texte_nettoye[ : : -1]
# affichage
print("Nombre total des caractere : ", nb_caracteres)
print("Nombre total des mots : ", nb_mots)
print(" texte en majuscule : ", texte_maj)
print(" texte en minuscule : ", texte_min)
if nb_occurence > 0 :
    print(f"le caractere '{caractere}' apparait {nb_occurence} fois dans le texte .")
else :
    print(f"le caractere '{caractere}' n'apparait pas  dans le texte .")
if est_palaindrome :
    print("le texte est palaindrome")
else :
       print("le texte n'est pas palaindrome")

