from .fa import FA, State, Set
from typing import Union

class DFA(FA):
    def __init__(self, alphabet : Set[str]) -> None:
        super().__init__(alphabet)
    
    def isValidInput(self, input_str: str) -> bool:
        if self.initial_state is None:
            raise ValueError("Estado inicial não definido.")

        current_state = self.initial_state
        for symbol in input_str:
            if symbol not in self.alphabet:
                return False  # Anteriormente lançava erro

            found = False
            for transition in current_state.transitions:
                if transition.input_symbol == symbol:
                    current_state = transition.target_state
                    found = True
                    break
            if not found:
                return False
            
        return current_state.is_final
    
    
    def getDestinationStateFromTransition(self, source_state : Union[State, str], symbol : str) -> State:
        source_state_obj = source_state
        if isinstance(source_state, str):
            source_state_obj = self._find_state_by_name(source_state)
        for transition in self.transitions:
            if transition.source_state == source_state_obj and transition.input_symbol == symbol:
                return transition.target_state
        return None