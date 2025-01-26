import ply.lex as lex

tokens = [
    'CONTRACT',
    'FUNCTION',
    'IDENTIFIER',
    'LBRACE', 'RBRACE', # {}
    'LPAREN', 'RPAREN', # ()
    'PUBLIC',
    'RETURNS',
    'RETURN',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'NUMBER',
    'UINT',
    'SEMICOLON',
]

reserved = {
    'contract': 'CONTRACT',
    'function': 'FUNCTION',
    'public'  : 'PUBLIC',
    'returns' : 'RETURNS',
    'return'  : 'RETURN',
    'uint'    : 'UINT',
}

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_DIVIDE    = r'\/'
t_MULTIPLY  = r'\*'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check if it's a reserved keyword
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert the value to an integer
    return t

# Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character {t.value[0]} at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = '''
    contract MyContract {
        function hello() public returns (uint) {
            return 1 + 2;
        }
    }
    '''

    lexer.input(data)

    for token in lexer:
        print(token)