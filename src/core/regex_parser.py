import re

class RegexToken:
    CHAR = 'CHAR'
    STAR = '*'
    PLUS = '+'
    QUESTION = '?'
    OR = '|'
    LPAREN = '('
    RPAREN = ')'
    CONCAT = '.'  # Caso especial: inseriremos este operador mesmo que não apareça explicitamente na regex
    CHAR_CLASS = 'CLASS'

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value})" if self.value else self.type

# Expandir uma representação condensada de caracteres
def expand_char_class(char_class: str) -> list:
    # Exemplo: [a-zA-Z0-9] → ['a', ..., 'z', 'A', ..., 'Z', '0', ..., '9']
    chars = []
    i = 0
    while i < len(char_class):
        if i + 2 < len(char_class) and char_class[i+1] == '-':
            start = char_class[i]
            end = char_class[i+2]
            chars.extend(chr(c) for c in range(ord(start), ord(end)+1))
            i += 3
        else:
            chars.append(char_class[i])
            i += 1
    return chars

def tokenize_regex(regex: str) -> list[RegexToken]:
    tokens = []
    i = 0
    while i < len(regex):
        c = regex[i]

        if c in {'*', '+', '?', '|', '(', ')'}:
            tokens.append(RegexToken(c))
            i += 1

        elif c == '[':
            j = i + 1
            while j < len(regex) and regex[j] != ']':
                j += 1
            if j == len(regex):
                raise ValueError("Classe de caracteres não foi fechada.")
            char_class = regex[i+1:j]
            expanded = expand_char_class(char_class)
            # Representar como um agrupamento de OR: [a-zA-Z] → (a|b|...|Z)
            if len(expanded) == 1:
                tokens.append(RegexToken(RegexToken.CHAR, expanded[0]))
            else:
                tokens.append(RegexToken(RegexToken.LPAREN))
                for idx, ch in enumerate(expanded):
                    tokens.append(RegexToken(RegexToken.CHAR, ch))
                    if idx < len(expanded) - 1:
                        tokens.append(RegexToken(RegexToken.OR))
                tokens.append(RegexToken(RegexToken.RPAREN))
            i = j + 1

        elif c == '\\':
            # Tratar caractere de escape: \* ou \( etc
            if i + 1 < len(regex):
                tokens.append(RegexToken(RegexToken.CHAR, regex[i+1]))
                i += 2
            else:
                raise ValueError("Caractere de escape ao final de um padrão.")

        else:
            tokens.append(RegexToken(RegexToken.CHAR, c))
            i += 1

    return tokens

# Operador de concatenação definido explicitamente a partir da regex, quando há um caractere ou ')' à esquerda, e um caractere ou '(' à direita
def insert_concatenation(tokens: list[RegexToken]) -> list[RegexToken]:
    result = []
    for i in range(len(tokens)):
        result.append(tokens[i])
        if i + 1 < len(tokens):
            t1, t2 = tokens[i], tokens[i+1]

            def is_operand(t):
                return t.type in {RegexToken.CHAR, RegexToken.RPAREN}

            def is_prefix(t):
                return t.type in {RegexToken.CHAR, RegexToken.LPAREN}

            if is_operand(t1) and is_prefix(t2):
                result.append(RegexToken(RegexToken.CONCAT))
    return result