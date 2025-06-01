import model.symbol_table as symbol_table
import core.nfa_builder as nfa_builder
import core.NFAtoDFA as nfa_to_dfa
from core.shunting_yard import shunting_yard
from core.regex_parser import tokenize_regex, insert_concatenation, get_regex_from_file, TokenType
from core.nfa_builder import NFAFromRegex

def main():
    
    print(f"Exemplo de tabela de símbolos com NFA e DFA")
    print(f"Construindo NFA e DFA a partir de uma expressão regular\n")
    
    id_regex = "[a-zA-Z_]([a-zA-Z]|[0-9]|_)*"
    input_id = "aaabnvs__ah86986___89689678_AKNBAHJD_VAHJD___CVAJjabdjhasvhjfajfva"
    
    print(f"Expressão regular: {id_regex}")
    print(f"Entrada: {input_id}")
    
    tokens = tokenize_regex(id_regex)
    tokens_with_concat = insert_concatenation(tokens)
    postfix = shunting_yard(tokens_with_concat)
    nfa = NFAFromRegex(postfix).build()
    dfa = nfa_to_dfa.NFAtoDFA(nfa)    
    
    print(f"Número de estados no DFA: {len(dfa.states)}\n")
    
    print(f"Entrada '{input_id}' é válida para a expressão regular {id_regex}: {dfa.isValidInput(input_id)}")
    
    token_type = TokenType(name="ID", regex=tokens_with_concat, dfa=dfa)
    lexeme = symbol_table.Lexeme()
    
    for char in input_id:
        lexeme.increase(char)
        
    ts = symbol_table.SymbolTable()

    ts.insert(lexeme, token_type)
    
    print(ts)
    
if __name__ == "__main__":
    main()
    # sys.exit(0)
        
    