from sly import Lexer

NumLinea =0

class BasicLexer(Lexer):
	tokens = { NAME, NUMBER,FLOAT,BOOLEAN, STRING, PARA, ENTONCES, HASTA, SI, SINO, SUM, RES, MUL, DIV, IMPRIMA,
	MAYORQUE, MENORQUE, MAYORIGUAL, MENORIGUAL, IGUAL, MIENTRAS, AGREGAR, CASOS, ES, HAGA, INICIO, FIN, Y, O, N}
	ignore = '\t '
	literals = { '=', '[',']',
				'(', ')', ',', ';'}


	INICIO = r'INICIO'
	IMPRIMA = r'IMPRIMA'
	Y=r'Y'
	O=r'O'
	N=r'N'
	FIN = r'FIN'
	SUM = r'SUM'
	RES = r'RES'
	MUL =r'MUL'
	DIV = r'DIV'
	MIENTRAS = r'MIENTRAS'
	PARA = r'PARA'
	ENTONCES = r'ENTONCES'
	HASTA = r'HASTA'
	SINO = r'SINO'
	SI = r'SI'
	MAYORIGUAL = r'>='
	MENORIGUAL = r'<='
	MAYORQUE =r'>'
	MENORQUE = r'<'
	IGUAL = r'==='
	AGREGAR = r'AGREGAR'
	CASOS= r'CASOS'
	ES= r'ES'
	HAGA = r'HAGA'
	

	@_(r'FALSE|TRUE')
	def BOOLEAN(self, t):
		if t.value == 'FALSE':
			t.value = bool(False)
		elif t.value == 'TRUE':
			t.value = bool(True)
		return t

	STRING = r'\".*?\"'


	@_(r'[+-]?[0-9]+\.[0-9]+')
	def FLOAT(self, t):
		t.value = float(t.value)
		return t

	@_(r'\d+')
	def NUMBER(self, t):
		t.value = int(t.value)
		return t

	@_(r'//.*')
	def COMMENT(self, t):
		pass


	NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

	@_(r'\n+')
	def newline(self, t):
		global NumLinea
		self.lineno = t.value.count('\n')
		NumLinea += self.lineno
	
	def error(self, t):
		self.index +=1		