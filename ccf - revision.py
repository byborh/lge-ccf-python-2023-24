import random

def matrice():
	return [[0 for i in range(6)] for j in range(7)]

def matriceAleatoire():
	return [[random.randint(0,101) for i in range(6)] for j in range(7)]

def matriceCarre():
	return [[0 for i in range(8)] for j in range(8)]

def matriceCarreAleatoire():
	return [[random.randint(0,101) for i in range(6)] for j in range(6)]

def matriceImage(n):
	return [[random.randint(0, 256) for i in range(n)] for j in range(n)]

def afficher(M):
	for i in M:
		print(i)

def contours(M):
	l = len(M)
	for i in range(l):
		for j in range (i):
			M[i][0] = 1
			M[i][-1] = 1
			M[0][j] = 1
			M[-1][j] = 1
	return M

def diagonal(M):
	l = len(M)
	for i in range(l):
		M[i][i] = 1
		M[i][l-1-i] = 1
	return M

def contoursPlusDiagonal(M):
	l = len(M)
	for i in range(l):
		M[i][i] = 1
		M[i][l-1-i] = 1
		M[i][0] = 1
		M[i][-1] = 1
		M[0][i] = 1
		M[-1][i] = 1
	return M

def sommeDiagonal(M):
	somme = 0
	for i in range(len(M)):
		somme += M[i][i]
	return somme

def moyenne(M): # La moyenne des valeurs d'une matrice
	s = 0
	l = len(M)
	for i in range(l):
		for j in range(l):
			s += M[i][j]
	return s / (l*len(M[0]))

def floutage(M):
	copie_M = [i[:] for i in M]
	n = len(M)
	for i in range(n):
		for j in range(1, n - 1):
			copie_M[i][j] = (M[i][j-1] + M[i][j+1]) / 2
	return copie_M


def compter_pixel(M):
	n = len(M)
	blanc = 0
	noir = 0
	for i in range(n):
		for j in range(i):
			if(M[i][j] == 0):
				blanc += 1
			if(M[i][j] == 255):
				noir += 1
	return "nombre de blanc : ", blanc, "nombre de noir : ", noir

def Matcontraste(M, m):
	nouvelle_M = []
	nouvelle_M.append(M)
	for i in range(len(M)):
		nouvelle_ligne = []
		for j in range(len(M[i])):
			valeur = M[i][j]

			if(valeur < m):
				n = int(valeur * 0.8)
			else:
				n = int(valeur * 1.2)

			if(n > 100):
				n = 100

			nouvelle_ligne.append(n)
		nouvelle_M.append(nouvelle_ligne)
	return nouvelle_M



def init2():
	M = [[random.randint(0,101) for i in range(7)] for i in range(6)]
	for i in range(len(M)):
		M[i][0] = 0
		M[i][-1] = 0
	return M


def tour(M, lig, col):
	for i in range(len(M)):
		for j in range(len(M[i])):
			M[lig][j] = 1
			M[i][col] = 1
	M[lig][col] = 2
	return M

def fous(M, lig, col):
	for i in range(len(M)):
		for j in range(len(M[i])):
			if(i+j == lig+col or i-j == lig-col):
				M[i][j] = 1
	M[lig][col]=3
	return M

def reine(M,lig,col):
	for i in range(len(M)):
		for j in range(len(M[i])):
			if(i+j == lig+col or i-j == lig-col):
				M[i][j] = 1
			M[lig][j] = 1
			M[i][col] = 1
	M[lig][col] = 4
	return M

def pion(M, lig, col):
	M[lig][col]=5
	if(M[lig][col] == M[-2][col]):
		M[lig-2][col]=1
	M[lig-1][col]=1
	return M


afficher(pion(matriceCarre(), 5, 5))

#print(floutage(matriceCarreAleatoire()))
#afficher(matriceCarreAleatoire())
#print('devient :')
#afficher(floutage(matriceCarreAleatoire()))
#afficher(Matcontraste(matriceAleatoire(), 50))
#afficher(compter_pixel(matriceImage(7)))

