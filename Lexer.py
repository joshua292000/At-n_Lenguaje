from sly import Lexer

class BasicLexer(Lexer):
	tokens = { NAME, NUMBER, STRING, FOR, THEN, TO, IF, ELSE, SUMA}
	ignore = '\t '
	literals = { '=', '-', '/',
				'*', '(', ')', ',', ';'}


	# Define tokens as regular expressions
	# (stored as raw strings)
	SUMA = r'SUMA'
	FOR = r'FOR'
	THEN = r'THEN'
	TO = r'TO'
	IF = r'IF'
	ELSE = r'ELSE'
	STRING = r'\".*?\"'

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
