import model.nfa as nfa
import model.dfa as dfa
import core.union as union
import example_dfa as example_dfa_1
import example_dfa2 as example_dfa_2
import core.NFAtoDFA as conversion

def main():
    
    print(f"Exemplo de união de DFAs e conversão para DFA\n")
    
    det_fa_1 : dfa.DFA = example_dfa_1.build_dfa()
    det_fa_2 : dfa.DFA = example_dfa_2.build_dfa()
    
    print("DFA 1:\n")
    print(det_fa_1.getTabularFormat())
    
    print("\nDFA 2:\n")
    print(det_fa_2.getTabularFormat())
    
    new_nfa : nfa.NFA = union.union(det_fa_1, det_fa_2)
    print ("\nResultado da união: \n")

    print(new_nfa.getTabularFormat(), "\n")

    new_det_fa = conversion.NFAtoDFA(new_nfa)

    print ("Resultado da conversão: \n")

    print(new_det_fa.getTabularFormat())
    
if __name__ == "__main__":
    main()