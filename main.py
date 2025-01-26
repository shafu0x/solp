from parser import parser
from utils import *
from gen import *
from opcodes import *

contract = read_file('Test.sol')
ast = parser.parse(contract)
dis = dispatcher(ast)
bytecode = disassemble(dis)

print(dis)
print(bytecode)