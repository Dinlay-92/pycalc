def calculator():
	a = int(input("Veuillez choisir la premiere valeur : \n"))
	b = int(input("Veuillez choisir la deuxieme valeur : \n"))
	fonction = input("Veuillez chosir le mode opérateur :\n s(somme) \n m(multiplication) \n d(division) \n di(difference) \n choix :")
	if fonction == "s" :
		print("resultat : ",a+b)
	elif fonction == "m" :
		print("resulat : ",a*b)
	elif fonction == "d" :
		print("resulat : ",a/b)
	elif fonction == "di" :
		print("resulat : ",a-b)
	else:
		print("Opérateur inexistant")

calculator()