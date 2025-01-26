import ply.yacc as yacc
from lexer import tokens
from utils import pretty_print

def p_contract(p):
    '''contract : CONTRACT IDENTIFIER LBRACE contract_body RBRACE'''
    p[0] = {
        "type": "contract",
        "name": p[2],
        "body": p[4],
    }

def p_contract_body(p):
    '''contract_body : function_definition
                     | contract_body function_definition'''
    if len(p) == 2:
        p[0] = [p[1]]  # Single function
    else:
        p[0] = p[1] + [p[2]]  # Append to existing body

def p_function_definition(p):
    '''function_definition : FUNCTION IDENTIFIER LPAREN RPAREN PUBLIC RETURNS LPAREN UINT RPAREN LBRACE function_body RBRACE'''
    p[0] = {
        "type": "function",
        "name": p[2],
        "visibility": "public",
        "return_type": "uint",
        "body": p[11],  # Function body
    }

def p_function_body(p):
    '''function_body : statement
                     | function_body statement'''
    if len(p) == 2:
        p[0] = [p[1]]  # Single statement
    else:
        p[0] = p[1] + [p[2]]  # Append to existing body

def p_statement(p):
    '''statement : RETURN expression SEMICOLON'''
    p[0] = {
        "type": "return",
        "value": p[2],
    }

def p_expression(p):
    '''expression : NUMBER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression DIVIDE expression
                  | expression MULTIPLY expression'''
    if len(p) == 2:
        p[0] = {
            "type": "number",
            "value": p[1],
        }
    else:
        p[0] = {
            "type": "binary_op",
            "operator": p[2],  # "+" or "-"
            "left": p[1],
            "right": p[3],
        }

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value: {p.value}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

data = '''
    contract MyContract {
        function add1() public returns (uint) {
            return 1 + 2;
        }
        function add2() public returns (uint) {
            return 9 + 10;
        }
    }
    '''

result = parser.parse(data)

# pretty_print(result)