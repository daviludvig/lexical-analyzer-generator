import model.symbol_table as symbol_table
import core.nfa_builder as nfa_builder
import core.NFAtoDFA as nfa_to_dfa
from core.shunting_yard import shunting_yard
from core.regex_parser import tokenize_regex, insert_concatenation, get_regex_from_file, TokenType
from core.nfa_builder import NFAFromRegex

def main():
    id_regex = "[a-zA-Z_]([a-zA-Z]|[0-9]|_)*"
    input_id = "aaabnvs__ah86986___89689678_AKNBAHJD_VAHJD___CVAJjabdjhasvhjfajfva"
    tokens = tokenize_regex(id_regex)
    tokens_with_concat = insert_concatenation(tokens)
    postfix = shunting_yard(tokens_with_concat)
    nfa = NFAFromRegex(postfix).build()
    dfa = nfa_to_dfa.NFAtoDFA(nfa)    
    
    tokentypes_from_regex_file = get_regex_from_file("inputs/main_regex.txt")
    for tokentype in tokentypes_from_regex_file:
        postfix_ = shunting_yard(tokentype.regex)
        nfa_ = NFAFromRegex(postfix_).build()
        dfa_ = nfa_to_dfa.NFAtoDFA(nfa_)    
        tokentype.dfa = dfa_
        print(tokentype.name)
    
    print(dfa.isValidInput(input_id))
    
    token_type = TokenType(name="ID", regex=tokens_with_concat, dfa=dfa)
    lexeme = symbol_table.Lexeme()
    
    for char in input_id:
        lexeme.increase(char)
        # print(f"Is valid {dfa.isValidInput(lexeme.get())} {lexeme.get()}")
        
    ts = symbol_table.SymbolTable()

    ts.insert(lexeme, token_type)
    
    print(ts)
    print(len(nfa.states))
    
if __name__ == "__main__":
    main()
    # sys.exit(0)
        
    