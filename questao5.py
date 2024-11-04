def reverse_string(text):
    inverted_text = ""
    for char in text:
        inverted_text = char + inverted_text
    return inverted_text

# Exemplo de uso
string = "exemplo"
print("String invertida:", reverse_string(string))
