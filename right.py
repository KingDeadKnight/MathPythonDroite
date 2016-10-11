import math
def droite(p1, p2):
	(x1, y1) = p1
	(x2, y2) = p2
	dir1 = x2-x1
	dir2 = y2-y1
	#vDir = (dir1, dir2)
	#vNor = (-dir2, dir1)
	a = -dir2
	b = dir1
	c = a*x1 + b*y1
	if(x1==x2 and y1==y2):
		return None
	else:
		return (a, b, c)

def appartient(d, p):
	(a, b, c) = d
	(x, y) = p
	if(c == a*x + b*y):
		return True
	else:
		return False

def paralleles(d1, d2):
	(a1, b1, c1) = d1
	(a2, b2, c2) = d2
	det = int(a1*b2 - a2*b1)
	if(det == 0):
		return True
	else:
		return False

def intersection(d1, d2):
	(a1, b1, c1) = d1
	(a2, b2, c2) = d2
	det = a1*b2 - a2*b1
	if(det == 0):
		return None
	else:
		x = (c1*b2 - b2*c1)/det
		y = (a1*c2 - c1*a2)/det
		return (x, y)

def droiteNormale(d, p):
	(x, y) = p
	(a, b, c) = d
	#vNor = (a ,b)
	#dNor = (-b, a)
	c1 = -b*x + a*y
	return (-b, a, c1)

def symetrieOrthogonale(d, p):
	(x, y) = p
	(a, b, c) = d
	d1 = droiteNormale(d, p)
	q = intersection(d, d1)
	(x1, y1) = q
	vecteur1 = x1 - x
	vecteur2 = y1 - y
	#(vecteur1, vecteur2) = vecteurPQ
	sym1 = x1 + vecteur1
	sym2 = y1 + vecteur2
	sym = (sym1, sym2)	
	return sym

def distanceDroitePoint(d, p):
	(x, y) = p
	(a, b, c) = d
	d1 = droiteNormale(d, p)
	q = intersection(d, d1)
	(x1, y1) = q
	vecteur1 = x1 - x
	vecteur2 = y1 - y
	norme = math.sqrt(vecteur1**2 + vecteur2**2)
	return norme

def confondues(d1, d2):
	(a1, b1, c1) = d1
	(a2, b2, c2) = d2
	det = a1*b2 - a2*b1
	vD1 = (-b1, a1)
	vD2 = (-b2, a2)
	if(det != 0):
		return False
	else:
		if(a1 == a2 and b1 == b2 and c1 == c2):
			return True
		elif(c1/b1 == c2/b2 or b1/c1 == b2/c2):
			return True
		else:
			return False
			
def droiteParallele(d, p):
	(a, b, c) = d
	(x, y) = p
	c1 = x*-b + y*a
	return (a, b, c1)
	'''Erreur de 2 possible pour c1'''
	
def coefficientAngulaire(d):
	(a, b, c) = d
	if(b == 0):
		return None
	else:
		m = -a/b
		return m

def intersectionAbscisses(d):
	(a, b, c) = d
	if(a == 0):
		return "Pas d'intersection"
	else:
		return c/a, 0

def determinant(d1, d2):
	(a1, b1, c1) = d1
	(a2, b2, c2) = d2
	det = (a1*b2) - (a2*b1)
	return det