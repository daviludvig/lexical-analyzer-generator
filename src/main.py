import sys
import core.regex_parser as regex_parser
from core.shunting_yard import shunting_yard
import core.utils as utils
from core.nfa_builder import NFAFromRegex as nfa_from_regex
from core.NFAtoDFA import NFAtoDFA as nfa_to_dfa
from typing import List
from model.dfa import DFA
from model.symbol_table import TokenType
from core.union import union
import core.source_parser as source_parser
from model.symbol_table import SymbolTable


def get_dfas_from_tokentypes(tokentypes : List[TokenType]) -> List[DFA]:
    """
    Recebe uma lista de TokenType com regex concatenados e transforma cada regex em um DFA.
    
    Deixa o primeiro DFA como None, que será o DFA que aceita a linguagem de todos os lexemas válidos.
    
    """
    dfas = []
    dfa_inicial = None  
    dfas.append(dfa_inicial)
    for tokentype in tokentypes:
        postfix_tokentype = shunting_yard(tokentype.regex)
        nfa = nfa_from_regex(postfix_tokentype).build()
        dfa = nfa_to_dfa(nfa)
        dfa.name = tokentype.name
        dfas.append(dfa)
    return dfas

def get_full_language_dfa(dfas : List[DFA]) -> DFA:
    """
    Combina todos os DFAs em um único DFA que aceita a linguagem de todos os lexemas válidos.
    """
    full_language_dfa = dfas[1]._cloneWithPrefix("cl1_")
    
    for i in range(2, len(dfas)):
        full_language_dfa = nfa_to_dfa(union(full_language_dfa, dfas[i]))
    
    return full_language_dfa

def main() -> None:
    """
    Função principal que executa o analisador léxico.
    Lê os arquivos de regex e código-fonte, constrói os DFAs a partir das regex e analisa o código-fonte.
    Exibe os tokens encontrados no código-fonte.
    Uso: python src/main.py <regex_file> <source_file>
    """
    if len(sys.argv) != 3:
        print("Uso: python src/main.py <regex_file> <source_file>")
        sys.exit(1)
        
    regex_file = sys.argv[1]
    source_file = sys.argv[2]
    
    if not utils.file_exists(source_file) or not utils.file_exists(regex_file):
        print(f"Arquivo de entrada ou regex não encontrado: {source_file} ou {regex_file}")
        sys.exit(1)
    
    tokentypes_from_regex_file = regex_parser.get_regex_from_file(regex_file)
    dfas = get_dfas_from_tokentypes(tokentypes_from_regex_file)
    
    dfas[0] = get_full_language_dfa(dfas)
    
    symbol_table = SymbolTable()
    
    tokens = source_parser.parse_source_code_from_file(source_file, dfas, symbol_table)
    for token in tokens:
        print(f"<{token.lexeme}, {token.tokentype}>")
    
if __name__ == "__main__":
    main()
    sys.exit(0)