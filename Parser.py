
from sly import Parser
from Lexer import BasicLexer
import Lexer as lex
ErrorT=""
class BasicParser(Parser):
	tokens = BasicLexer.tokens

	precedence = (
		('left', SUM, RES),
		('left', MUL, DIV),
		('right', 'UMINUS'),
	)

	def __init__(self):
		self.env = { }

	def error(self, p):
			global ErrorT	
			if p:
		
				ErrorT= ErrorT + "Error de sintaxis en el token = "+ p.type+", en la linea "+str(lex.NumLinea+1)+'\n'
	
				self.errok()
			else:
				ErrorT=ErrorT + "Error de sintaxis en EOF, en la linea "+str(lex.NumLinea+1)+'\n'
			

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

	@_('IMPRIMA NAME')
	def expr(self, p):
		return ('var', p.NAME)

	@_('BOOLEAN')
	def expr(self, p):
		return ('str', p.BOOLEAN)

	@_('NUMBER')
	def expr(self, p):
		return ('num', p.NUMBER)

	@_('FLOAT')
	def expr(self, p):
		return ('num', p.FLOAT)


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

	@_('MIENTRAS NAME MENORQUE expr ENTONCES statement')
	def expr(self,p):
		return ('while', p.NAME, p.expr, p.statement)

	@_('CASOS expr ENTONCES')
	def expr(self,p):
		return ('CASOS',p.expr)

	@_('ES expr ENTONCES statement')
	def expr(self,p):
		return ('ES',p.expr, p.statement)

	@_('SI NAME MAYORQUE expr ENTONCES statement')
	def expr(self,p):
		return ('if', p.NAME, p.expr,p.statement)


	@_('SI NAME MAYORIGUAL expr ENTONCES statement')
	def expr(self,p):
		return ('ifmayorigual', p.NAME, p.expr,p.statement)
	

	@_('SI NAME MENORQUE expr ENTONCES statement')
	def expr(self,p):
		return ('ifmenor', p.NAME, p.expr, p.statement)

	@_('SI NAME MENORIGUAL expr ENTONCES statement')
	def expr(self,p):
		return ('ifmenorigual', p.NAME, p.expr,p.statement)

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

	@_('SI NAME MAYORQUE expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelse', p.NAME, p.expr,p.statement0, p.statement1)
	
	@_('SI NAME MENORQUE expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelse2', p.NAME, p.expr,p.statement0, p.statement1)

	@_('SI NAME MENORIGUAL expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelse3', p.NAME, p.expr,p.statement0, p.statement1)

	@_('SI NAME MAYORIGUAL expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelse4', p.NAME, p.expr,p.statement0, p.statement1)

	@_('SI NAME MAYORQUE expr O NAME MENORQUE expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelsecondi', p.NAME0, p.expr0, p.NAME1, p.expr1, p.statement0, p.statement1)

	@_('SI NAME MENORQUE expr O NAME MAYORQUE expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelsecondi2', p.NAME0, p.expr0, p.NAME1, p.expr1, p.statement0, p.statement1)

	@_('SI NAME MAYORQUE expr Y NAME MENORQUE expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelsecondi3', p.NAME0, p.expr0, p.NAME1, p.expr1, p.statement0, p.statement1)

	@_('SI NAME MENORQUE expr Y NAME MAYORQUE expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelsecondi4', p.NAME0, p.expr0, p.NAME1, p.expr1, p.statement0, p.statement1)

	@_('SI NAME IGUAL expr ENTONCES statement SINO ENTONCES statement ')
	def expr(self,p):
		return ('ifelseigual', p.NAME, p.expr,p.statement0, p.statement1)

	@_('SI NAME IGUAL expr ENTONCES statement')
	def expr(self,p):
		return ('ifIGUAL', p.NAME, p.expr, p.statement)

	
	@_('NAME "[" expr "," expr "," expr "]" "[" expr "," expr "," expr "]" ')
	def var_assign(self, p):
		return ('Matriz', p.NAME, p.expr0, p.expr1, p.expr2,p.expr3, p.expr4, p.expr5) 