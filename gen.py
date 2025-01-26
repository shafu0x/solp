from parser import parser
from utils import *

contract = read_file('Test.sol')
ast = parser.parse(contract)

def dispatcher(ast):
    functions          = get_functions(ast)
    function_selectors = ["0x" + get_function_selector(func + "()") for func in functions]

    dis = ""

    for i, selector in enumerate(function_selectors):
        dis += f"""
        PUSH4 {selector}
        CALLDATALOAD
        EQ
        PUSH1 {hex(0x12 + (0xe*i)) }
        JUMPI
        """
    
    dis += "\n"
    dis += "STOP"

    return dis