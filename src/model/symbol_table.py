from .dfa import DFA
from core.regex_parser import TokenType
from typing import List, Dict
    
class Lexeme:
    def __init__(self):
        self.lexeme : str = ""
        
    def __repr__(self):
        return f"<Lexeme('{self.lexeme}')>"
    
    def __str__(self):
        return self.lexeme
    
    def __eq__(self, other):
        if isinstance(other, Lexeme):
            return self.lexeme == other.lexeme
        return False

    def __hash__(self):
        return hash(self.lexeme)
    
    def get(self) -> str:
        """Retorna o lexema atual"""
        return self.lexeme

    def increase(self, char: str) -> None:
        """Adiciona um caractere ao lexema"""
        self.lexeme += char   
    
    def decrease(self) -> None:
        """Remove o último caractere do lexema"""
        if self.lexeme:
            self.lexeme = self.lexeme[:-1] 


class SymbolTable:
    def __init__(self):
        # Inicializa com palavras reservadas
        self.table : Dict[Lexeme, TokenType] = {}

    def insert(self, lexeme: Lexeme, token_type: str):
        """Insere um novo símbolo se não existir"""
        if lexeme not in self.table:
            self.table[lexeme] = token_type

    def lookup(self, lexeme: Lexeme) -> str:
        """Retorna o tipo de token do lexema"""
        return self.table.get(lexeme, None)

    def contains(self, lexeme: Lexeme) -> bool:
        """Verifica se o lexema já está na tabela"""
        return lexeme in self.table

    def export(self, filename: str = "tabela_simbolos.csv"):
        """Exporta a tabela para CSV"""
        with open(filename, "w") as f:
            f.write("Lexema,Tipo\n")
            for lexeme, tipo in self.table.items():
                f.write(f"{lexeme},{tipo}\n")

    def __repr__(self):
        return f"<SymbolTable(size={len(self.table)})>"

    def __str__(self):
        output = ["Tabela de Símbolos:"]
        for lexeme, token_type in self.table.items():
            output.append(f"  {lexeme.get():<20} <=> {token_type.name}")
        return "\n".join(output)