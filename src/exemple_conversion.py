import model.nfa as nfa
import model.dfa as dfa
import core.NFAtoDFA as conversion
import exampleNFA as example_nfa


def main():
    
    no_det_fa : nfa.NFA = example_nfa.build_nfa()
    
    DFA = conversion.NFAtoDFA(no_det_fa)
    
if __name__ == "__main__":
    main()