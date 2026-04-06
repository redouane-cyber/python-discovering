#creation de la salle ( 5 ranges et 4 sieges)
cinema=[]
for i in range(5):
    cinema.append([0,0,0,0,])
# reservation de la range 2 , siege 3
cinema[1][2]=1
print("la salle du cenima apres la reservation :")
for ligne in cinema :
    print(ligne)
#vefifier disponobilite de la range 4 siege 1
if cinema[3][0]==0:
    print(" la place de la range 4 siege 1 est disponible")
else :
    print(" la place de la range 4 siege 1 n'est pas disponible")
#4 compter les place libre 
place_libre = 0
for ligne in cinema :
    for place in ligne :
        if place == 0 :
            place_libre +=1
print("Nombre total des places libre : " , place_libre)
# reserver 3 place cote a cote a la range 5
cinema[4][0]=1
cinema[4][1]=1
cinema[4][2]=1
print(" Voisi la salle apres la reservation de 3 place cote a cote de la rangee 5 : ")
for ligne in cinema :
    print(ligne)




