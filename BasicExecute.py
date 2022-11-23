import os
import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import*


Resultado=""
SWith =""
func = ""
class BasicExecute():
	

	def __init__(self, tree, env):
		self.env = env
		result = self.walkTree(tree)
		if result is not None and isinstance(result, int):
			global Resultado
			Resultado += str(result) + '\n'

		elif result is not None and isinstance(result, float):
			Resultado += str(result) + '\n'
								

		elif isinstance(result, str) and result[0] == '"':
			Resultado+=result + '\n'

		elif result is not None and isinstance(result, list):
			Resultado += str(result) + '\n'
			

	def walkTree(self, node):
		global Resultado
		global SWith
		global func
		if isinstance(node, int):
			return node
		if isinstance(node, str):
			return node

		if node is None:
			return None

		if node[0] == 'program':
			if node[1] == None:
				self.walkTree(node[2])
				
			else:
				self.walkTree(node[1])
				self.walkTree(node[2])
				
#-----------------------------------Ve si la variable es int o string---------------------------------------------
		if node[0] == 'num':
			return node[1]

		if node[0] == 'str':
			return node[1]
#-----------------------------------Busca que operacion matematica hacer-------------------------------------------
		if node[0] == 'add':
			return self.walkTree(node[1]) + self.walkTree(node[2])
		elif node[0] == 'sub':
			return self.walkTree(node[1]) - self.walkTree(node[2])
		elif node[0] == 'mul':
			return self.walkTree(node[1]) * self.walkTree(node[2])
		elif node[0] == 'div':
			return self.walkTree(node[1]) / self.walkTree(node[2])

		if node[0] == 'var_assign':
			self.env[node[1]] = self.walkTree(node[2])
			return node[1]

		
		if node[0] == 'ArregloV':
			self.env[node[1]] = []
			return node[1]


		elif node[0] == 'Arreglo':
			self.env[node[1]] = [self.walkTree(node[2])]
			return node[1]
		
		elif node[0] == 'Arreglo2':
			self.env[node[1]] = [self.walkTree(node[2]), self.walkTree(node[3])]
			return node[1]
		
		elif node[0] == 'Arreglo3':
			self.env[node[1]] = [self.walkTree(node[2]),self.walkTree(node[3]),self.walkTree(node[4])]
			return node[1]

		if node[0] == 'var':
			try:
				return self.env[node[1]]
			except LookupError:
				return 0

		if node[0] == 'for_loop_setup':
			valores = []
			valor = node[1]
			for x in range(self.walkTree(valor[2]),self.walkTree(node[2])):
				valores.append(x)
			Resultado+=str(valores) + '\n'
			return valores

		if node[0] == 'forA':
			valores = []
			valor = node[1]
			valor2 = node[3]
			for x in range(self.walkTree(valor[2]),self.walkTree(node[2])):
				self.walkTree(node[3]).append(x)
			return node[3]

		
		if node[0] == 'while':
			valoresW = []
			i=  self.env[node[1]] 
			while i < self.walkTree(node[2]):
				valoresW.append(i)
				i+=1
			
			#Resultado+=str(valoresW) + '\n'
			return valoresW


		if node[0] == 'CASOS':
			SWith =self.walkTree(node[1])
			return None
		
		if node[0] == 'ES':
			res = None
			valor = SWith
			valor2 = self.walkTree(node[1])
			if valor== valor2:
				res=self.walkTree(node[2])
			return res

		if node[0] == 'if':
			valores = []
			if self.env[node[1]]  > self.walkTree(node[2]):
				return self.walkTree(node[3])
		
		elif node[0] == 'ifmenor':
			valores = []

			if self.env[node[1]] < self.walkTree(node[2]):
				return self.walkTree(node[3])

		elif node[0] == 'ifmayorigual':
			valores = []

			if self.env[node[1]] >= self.walkTree(node[2]):
				return self.walkTree(node[3])

		elif node[0] == 'ifmenorigual':
			valores = []

			if self.env[node[1]] <= self.walkTree(node[2]):
				return self.walkTree(node[3])

		elif node[0] == 'ifIGUAL':
			valores = []

			if self.env[node[1]] == self.walkTree(node[2]):
				return self.walkTree(node[3])
		
		if node[0] == 'Funcion':
			func = node[1],node[2]

		if node[0] == 'LLamarFuncion':
			if node[1] == func[0]:
				return self.walkTree(func[1])
			else:
				return 0

				
		if node[0] == 'Funcion2':
			func = node[1],node[2],node[3],node[4]

		if node[0] == 'LLamarFuncion2':
			if node[1] == func[0]:
				gua= func[3]			
				if gua[0] == 'add':
					return self.walkTree(node[2]) + self.walkTree(node[3]) 
				elif gua[0] == 'sub':
					return self.walkTree(node[2]) - self.walkTree(node[3]) 
				elif gua[0] == 'mul':
					return self.walkTree(node[2]) * self.walkTree(node[3]) 
				elif gua[0] == 'div':
					return self.walkTree(node[2]) / self.walkTree(node[3]) 
			else:
				return 0


		if node[0] == 'ifelse':
			valores = []

			if self.env[node[1]] > self.walkTree(node[2]):
				return self.walkTree(node[3])
			else:
				return self.walkTree(node[4])

		if node[0] == 'ifelse2':
			valores = []

			if self.env[node[1]] < self.walkTree(node[2]):
				return self.walkTree(node[3])
			else:
				return self.walkTree(node[4])

		if node[0] == 'ifelse3':
			valores = []

			if self.env[node[1]] <= self.walkTree(node[2]):
				return self.walkTree(node[3])
			else:
				return self.walkTree(node[4])

		if node[0] == 'ifelse4':
			valores = []

			if self.env[node[1]] >= self.walkTree(node[2]):
				return self.walkTree(node[3])
			else:
				return self.walkTree(node[4])

		if node[0] == 'ifelseigual':
			valores = []

			if self.env[node[1]] == self.walkTree(node[2]):
				return self.walkTree(node[3])
			else:
				return self.walkTree(node[4])

		if node[0] == 'ifelsecondi':
			valores = []

			if self.env[node[1]] > self.walkTree(node[2]) or self.env[node[3]] < self.walkTree(node[4]) :
				return self.walkTree(node[5])
			else:
				return self.walkTree(node[6])

		if node[0] == 'ifelsecondi2':
			valores = []

			if self.env[node[1]] < self.walkTree(node[2]) or self.env[node[3]] > self.walkTree(node[4]) :
				return self.walkTree(node[5])
			else:
				return self.walkTree(node[6])

		if node[0] == 'ifelsecondi3':
			valores = []

			if self.env[node[1]] > self.walkTree(node[2]) and self.env[node[3]] < self.walkTree(node[4]) :
				return self.walkTree(node[5])
			else:
				return self.walkTree(node[6])

		if node[0] == 'ifelsecondi4':
			valores = []

			if self.env[node[1]] < self.walkTree(node[2]) and self.env[node[3]] > self.walkTree(node[4]) :
				return self.walkTree(node[5])
			else:
				return self.walkTree(node[6])


		if node[0] == 'Matriz':
			self.env[node[1]] = [[self.walkTree(node[2]),self.walkTree(node[3]),self.walkTree(node[4])],[self.walkTree(node[5]),self.walkTree(node[6]),self.walkTree(node[7])],]
			return node[1]
