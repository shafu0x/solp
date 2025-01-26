from Crypto.Hash import keccak

def read_file(file_path):
    open_file = open(file_path, "r")
    data = open_file.read()
    open_file.close()
    return data

def get_function_selector(function_signature):
    k = keccak.new(digest_bits=256)
    k.update(function_signature.encode('utf-8'))
    return k.hexdigest()[:8]

def pretty_print(result, indent=0):
    if isinstance(result, dict):
        for key, value in result.items():
            print("    " * indent + f"{key}:")
            pretty_print(value, indent + 1)
    elif isinstance(result, list):
        for item in result:
            pretty_print(item, indent)
    else:
        print("    " * indent + str(result))

def get_functions(ast):
    return [func['name'] for func in ast['body'] if func['type'] == 'function']