import Métodos

A = [[3, -1, 1], 		#Matriz

	 [3, 6, 2],

	 [3, 3, 7]]

b = [1,0,4]		#Vector resultante

Inicial = [0,0,0] 	#Estimación inicial

Métodos.mostrar(A,b)

Métodos.Jacobi(A,b,Inicial,10**(-3),20)

print('')

Métodos.GaussSeidel(A,b,Inicial,10**(-3),20)

print('\n')





A = [[10, -1, 2, 0], 

	[-1, 11, -1, 3],

	[2, -1, 10, -1],

	[0, 3, -1, 8]]

b = [6, 25, -11, 15]

Inicial = [0,0,0,0]

Métodos.mostrar(A,b)

Métodos.Jacobi(A,b,Inicial,10**(-3),20)

print('')

Métodos.GaussSeidel(A,b,Inicial,10**(-3),20)

print('\n')





#Este sistema es para ver si con matrices más grandes sigue funcionando

A = [[14, -1, 2, 0, 4, 0, 2, 3], 

	[-1, 20, -1, 3, 5, 2, 1, 0],

	[2, -1, 40, -1, 2, 1, 0, 9],

	[0, 3, -1, 15, 0, 6, 1, 0],

	[0, 0, 0, 4, 10, 2, 0, 0],

	[0, 2, 0, 0, 4, 10, 2, 0],

	[0, 0, 0, 0, 4, 0, 8, 0],

	[0, 6, 0, 6, 4, 6, 1, 25]]

b = [0, 0, 0, 1, 2, 4, 6, 2]

Inicial = [0]*8

Métodos.mostrar(A,b)

Métodos.GaussSeidel(A,b,Inicial,10**(-4),20)

print('\n')





#Este sistema está como uno de los ejercicios del libro

A = [[2, -1, 1],

	[2, 2, 2],

	[-1, -1, 2]]

b = [-1, 4, -5]

Inicial = [0]*3

Métodos.mostrar(A,b)

Métodos.GaussSeidel(A,b,Inicial,10**(-5),25)

print('')

Métodos.Jacobi(A,b,Inicial,10**(-5),25)

#Probar una matriz no cuadrada
A = [[2, -1, 1],

	[2, 2, 3]]

b = [-1, 4, -5]

Inicial = [0]*3

Métodos.mostrar(A,b)

Métodos.GaussSeidel(A,b,Inicial,10**(-5),25)

#Probar una matriz A con vector b de dimensión no correspondida
A = [[2, -1, 1],

	[2, 2, 2],

	[-1, -1, 2]]

b = [-1, 4]

Inicial = [0]*3

Métodos.mostrar(A,b)

Métodos.GaussSeidel(A,b,Inicial,10**(-5),25)