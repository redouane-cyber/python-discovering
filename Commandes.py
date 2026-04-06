commandes= {
    "client 1" : {
        "clavier":{ "quantite" : 3 , "prix": 20 } ,
          "ecran":{ "quantite" : 1 , "prix": 150 }} 
    ,  "client 2" : {
        "clavier":{ "quantite" : 6 , "prix": 20 } ,
          "Souris":{ "quantite" : 5 , "prix": 15 }} , 
"client 3" : {"chargeur":{ "quantite" : 1 , "prix": 80 } , "Casque":{ "quantite" : 5 , "prix": 15 }}}
# print(cammandes)
client=input("entrez le nom du client a afficher : ")
if client in commandes :
    print("commande de " , client , ":")
    for produit , details in commandes[client].items() :
        print( produit,"-quantite :", details["quantite"] ," -prix : " , details["prix"] )
    else :
        print(f"le client {client} n'a pas de commandes .")
#le total
print("\n montant total par client : ")
for nom_client , produits in commandes.items():
    total = 0
    for details in produits.values():
        total += details["quantite"] * details["prix"]
        print( nom_client , " : " , total , "euro")
# ajouter un nouvelle produit
print(" \n Ajout d'un produit pour client 1 ")
commandes["client 1"]["disque dur"] = { "quantite" : 5 , "prix" : 30}
# affichage de la resulat
print(commandes)