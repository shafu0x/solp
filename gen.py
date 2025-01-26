from parser import parser
from utils import *
from opcodes import *

contract = read_file('Test.sol')
ast = parser.parse(contract)

def dispatcher(ast):
    functions          = get_function_names(ast)
    function_selectors = ["0x" + get_function_selector(func + "()") for func in functions]

    ass = ""

    for i, selector in enumerate(function_selectors):
        ass += f"""
        PUSH4 {selector}
        CALLDATALOAD
        EQ
        PUSH1 {hex(0x12 + (0xe*i)) }
        JUMPI
        """
    
    ass += "\n"
    ass += "STOP"

    return ass

def funcs(ast):
    ass = ""
    functions = get_functions(ast)
    for f in functions:
        if f['body'][0]['type'] == 'return':
            value = f['body'][0]['value']
            op    = value['operator']
            left  = value['left']['value']
            right = value['right']['value']
            print(op, left, right)

            ass += f"""
                    PUSH32 {left}
                    PUSH32 {right}
                    {OPERATOR_MAP[op]}
                    PUSH32 0x00
                    MSTORE
                    PUSH32 0x20
                    PUSH32 0x00
                    RETURN
                    """
    return ass