def decode_code(secret_Code):
    words = secret_Code.split("-") 
    words.reverse()
    return " ".join(words).upper()
secret_code = "charlie-bravo-alpha"
print(decode_code(secret_code))