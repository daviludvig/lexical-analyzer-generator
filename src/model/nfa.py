from .fa import FA, State, Set

class NFA(FA):

    def __init__(self, alphabet : Set[str]) -> None:
        super().__init__(alphabet)
        self.epsilon = "&"

    #Calcula o fecho-epsilon de um conjunto de estados
    def epsilon_closure(self, states: Set[State]) -> Set[State]:
        
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            for transition in state.transitions:
                if transition.input_symbol == self.epsilon and transition.target_state not in closure:
                    closure.add(transition.target_state)
                    stack.append(transition.target_state)
        return closure

    def isValidInput(self, input_str: str) -> bool:
        if self.initial_state is None:
            raise ValueError("Estado inicial não definido.")

        # Começa com o fecho-epsilon do estado inicial
        current_states = self.epsilon_closure({self.initial_state})

        for symbol in input_str:
            if symbol not in self.alphabet:
                raise ValueError(f"Símbolo inválido: {symbol}")

            found = False
            next_states = set()
            for state in current_states:
                for transition in state.transitions:
                    if transition.input_symbol == symbol:
                        next_states.add(transition.target_state)
                        # Aplica o fecho-epsilon nos estados alcançados
            
            current_states = self.epsilon_closure(next_states)
            
            if next_states:
                found = True
                        
                
            if not found:
                return False
            
        return any(state.is_final for state in current_states)
    
    def _find_state_by_name(self, name: str) -> State:
        for state in self.states:
            if state.name == name:
                return state
        raise ValueError(f"Estado '{name}' não encontrado.")