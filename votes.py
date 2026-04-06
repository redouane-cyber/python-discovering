# liste des votes
votes = ["najat" , "redouane" , "ossama" , "najat" , "redouane" , "najat" , "ossama" , "redouane" , "ossama" , "najat"]
# dictionaire pour compter les votes
resultat ={}
for nom in votes :
    if nom in resultat :
        resultat[nom] +=1
    else :
        resultat[nom] =1
#candidat avec les plus des votes
candidat_max=max(resultat , key=resultat.get)
#affichage
print("resultats des votes : " , resultat)
print("le condidat avec le plus de votes est : " , candidat_max , "avec" , resultat[candidat_max] , "votes")