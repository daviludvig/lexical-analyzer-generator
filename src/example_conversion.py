import model.nfa as nfa
import model.dfa as dfa
import core.NFAtoDFA as conversion
import example_nfa as example_nfa


def main():
    
    no_det_fa : nfa.NFA = example_nfa.build_nfa()
    
    det_fa = conversion.NFAtoDFA(no_det_fa)

    print("\n" + det_fa.getTabularFormat())
    
if __name__ == "__main__":
    main()