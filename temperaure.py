#creation des listes
temperature = [100,3,6,1000,200]
#temperature max et min
temp_max=max(temperature)
temp_min=min(temperature)
# temperature moyenne
moyenne=sum(temperature)/len(temperature)
# nombre des jours au dessous de la moyenne
jours_en_dessous=0
for t in temperature :
    if t < moyenne :
        jours_en_dessous += 1
#Remplacer la temperature du 3eme jour par 25
temperature[2] = 25
#affichage 
print("temperature la plus elevee : " , temp_max)
print("temperature la plus basse : " , temp_min)
print("tenperature moyenne" , round(moyenne , 2))
print("Nombre de jours en dessous de la moyenne : " , jours_en_dessous)
print( "Nouvelle liste des temperature : " , temperature)