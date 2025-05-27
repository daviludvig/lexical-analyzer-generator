import os

def get_file_lines(file_path: str) -> list[str]:
    """Lê um arquivo e retorna uma lista de linhas não vazias, sem espaços extras."""   
    with open(file_path, 'r', encoding='utf-8') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]  # remove linhas vazias e espaços
    return linhas

def file_exists(file_path: str) -> bool:
    """Verifica se um arquivo existe."""
    return os.path.isfile(file_path)