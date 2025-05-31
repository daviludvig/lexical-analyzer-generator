import core.source_parser as source_parser
import core.NFAtoDFA as nfa_to_dfa
import core.union as union
from core.shunting_yard import shunting_yard
from core.regex_parser import get_regex_from_file
from core.nfa_builder import NFAFromRegex

def main():
    
    dfas = []
    dfa_inicial = None
    dfas.append(dfa_inicial)

    tokentypes_from_regex_file = get_regex_from_file("inputs/main_regex.txt")
    for tokentype in tokentypes_from_regex_file:
        postfix_ = shunting_yard(tokentype.regex)
        nfa_ = NFAFromRegex(postfix_).build()
        dfa_ = nfa_to_dfa.NFAtoDFA(nfa_)
        dfa_.name = tokentype.name
        dfas.append(dfa_)

    dfas[0] = dfas[1]._cloneWithPrefix("cl1_")

    for i in range(2, len(dfas)):
        dfas[0] = nfa_to_dfa.NFAtoDFA(union.union(dfas[0], dfas[i]))
    
    tokens = source_parser.parse_source_code_from_file("inputs/main_source.txt", dfas)
    for token in tokens:
        print(f"<{token.lexeme}, {token.tokentype}>")

if __name__ == "__main__":
    main()