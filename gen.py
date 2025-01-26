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

def gen_binary_op(ast):
    op = ast['operator']
    left = ast['left']
    right = ast['right']

    if left["type"] == "number": left_code = f"PUSH32 {left['value']}"
    else:                        left_code = gen_binary_op(left)

    if right["type"] == "number": right_code = f"PUSH32 {right['value']}"
    else:                         right_code = gen_binary_op(right)

    return f"""
            {left_code}
            {right_code}
            {OPERATOR_MAP[op]}
            """

def gen_return(): # NOTE: can onyl return 32 bytes
    return f"""
            PUSH32 0x00
            MSTORE
            PUSH32 0x20
            PUSH32 0x00
            RETURN
            """

def funcs(ast):
    ass = ""
    functions = get_functions(ast)
    for f in functions:
        value = f['body'][0]['value']
        type  = value['type']

        if type == 'binary_op': ass += gen_binary_op(value)
        ass += gen_return()

    return "\n".join(line.lstrip() for line in ass.splitlines() if line.strip())