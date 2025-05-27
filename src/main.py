import sys
import core.regex_parser as regex_parser
import core.utils as utils

def main() -> None:
    if len(sys.argv) != 3:
        print("Uso: python src/main.py <regex_file> <source_file>")
        sys.exit(1)
        
    regex_file = sys.argv[1]
    source_file = sys.argv[2]
    
    if not utils.file_exists(source_file) or not utils.file_exists(regex_file):
        print(f"Arquivo de entrada ou regex não encontrado: {source_file} ou {regex_file}")
        sys.exit(1)
    
    print(regex_parser.get_regex_from_file(regex_file))
    
    
if __name__ == "__main__":
    main()
    sys.exit(0)