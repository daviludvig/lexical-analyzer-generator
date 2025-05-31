from .utils import get_file_lines
from typing import List, Tuple
from model.dfa import DFA
from model.symbol_table import Lexeme


def parse_source_code_from_file(file_path: str, dfas: List[DFA]) -> None:
    """
    Reads the content of a source code file and returns it as a string.

    Args:
        file_path (str): The path to the source code file.
        dfas (List[DFA]): A list of DFA objects to be used in parsing.

    Returns:
        
    """
    lines = get_file_lines(file_path)
    single_line = "".join(lines)
    
    lexemes = get_tokens(single_line, dfas)
    
    pass

def get_tokens(source_code : str, dfas : List[DFA]) -> List[Tuple[str, str]]:
    """
    O automato principal da análise léxica é o dfas[0], que é o DFA que aceita a linguagem de todos os lexemas válidos.
    
    """
    
    tokens = []
    
    curr_lexeme = ""
    curr_token = tuple()
    for i in range(len(source_code)):
        if curr_lexeme == "" and (source_code[i] == " " or source_code[i] == "\n"):
            continue
        if curr_lexeme == "":
            lexeme_obj = Lexeme()
        lexeme_obj.increase(source_code[i])
        if not dfas[0].isValidInput(lexeme_obj.get()):
            # retroceder 1
            i -= 1
            lexeme_obj.decrease()
            
            # checar todos os outros DFAs
            lexeme_type = get_lexeme_type(lexeme_obj, dfas)
            
            curr_token = (lexeme_obj.get(), lexeme_type)
            tokens.append(curr_token)
            curr_lexeme = ""
        
    return tokens

def get_lexeme_type(lexeme: Lexeme, dfas: List[DFA]) -> str:
    for dfa in dfas:
        if dfa.isValidInput(lexeme.get()):
            return dfa.name
