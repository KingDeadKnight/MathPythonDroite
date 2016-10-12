import right

q1 = input("What do you have? (Tip the number of the answer)\n1: 2 rights\n2: 1 point et 1 right\n3: 2 points\n4: 1 right\n")

if(q1 == '1'):
	print('Equation of the first right')
	a1 = int(input('Enter a: '))
	b1 = int(input('Enter b: '))
	c1 = int(input('Enter c: '))
	d1 = (a1, b1, c1)
	print('Equation of the second right')
	a2 = int(input('Enter a: '))
	b2 = int(input('Enter b: '))
	c2 = int(input('Enter c: '))
	d2 = (a2, b2, c2)
	q2 = input("What do you search ?\n1: The determinant ?\n2: If they are parrallel ?\n")
	if(q2 == '1'):
		det = right.determinant(d1, d2)
		print('The determinant is:', det)
		if(det == 0):
			q3 = input("Do you want to know if they are parrallel and mingled ?\n1: Yes\n2: No\n")
			if(q3 == '1'):
				conf = right.confondues(d1, d2)
				if(conf == True):
					print('They are mingled')
					print("i'm stopping here")
				else:
					print('They are not mingled')
					print("I'm stopping here")
			else:
				print("I'm stopping here")
		else:
			q4 = input("Do yo want to know the intersection of these rights ?\n1: Yes\n2: No\n")
			if(q4 == '1'):
				inter = right.intersection(d1, d2)
				print("The intersection is: ", inter)
				print("I'm stopping here")
			elif(q4 == '2'):
				print("I'm stopping here")
			else:
				print("Error, I'm stopping here")
	elif(q2 == '2'):
		para = right.paralleles(d1, d2)
		if(para == True):
			print("They are parralels")
			print("I'm stopping here")
		else:
			print("They are not parralels")
			print("I'm stopping here")
	else:
		print("Error, I'm stopping here")
elif(q1 == '2'):
	print("Equation of the right:")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	d = (a, b, c)
	print("Coordinate of the point:")
	x = int(input("Enter x: "))
	y = int(input("Enter y: "))
	p = (x, y)
	q5 = input("What do you search ?:\n1: Check if the point is on the right\n2: A perpendicular right to the given right passing by the point\n3: The symmetry orthogonal of the point by the right\n4: The distance between the point and the right\n")
	if(q5 == '1'):
		appar = right.appartient(d, p)
		if(appar == True):
			print("The point is on the right")
			print("I'm stopping here")
		else:
			print("The point is not on the right")
			print("I'm stopping here")
	elif(q5 == '2'):
		dNor = right.rightNormale(d, p)
		print("A, b, c of the perpendicular right is: ", dNor)
		print("I'm stopping here")
	elif(q5 == '3'):
		sym = symetrieOrthogonale(d, p)
		print("The result of the symmetry is: ", sym)
		print("I'm stopping here")
	elif(q5 == '4'):
		distance = distancerightPoint(d, p)
		print("The distance is: ", distance)
		print("I'm stopping here")
	else:
		print("Error, I'm stopping here")
elif(q1 == '3'):
	print("Coordinate of the first point:")
	x1 = int(input("Enter x: "))
	y1 = int(input("Enter y: "))
	p1 = (x1, y1)
	print("Coordinate of the second point:")
	x2 = int(input("Enter x: "))
	y2 = int(input("Enter y: "))
	p2 = (x2, y2)
	print("You can only know the right passing by the points")
	d = right.right(p1, p2)
	print("A, b, c is this right is: ", d)
	print("I'm stopping here")
elif(q1 == '4'):
	print('Equation of the right:')
	a = int(input('Enter a: '))
	b = int(input('Enter a: '))
	c = int(input('Enter c: '))
	d = (a, b, c)
	q6 = input("What do you search ?\n1: The slope of the right\n2: The intersection with OX axe")
	if(q6 == '1'):
		m = right.coefficientAngulaire(d)
		print("The slope is: ", m)
		print("I'm stopping here")
	elif(q6 == '2'):
		p = right.intersectionAbscisses(d)
		print("The intersection is: ", p)
		print("I'm stopping here")
	else:
		print("Error, I'm stopping here")
else:
	print("Error, I'm stopping here")