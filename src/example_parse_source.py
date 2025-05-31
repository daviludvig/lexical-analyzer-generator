import core.source_parser as source_parser
import model.symbol_table as symbol_table
import core.nfa_builder as nfa_builder
import core.NFAtoDFA as nfa_to_dfa
import model.dfa as dfa
from core.shunting_yard import shunting_yard
from core.regex_parser import tokenize_regex, insert_concatenation, get_regex_from_file, TokenType
from core.nfa_builder import NFAFromRegex

def main():
    
    dfas = []
    dfa_inicial = dfa.DFA
    tokentypes_from_regex_file = get_regex_from_file("inputs/main_regex.txt")
    for tokentype in tokentypes_from_regex_file:
        postfix_ = shunting_yard(tokentype.regex)
        nfa_ = NFAFromRegex(postfix_).build()
        dfa_ = nfa_to_dfa.NFAtoDFA(nfa_)
        
    
    tokens = source_parser.get_tokens("inputs/main_source.txt")