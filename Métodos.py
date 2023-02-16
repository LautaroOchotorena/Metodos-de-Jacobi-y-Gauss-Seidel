#! /usr/bin/env python3

import random

import numpy as np

from numpy import linalg

#Limitaciones de estas funciones (de este script): 

#No reordena las filas para que la matriz no tenga ceros en la diagonal,

#No reordena filas para acelerar convergencia

#No saca el espectro de los métodos, no te dirá si los métodos convergen o no

#Estas cosas se podrían agregar mediante el uso de algunas librerias



#---------------------------------Funciones-----------------------------------------

#A es la matriz

#b es el vector resultante

#Inicial es la estimación inicial para empezar a iterar

#tol es la tolerancia

#iter_max la cantidad de iteraciones máxima

#dim es la dimensión de la matriz A

def Jacobi(A,b,Inicial,tol,iter_max):		#Método de Jacobi
	A = np.array(A)
	b = np.array(b)
	#Para corroborar que la matriz sea cuadrada y que el vector b tenga la dimensión requerida
	if (A.shape[0]!= A.shape[1]) or (A.shape[0]!=len(b)):
		print("La matriz A no es cuadrada o el vector b no tiene la dimensión requerida \n")
		return
	else:
		dim = A.shape[0]
	x = Inicial[:]
	y = [0]*dim
	z = [0]*dim
	for t in range(iter_max):		#Iterar hasta que se cumple el máximo de iteraciones
		for i in range(dim):
			suma = 0 				#Seteo en 0 la suma de cada y[i]
			for j in range(dim):
				if i != j:
					suma += A[i][j]*x[j]
			y[i] = (1/A[i][i])*(-suma+b[i])
			z[i] = x[i]-y[i]		#Para ver si la resta de estos vectores llega a cumplir la tolerancia
		for i in range(dim):
			x[i] = y[i]
		if tol>linalg.norm(z, dim):		#Si uno quiere la norma infinito reemplazar esta linea por linalg.norm(z, np.inf)
			print('La respuesta con el método de Jacobi es: \n',x)
			print('El número de iteraciones usadas fue de', t)
			return()
	print('Se superó el límite de iteraciones con el método de Jacobi \n')
def GaussSeidel(A,b,Inicial,tol,iter_max):
	A = np.array(A)
	b = np.array(b)
	#Para corroborar que la matriz sea cuadrada y que el vector b tenga la dimensión requerida
	if (A.shape[0]!= A.shape[1]) or (A.shape[0]!=len(b)):
		print("La matriz A no es cuadrada o el vector b no tiene la dimensión requerida \n")
		return
	else:
		dim = A.shape[0]
	x = Inicial[:]
	y = [0]*dim
	z = [0]*dim
	for t in range(iter_max):		#Iterar hasta que se cumple el máximo de iteraciones
		for i in range(dim):
			suma = 0 				#Seteo en 0 la suma de cada y[i]
			for j in range(dim):
				if i != j:
					if j<i:
						suma += A[i][j]*y[j]
					else:
						suma += A[i][j]*x[j]
			y[i] = (1/A[i][i])*(-suma+b[i])
			z[i] = x[i]-y[i]
		for i in range(dim):
			x[i] = y[i]
		if tol>linalg.norm(z, dim):		#Si uno quiere la norma infinito reemplazar esta linea por linalg.norm(z, np.inf)
			print ('La respuesta con el método Gauss-Seidel es \n', x)
			print('El número de iteraciones usadas fue de', t)
			return()
	print('Se superó el límite de iteraciones con el método de Gauss-Seidel \n')
def mostrar(A,b):
  A = np.array(A)
  print("A = \n", A)
  print('\nb = ', b, '\n')