from sly import Lexer

class BasicLexer(Lexer):
	tokens = { NAME, NUMBER, STRING, PARA, ENTONCES, HASTA, SI, SINO, SUM, RES, MUL, DIV, 
	MAYORQUE, MENORQUE, MAYORIGUAL, MENORIGUAL, IGUAL, MIENTRAS, AGREGAR, CASOS, ES, HAGA, INICIO, FIN}
	ignore = '\t '
	literals = { '=', '[',']',
				'(', ')', ',', ';'}


	# Define tokens as regular expressions
	# (stored as raw strings)
	INICIO = r'INICIO'
	FIN = r'FIN'
	SUM = r'SUM'
	RES = r'RES'
	MUL =r'MUL'
	DIV = r'DIV'
	MIENTRAS = r'MIENTRAS'
	PARA = r'PARA'
	ENTONCES = r'ENTONCES'
	HASTA = r'HASTA'
	SI = r'SI'
	SINO = r'SINO'
	STRING = r'\".*?\"'
	MAYORQUE = r'>'
	MENORQUE = r'<'
	MAYORIGUAL = r'=>'
	MENORIGUAL = r'<='
	IGUAL = r'==='
	AGREGAR = r'AGREGAR'
	CASOS= r'CASOS'
	ES= r'ES'
	HAGA = r'HAGA'
	# Number token
	@_(r'\d+')
	def NUMBER(self, t):
		
		# convert it into a python integer
		t.value = int(t.value)
		return t

	# Comment token
	@_(r'//.*')
	def COMMENT(self, t):
		pass


	NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

	# Newline token(used only for showing
	# errors in new line)
	@_(r'\n+')
	def newline(self, t):
		self.lineno = t.value.count('\n')
	
