import model.nfa as nfa
import model.dfa as dfa
import core.NFAtoDFA as conversion
import example_nfa as example_nfa


def main():
    
    print(f"Exemplo de conversão de NFA para DFA\n")
    
    print(f"NFA original:")
    no_det_fa : nfa.NFA = example_nfa.build_nfa()
    print(no_det_fa.getTabularFormat())
    
    det_fa = conversion.NFAtoDFA(no_det_fa)

    print("\nDFA obtido\n" + det_fa.getTabularFormat())
    
if __name__ == "__main__":
    main()