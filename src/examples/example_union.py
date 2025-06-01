import model.nfa as nfa
import model.dfa as dfa
import core.union as union
import example_dfa as example_dfa
import example_nfa as example_nfa

def main():
    
    print(f"Exemplo de união de DFA e NFA\n")
    
    det_fa : dfa.DFA = example_dfa.build_dfa()
    print("DFA de entrada:\n\n", det_fa.getTabularFormat()+"\n")
    no_det_fa : nfa.NFA = example_nfa.build_nfa()
    print("NFA de entrada:\n\n",no_det_fa.getTabularFormat()+"\n")
    
    new_nfa : nfa.NFA = union.union(det_fa, no_det_fa)
    print("NFA de saída:\n\n",new_nfa.getTabularFormat())
        
if __name__ == "__main__":
    main()
