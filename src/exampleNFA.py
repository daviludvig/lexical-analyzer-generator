import model.nfa as nfa
import model.fa as fa

def build_nfa() -> nfa.NFA:
    alphabet : fa.Set[str] = {"a", "b", "&"}
    
    q0 : fa.State = fa.State(name='q0', is_initial=True, is_final=False)
    q1 : fa.State = fa.State(name='q1', is_initial=False, is_final=False)
    q2 : fa.State = fa.State(name='q2', is_initial=False, is_final=True)
    q3 : fa.State = fa.State(name='q3', is_initial=False, is_final=False)
    q4 : fa.State = fa.State(name='q4', is_initial=False, is_final=True)
    q5 : fa.State = fa.State(name='q5', is_initial=False, is_final=False)
    
    t1 : fa.Transition = fa.Transition(source_state=q0, input_symbol="&", target_state=q1)
    t2 : fa.Transition = fa.Transition(source_state=q0, input_symbol="&", target_state=q3)
    t3 : fa.Transition = fa.Transition(source_state=q0, input_symbol="&", target_state=q5) 
    t4 : fa.Transition = fa.Transition(source_state=q1, input_symbol="a", target_state=q2)
    t5 : fa.Transition = fa.Transition(source_state=q2, input_symbol="b", target_state=q4)
    t6 : fa.Transition = fa.Transition(source_state=q3, input_symbol="b", target_state=q4)
    
    no_det_fa : nfa.NFA = nfa.NFA(alphabet=alphabet)
    no_det_fa.addStates({q0,q1,q2,q3,q4,q5})
    no_det_fa.addTransitions({t1,t2,t3,t4,t5,t6})
    
    return no_det_fa

def main():
    
    no_det_fa : nfa.NFA = build_nfa()
    
    print(no_det_fa)
    
    input_example1 : str = "a"
    input_example2 : str = "ab"
    input_example3 : str = "b"
    input_example4 : str = "&"
    input_example5 : str = "aa"
    
    
    print(f"Is input '{input_example1}' valid: {no_det_fa.isValidInput(input_example1)}")  #resultado esperado: TRUE
    print(f"Is input '{input_example2}' valid: {no_det_fa.isValidInput(input_example2)}")  #resultado esperado: TRUE
    print(f"Is input '{input_example3}' valid: {no_det_fa.isValidInput(input_example3)}")  #resultado esperado: TRUE
    print(f"Is input '{input_example4}' valid: {no_det_fa.isValidInput(input_example4)}")  #resultado esperado: TRUE
    print(f"Is input '{input_example5}' valid: {no_det_fa.isValidInput(input_example5)}")  #resultado esperado: FALSE
    
    print("\n" + no_det_fa.getTabularFormat())

    print(no_det_fa._cloneWithPrefix("copy_"))

if __name__ == "__main__":
    main()