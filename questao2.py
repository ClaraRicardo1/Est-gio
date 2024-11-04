def is_fibonacci(number):
    a, b = 0, 1
    while a <= number:
        if a == number:
            return f"O número {number} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {number} NÃO pertence à sequência de Fibonacci."

# Exemplo de uso
number = 21  # Insira qualquer número para testar
print(is_fibonacci(number))
