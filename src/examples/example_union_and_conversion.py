import model.nfa as nfa
import model.dfa as dfa
import core.union as union
import examples.example_dfa as example_dfa
import examples.example_nfa as example_nfa
import core.NFAtoDFA as conversion

def main():
    
    print(f"Exemplo de união de DFAs e conversão para DFA\n")
    
    n_det_fa_1 : nfa.NFA = example_nfa.build_nfa()
    det_fa_2 : dfa.DFA = example_dfa.build_dfa2()
    
    print("NFA 1:\n")
    print(n_det_fa_1.getTabularFormat())
    
    print("\nDFA 2:\n")
    print(det_fa_2.getTabularFormat())
    
    new_nfa : nfa.NFA = union.union(n_det_fa_1, det_fa_2)
    print ("\nResultado da união: \n")

    print(new_nfa.getTabularFormat(), "\n")

    new_det_fa = conversion.NFAtoDFA(new_nfa)

    print ("Resultado da conversão: \n")

    print(new_det_fa.getTabularFormat())
    
if __name__ == "__main__":
    main()