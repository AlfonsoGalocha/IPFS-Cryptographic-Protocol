import hashlib

def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

if __name__ == "__main__":
    user_input = input("Ingrese una cadena de caracteres para hashear: ")
    hashed_result = calculate_hash(user_input)
    print(f"El hash SHA-256 de '{user_input}' es: {hashed_result}")
