# authentication.py

tokens = {"admin": "securetoken123"}  # Predefined tokens

def authenticate(request):
    token = request.headers.get("Authorization")
    if token and token in tokens.values():
        return True
    return False
