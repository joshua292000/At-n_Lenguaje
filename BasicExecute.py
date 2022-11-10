import os
import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import*


Resultado=""

class BasicExecute():
	

	def __init__(self, tree, env):
		self.env = env
		result = self.walkTree(tree)
		if result is not None and isinstance(result, int):
			print("es integer",result)
			global Resultado
			Resultado = str(result) + '\n'
								

		if isinstance(result, str) and result[0] == '"':
			print("es string",result)
			Resultado+=result + '\n'
			
		print("salgo ", Resultado)

	def walkTree(self, node):
		global Resultado

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

		if node[0] == 'num':
			return node[1]

		if node[0] == 'str':
			return node[1]

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

		if node[0] == 'var':
			try:
				return self.env[node[1]]
			except LookupError:
				print("Undefined variable '"+node[1]+"' found!")
				return 0

		if node[0] == 'for_loop_setup':
			valores = []

			for x in range(1,self.walkTree(node[2])):
				valores.append(x)
			print(valores)
			Resultado+=str(valores) + '\n'
			return valores

