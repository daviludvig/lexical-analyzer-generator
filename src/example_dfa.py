import model.dfa as dfa
import model.fa as fa

def build_dfa() -> dfa.DFA:

    alphabet : fa.Set[str] = {"a", "b"}
    
    q0 : fa.State = fa.State(name='q0', is_initial=True, is_final=False)
    q1 : fa.State = fa.State(name='q1', is_initial=False, is_final=True)
    q2 : fa.State = fa.State(name='q2', is_initial=False, is_final=False)
    
    t1 : fa.Transition = fa.Transition(source_state=q0, input_symbol="a", target_state=q0)
    t2 : fa.Transition = fa.Transition(source_state=q0, input_symbol="b", target_state=q1)
    t3 : fa.Transition = fa.Transition(source_state=q1, input_symbol="a", target_state=q1) 
    
    det_fa : dfa.DFA = dfa.DFA(alphabet=alphabet)
    det_fa.addStates({q0,q1,q2})
    det_fa.addTransitions({t1,t2,t3})
    
    return det_fa

def main():
    
    det_fa : dfa.DFA = build_dfa()
    print(det_fa)
    
    input_example : str = "abaaaaaa"
    print(f"Is input '{input_example}' valid: {det_fa.isValidInput(input_example)}")
    print("\n" + det_fa.getTabularFormat())

    print(det_fa._cloneWithPrefix("copy_"))

if __name__ == "__main__":
    main()