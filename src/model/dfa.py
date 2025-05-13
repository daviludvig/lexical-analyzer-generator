from .fa import FA, State, Set

class DFA(FA):
    def __init__(self, alphabet : Set[str]) -> None:
        super().__init__(alphabet)
    
    def isValidInput(self, input_str: str) -> bool:
        if self.initial_state is None:
            raise ValueError("Estado inicial não definido.")

        current_state = self.initial_state
        for symbol in input_str:
            if symbol not in self.alphabet:
                raise ValueError(f"Símbolo inválido: {symbol}")

            found = False
            for transition in current_state.transitions:
                if transition.input_symbol == symbol:
                    current_state = transition.target_state
                    found = True
                    break
            if not found:
                return False
            
        return current_state.is_final
    
    def _find_state_by_name(self, name: str) -> State:
        for state in self.states:
            if state.name == name:
                return state
        raise ValueError(f"Estado '{name}' não encontrado.")