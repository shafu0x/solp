from parser import parser
from utils import *
from gen import *
from opcodes import *

contract = read_file('Test.sol')
ast = parser.parse(contract)
dis = dispatcher(ast)
func = funcs(ast)
# bytecode = disassemble(dis)

# print(ast)
# print(contract)
# print(dis)
# print(bytecode)
print(func)