import random
import string
import base64
import ast
import codegen

# Helper functions

def generate_random_name(length=8):
    return ''.join(random.sample(string.ascii_lowercase + string.digits, length))

def encrypt_code(code):
    encoded_bytes = base64.b64encode(code.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decrypt_code(encrypted_code):
    decoded_bytes = base64.b64decode(encrypted_code.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def transform_code(tree):
    class Transformer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            node.name = generate_random_name()
            return self.generic_visit(node)

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Load):
                node.id = generate_random_name()
            return self.generic_visit(node)

        def visit_If(self, node):
            # Transform if conditions to always true
            new_test = ast.Constant(value=True)
            node.test = new_test
            return self.generic_visit(node)

    return Transformer().visit(tree)

def mutate_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Encrypt the original code
    encrypted_code = encrypt_code(code)
    
    # Create the wrapper code to decrypt and execute the encrypted code
    decrypted_code = """
import base64

def decrypt_code(encrypted_code):
    decoded_bytes = base64.b64decode(encrypted_code.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

exec(decrypt_code("{encrypted_code}"))
""".format(encrypted_code=encrypted_code)

    # Parse and transform the wrapper code
    tree = ast.parse(decrypted_code)
    transformed_tree = transform_code(tree)
    mutated_code = codegen.to_source(transformed_tree)

    # Flatten control flow and add dummy code
    mutated_code = mutated_code.replace('if ', 'if True: pass # ')
    mutated_code += "\n\n# Dummy code\nprint('This is dummy code.')"

    # Save the mutated code
    with open('mutated.py', 'w') as file:
        file.write(mutated_code)

if __name__ == "__main__":
    mutate_code('original.py')
