from core.regex_parser import RegexToken
from typing import List, Tuple

'''
Este algoritmo recebe como input uma lista de caracteres e operadores como a retornada pelo regex parser,
e a retorna reescrita em notação polonesa invertida usando o algoritmo de Shunting-Yard.
'''

# Define precedência e associatividade dos operadores
precedence = {
    RegexToken.STAR: 3,
    RegexToken.PLUS: 3,
    RegexToken.QUESTION: 3,
    RegexToken.CONCAT: 2,
    RegexToken.OR: 1,
}

right_associative = {
    RegexToken.STAR,
    RegexToken.PLUS,
    RegexToken.QUESTION,
}

def shunting_yard(tokens: List[RegexToken]) -> List[RegexToken]:
    output = []
    stack = []

    for token in tokens:
        tok_type = token.type
        tok_val = token.value

        if tok_type == RegexToken.CHAR:
            output.append(token)

        elif tok_type in {RegexToken.STAR, RegexToken.PLUS, RegexToken.QUESTION,
                          RegexToken.CONCAT, RegexToken.OR}:
            while stack:
                top_type = stack[-1].type
                if top_type == RegexToken.LPAREN:
                    break

                if (precedence[top_type] > precedence[tok_type] or
                    (precedence[top_type] == precedence[tok_type] and
                     tok_type not in right_associative)):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)

        elif tok_type == RegexToken.LPAREN:
            stack.append(token)

        elif tok_type == RegexToken.RPAREN:
            while stack and stack[-1].type != RegexToken.LPAREN:
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()  # Remove the '('

    while stack:
        if stack[-1].type in {RegexToken.LPAREN, RegexToken.RPAREN}:
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return output