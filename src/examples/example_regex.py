from core.regex_parser import RegexToken
from core.regex_parser import expand_char_class
from core.regex_parser import tokenize_regex
from core.regex_parser import insert_concatenation

# Exemplos de expressões regulares
test_regexes = [
    "[a-zA-Z]([a-zA-Z]|[0-9])*",   # id
    "[1-9][0-9]*|0",               # número
    "a(b|c)*d",
    "(a|b)+c?",
]

def main():

    print(f"Exemplo de análise de expressões regulares")

    for regex in test_regexes:
        print(f"\nRegex: {regex}")
        tokens = tokenize_regex(regex)
        print("Tokens:")
        print([str(tok) for tok in tokens])

        with_concats = insert_concatenation(tokens)
        print("Tokens com concatenação:")
        print([str(tok) for tok in with_concats])

if __name__ == "__main__":
    main()