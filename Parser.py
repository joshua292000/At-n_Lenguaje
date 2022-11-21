# SLY (Sly Lex-Yacc)

# Copyright (C) 2016-2019
# David M. Beazley (Dabeaz LLC)
# All rights reserved.

from sly import Parser
from Lexer import BasicLexer


class BasicParser(Parser):
	#tokens are passed from lexer to parser
	tokens = BasicLexer.tokens

	precedence = (
		('left', SUM, RES),
		('left', MUL, DIV),
		('right', 'UMINUS'),
	)

	def __init__(self):
		self.env = { }

	@_('')
	def statement(self, p):
		pass

	@_('var_assign')
	def statement(self, p):
		return p.var_assign


	@_('NAME "=" expr')
	def var_assign(self, p):
		return ('var_assign', p.NAME, p.expr) 

	@_('NAME "=" STRING')
	def var_assign(self, p):
		return ('var_assign', p.NAME, p.STRING)


	@_('expr')
	def statement(self, p):
		return (p.expr)

	@_('INICIO')
	def expr(self, p):
		return None

	@_('FIN')
	def expr(self, p):
		return None


	@_('expr SUM expr')
	def expr(self, p):
		return ('add', p.expr0, p.expr1)

	@_('expr RES expr')
	def expr(self, p):
		return ('sub', p.expr0, p.expr1)

	@_('expr MUL expr')
	def expr(self, p):
		return ('mul', p.expr0, p.expr1)

	@_('expr DIV expr')
	def expr(self, p):
		return ('div', p.expr0, p.expr1)

	@_('"-" expr %prec UMINUS')
	def expr(self, p):
		return p.expr

	@_('NAME')
	def expr(self, p):
		return ('var', p.NAME)

	@_('NUMBER')
	def expr(self, p):
		return ('num', p.NUMBER)


	@_('NAME "["  "]" ')
	def var_assign(self, p):
		return ('ArregloV', p.NAME) 


	@_('NAME "[" expr "]" ')
	def var_assign(self, p):
		return ('Arreglo', p.NAME, p.expr) 
	
	@_('NAME "[" expr "," expr "]" ')
	def var_assign(self, p):
		return ('Arreglo2', p.NAME, p.expr0, p.expr1) 

	@_('NAME "[" expr "," expr "," expr "]" ')
	def var_assign(self, p):
		return ('Arreglo3', p.NAME, p.expr0, p.expr1, p.expr2) 

	@_('NAME "[" STRING "]" ')
	def var_assign(self, p):
		return ('Arreglo', p.NAME, p.STRING) 

	@_('NAME "[" STRING "," STRING "]" ')
	def var_assign(self, p):
		return ('Arreglo2', p.NAME, p.STRING0, p.STRING1) 

	@_('NAME "[" STRING "," STRING "," STRING "]" ')
	def var_assign(self, p):
		return ('Arreglo3', p.NAME, p.STRING0, p.STRING1, p.STRING2) 
	

	@_('PARA var_assign HASTA expr ENTONCES statement')
	def expr(self,p):
		return ('for_loop_setup', p.var_assign, p.expr, p.statement)

	
	@_('PARA var_assign HASTA expr ENTONCES expr AGREGAR "(" expr ")" ')
	def expr(self,p):
		return ('forA', p.var_assign, p.expr0, p.expr1, p.expr2)

	@_('MIENTRAS expr MENORQUE expr ENTONCES statement')
	def expr(self,p):
		return ('while', p.expr0, p.expr1, p.statement)

	@_('CASOS expr ENTONCES')
	def expr(self,p):
		return ('CASOS',p.expr)

	@_('ES expr ENTONCES statement')
	def expr(self,p):
		return ('ES',p.expr, p.statement)

	@_('SI expr MAYORQUE expr ENTONCES statement')
	def expr(self,p):
		return ('if', p.expr0, p.expr1,p.statement)

	@_('SI NAME MENORQUE expr ENTONCES statement')
	def expr(self,p):
		return ('ifmenor', p.NAME, p.expr,p.statement)

	@_('HAGA NAME "("  ")" ENTONCES statement ')
	def expr(self,p):
		return ('Funcion', p.NAME, p.statement)

	@_('NAME "("  ")"')
	def expr(self,p):
		return ('LLamarFuncion', p.NAME)


	@_('HAGA NAME "(" expr "," expr ")" ENTONCES statement ')
	def expr(self,p):
		return ('Funcion2', p.NAME, p.expr0, p.expr1, p.statement)

	@_('NAME "(" expr "," expr ")"')
	def expr(self,p):
		return ('LLamarFuncion2', p.NAME, p.expr0, p.expr1)