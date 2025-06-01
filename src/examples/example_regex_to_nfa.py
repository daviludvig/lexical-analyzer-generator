from core.regex_parser import tokenize_regex, insert_concatenation
from core.nfa_builder import NFAFromRegex
from core.shunting_yard import shunting_yard

# Examplos de regex
regex = "(a|b)+c?"
# regex = "(a|b)"
# regex = "ab"

def main():

    print(f"Exemplo de conversão de expressão regular para NFA")
    print(f"Expressão regular: {regex}\n")

    # Passo 1: Tokenizar
    tokens = tokenize_regex(regex)
    print("Tokens:", tokens)

    # Passo 2: Inserir concatenação
    tokens_with_concat = insert_concatenation(tokens)
    print("Com concatenação:", tokens_with_concat)

    # Passo 3: Converter para postfix
    postfix = shunting_yard(tokens_with_concat)
    print("Postfix:", postfix)

    # Passo 4: Construir NFA
    nfa = NFAFromRegex(postfix).build()
    print("\nNFA (Formato tabular):")
    print(nfa.getTabularFormat())

if __name__ == "__main__":
    main()