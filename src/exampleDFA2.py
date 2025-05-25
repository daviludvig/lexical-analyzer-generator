import model.dfa as dfa
import model.fa as fa

def main():
    
    alphabet : fa.Set[str] = {"a", "b"}
    
    q0 : fa.State = fa.State(name='q0', is_initial=True, is_final=False)
    q1 : fa.State = fa.State(name='q1', is_initial=False, is_final=False)
    q2 : fa.State = fa.State(name='q2', is_initial=False, is_final=False)
    q3 : fa.State = fa.State(name='q3', is_initial=False, is_final=True)
    
    t1 : fa.Transition = fa.Transition(source_state=q0, input_symbol="a", target_state=q1)
    t2 : fa.Transition = fa.Transition(source_state=q0, input_symbol="b", target_state=q0)
    t3 : fa.Transition = fa.Transition(source_state=q1, input_symbol="a", target_state=q2)
    t4 : fa.Transition = fa.Transition(source_state=q1, input_symbol="b", target_state=q0)
    t5 : fa.Transition = fa.Transition(source_state=q2, input_symbol="a", target_state=q2)
    t6 : fa.Transition = fa.Transition(source_state=q2, input_symbol="b", target_state=q3)
    t7 : fa.Transition = fa.Transition(source_state=q3, input_symbol="a", target_state=q3)
    t8 : fa.Transition = fa.Transition(source_state=q3, input_symbol="b", target_state=q3) 
    
    det_fa : dfa.DFA = dfa.DFA(alphabet=alphabet)
    det_fa.addStates({q0,q1,q2,q3})
    det_fa.addTransitions({t1,t2,t3,t4,t5,t6,t7,t8})
    
    print(det_fa)
    
    input_example : str = "abaabbba"
    
    
    print(f"Is input '{input_example}' valid: {det_fa.isValidInput(input_example)}")
    
    print("\n" + det_fa.getTabularFormat())

if __name__ == "__main__":
    main()