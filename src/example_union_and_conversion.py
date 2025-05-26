import model.nfa as nfa
import model.dfa as dfa
import core.union as union
import example as example_dfa
import exampleDFA2 as example_dfa_2
import core.NFAtoDFA as conversion

def main():
    
    det_fa_1 : dfa.DFA = example_dfa.build_dfa()
    det_fa_2 : dfa.DFA = example_dfa_2.build_dfa()
    
    
    new_nfa : nfa.NFA = union.union(det_fa_1, det_fa_2)
    print ("Resultado da união: \n")

    print(new_nfa, "\n")

    new_det_fa = conversion.NFAtoDFA(new_nfa)

    print ("Resultado da conversão: \n")

    print("\n" + new_det_fa.getTabularFormat())
    
if __name__ == "__main__":
    main()