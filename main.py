from parser import parser
from utils import *
from gen import *
from opcodes import *
from storage import *

contract = read_file('Test.sol')
ast = parser.parse(contract)
dis = dispatcher(ast)
func = funcs(ast)
bytecode = disassemble(dis)
storage_slots = get_storage_slots(ast)

# print(contract)
# print(dis)
# print(bytecode)
# print(func)
# print(get_storage_slots(ast))