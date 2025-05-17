import model.nfa as nfa
import model.dfa as dfa
import core.NFAtoDFAconversion as conversion
import exampleNFA as example_nfa


def main():
    
    no_det_fa : nfa.NFA = example_nfa.build_nfa()
    
    Q,F = conversion.NFAtoDFAconversion(no_det_fa)

    print(Q, F)
    
if __name__ == "__main__":
    main()