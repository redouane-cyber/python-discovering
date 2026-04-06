# liste vide
taches =[]
# ajouter les taches
taches.append("faire les courses")
taches.append("envoie un mail")
taches.append(" Etudier")
taches.append(" Nettoyer la maison")
# affichage
print("liste des taches : " , taches)
# recherche d'une tache 
recherche=input("entrez la taches a rechercher : ")
if recherche in taches :
    print(f"la taches {recherche} est a la position ",taches.index(recherche))
else :
    print("la tache n'est pas dans la listes")
#insertion d'une nouveau tache
nouvelle_tache = input("entrez une nouvelle taches a ajouter : ")
position=int(input(f" A quelle position sohaitez vous ajouter la tache ( entre 0 et {len(taches)}) ? "))
taches.insert(position , nouvelle_tache)
# affichage final
print(" liste mise a jour des taches : " , taches)