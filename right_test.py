import droite

q1 = input("Qu'avez vous? (tapez le chiffre correspondant)\n1: 2 droites\n2: 1 point et 1 droite\n3: 2 points\n4: 1 droite\n")

if(q1 == '1'):
	print('Equation de la première droite')
	a1 = int(input('Entrez le a: '))
	b1 = int(input('Entrez le b: '))
	c1 = int(input('Entrez le c: '))
	d1 = (a1, b1, c1)
	print('Equation de la deuxième droite:')
	a2 = int(input('Entrez le a: '))
	b2 = int(input('Entrez le b: '))
	c2 = int(input('Entrez le c: '))
	d2 = (a2, b2, c2)
	q2 = input("Que cherchez vous ?\n1: Le déterminant ?\n2: Sont-elles parallèles ?\n")
	if(q2 == '1'):
		det = droite.determinant(d1, d2)
		print('Le déterminant est:', det)
		if(det == 0):
			q3 = input("Voulez vous savoir si elles sont parallèles confondues ?\n1: Oui\n2: Non\n")
			if(q3 == '1'):
				conf = droite.confondues(d1, d2)
				if(conf == True):
					print('Ce sont des droites parallèles confondues')
					print("Je m'arrête ici")
				else:
					print('Ce sont des droites parallèles distinctes')
					print("Je m'arrête ici")
			else:
				print("Je m'arrête ici alors")
		else:
			q4 = input("Voulez vous savoir le point d'intersection de ces deux droites ?\n1: Oui\n2: Non\n")
			if(q4 == '1'):
				inter = droite.intersection(d1, d2)
				print("Le point d'intersection est: ", inter)
				print("Je m'arrête ici")
			elif(q4 == '2'):
				print("Je m'arrête ici")
			else:
				print("Erreur, je m'arrête ici")
	elif(q2 == '2'):
		para = droite.paralleles(d1, d2)
		if(para == True):
			print("Les deux droites sont parallèles")
			print("Je m'arrête ici")
		else:
			print("Les deux droites ne sont pas parallèles")
			print("Je m'arrête ici")
	else:
		print("Erreur, je m'arrête ici")
elif(q1 == '2'):
	print("Equation de la droite:")
	a = int(input('Entrez le a: '))
	b = int(input('Entrez le b: '))
	c = int(input('Entrez le c: '))
	d = (a, b, c)
	print("Coordonnées du point:")
	x = int(input("Entrez le x: "))
	y = int(input("Entrez le y: "))
	p = (x, y)
	q5 = input("Que voulez vous ?:\n1: Vérifiez si le point appartient à la droite\n2: Une droite normale à la droite donnée passant par le point donné\n3: La symétrie orthogonale, où l'axe est la droite donné, du point donné\n4: La distance entre le point donné et la droite donnée\n")
	if(q5 == '1'):
		appar = droite.appartient(d, p)
		if(appar == True):
			print("Le point appartient à la droite")
			print("Je m'arrête ici")
		else:
			print("Le point n'appartient pas à la droite")
			print("Je m'arrête ici")
	elif(q5 == '2'):
		dNor = droite.droiteNormale(d, p)
		print("Le a, le b et le c de la droite normales sont: ", dNor)
		print("Je m'arrête ici")
	elif(q5 == '3'):
		sym = symetrieOrthogonale(d, p)
		print("Le point image par la symétrie orthogonale est: ", sym)
		print("Je m'arrête ici")
	elif(q5 == '4'):
		distance = distanceDroitePoint(d, p)
		print("La distance entre le point et la droite est: ", distance)
		print("Je m'arrête ici")
	else:
		print("Erreur, je m'arrête ici")
elif(q1 == '3'):
	print("Coordonnées du point 1:")
	x1 = int(input("Entrez le x: "))
	y1 = int(input("Entrez le y: "))
	p1 = (x1, y1)
	print("Coordonnées du point 2:")
	x2 = int(input("Entrez le x: "))
	y2 = int(input("Entrez le y: "))
	p2 = (x2, y2)
	print("La seule option disponible est la droite passant par les deux points données")
	d = droite.droite(p1, p2)
	print("Le a, le b et le c de cette droite sont: ", d)
	print("Je m'arrête ici")
elif(q1 == '4'):
	print('Equation de la droite:')
	a = int(input('Entrez le a: '))
	b = int(input('Entrez le b: '))
	c = int(input('Entrez le c: '))
	d = (a, b, c)
	q6 = input("Que voulez vous ?\n1: La pente de la droite\n2: L'intersection avec l'axe des abscisses")
	if(q6 == '1'):
		m = droite.coefficientAngulaire(d)
		print("La pente de la droite est: ", m)
		print("Je m'arrête ici")
	elif(q6 == '2'):
		p = droite.intersectionAbscisses(d)
		print("L'intersection de la droite avec l'axe des abscisses est le point: ", p)
		print("Je m'arrête ici")
	else:
		print("Erreur, je m'arrête ici")
else:
	print("Erreur, je m'arrête ici")