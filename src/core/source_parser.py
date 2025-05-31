from .utils import get_file_lines
from typing import List, Tuple
from model.dfa import DFA
from model.symbol_table import Token, Lexeme


def parse_source_code_from_file(file_path: str, dfas: List[DFA]) -> None:
    """
    Reads the content of a source code file and returns it as a string.

    Args:
        file_path (str): The path to the source code file.
        dfas (List[DFA]): A list of DFA objects to be used in parsing.

    Returns:
        
    """
    lines = get_file_lines(file_path)
    single_line = ""
    for line in lines:
        single_line += "\n" + line
    
    tokens = get_tokens(single_line, dfas)
    return tokens

def get_tokens(source_code : str, dfas : List[DFA]) -> List[Tuple[str, str]]:
    """
    O automato principal da análise léxica é o dfas[0], que é o DFA que aceita a linguagem de todos os lexemas válidos.
    
    """
    
    tokens = []

    lexeme_obj = Lexeme()
    curr_token = Token()
    i = 0
    while i != len(source_code):
        if ((lexeme_obj.get() == "") and (source_code[i] == " " or source_code[i] == "\n")):
            i += 1
            continue
        lexeme_obj.increase(source_code[i])
        if not dfas[0].isValidInput(lexeme_obj.get()):
            if ((source_code[i] != " ") and (source_code[i] != "\n") and (source_code[i] != ";")):  # Ponto e vírgula só pode ser usado para final de sentença
                while ((source_code[i] != " ") and (source_code[i] != "\n")):
                    i += 1
                    lexeme_obj.increase(source_code[i])
                lexeme_obj.decrease()
                curr_token.lexeme = lexeme_obj.get()
                curr_token.tokentype = "ERRO"
                tokens.append(curr_token)
                curr_token = Token()
                lexeme_obj = Lexeme()
                i += 1
                continue

            # retroceder 1
            i -= 1
            lexeme_obj.decrease()
            
            # checar todos os outros DFAs
            lexeme_type = get_lexeme_type(lexeme_obj, dfas)
            
            curr_token.lexeme = lexeme_obj.get()
            curr_token.tokentype = lexeme_type
            tokens.append(curr_token)
            curr_token = Token()
            lexeme_obj = Lexeme()

        i += 1
        
    return tokens

def get_lexeme_type(lexeme: Lexeme, dfas: List[DFA]) -> str:
    for i in range(1, len(dfas)):
        if dfas[i].isValidInput(lexeme.get()):
            return dfas[i].name
