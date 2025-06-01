import model.nfa as nfa
import model.dfa as dfa
import core.union as union
import example_dfa as example_dfa
import example_nfa as example_nfa

def main():
    
    det_fa : dfa.DFA = example_dfa.build_dfa()
    no_det_fa : nfa.NFA = example_nfa.build_nfa()
    
    new_nfa : nfa.NFA = union.union(det_fa, no_det_fa)
    print(new_nfa)
    
    print(new_nfa.getDestinationStatesFromTransition(new_nfa.initial_state, "&"))
    
if __name__ == "__main__":
    main()
