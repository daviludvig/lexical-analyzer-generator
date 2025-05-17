from typing import Union
from .fa import FA, State, Set

class NFA(FA):

    def __init__(self, alphabet : Set[str]) -> None:
        super().__init__(alphabet)
        self.epsilon = "&"

    # Calcula o fecho-epsilon de um conjunto de estados
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
    
    def getDestinationStatesFromTransition(self, source_state : Union[State, str], symbol : str) -> Set[State]:
        source_state_obj = source_state
        if isinstance(source_state, str):
            source_state_obj = self._find_state_by_name(source_state)
        return {t.target_state for t in self.transitions
            if t.source_state == source_state_obj and t.input_symbol == symbol}
    
    def deltaHat(self, states: Union[State, Set[State]], symbol: str) -> Set[State]:
        """
        Calcula o conjunto de estados alcançáveis a partir de um estado ou conjunto de estados,
        ao consumir um único símbolo do alfabeto, considerando transições-ε antes e depois.
        """
        if symbol not in self.alphabet:
            raise ValueError(f"Símbolo inválido: {symbol}")
        
        # Garante que 'states' seja um conjunto
        if isinstance(states, State):
            states = {states}

        # Aplica o fecho-epsilon inicial
        current_states = self.epsilon_closure(states)
        print( "[DEBUG] ", "ε-fecho inicial:", current_states)

        # Realiza as transições pelo símbolo
        next_states = set()
        for st in current_states:
            destinations = self.getDestinationStatesFromTransition(st, symbol)
            print( "[DEBUG] ", f"Transições de {st} com símbolo '{symbol}': {destinations}")
            next_states.update(destinations)

        # Aplica o fecho-epsilon final
        result_states = self.epsilon_closure(next_states)
        print( "[DEBUG] ", "ε-fecho após transições:", result_states)

        return result_states

    '''
    
    def deltaHat(self, state, inputString):
        """
    Calcula o conjunto de estados alcançáveis a partir de um estado dado
    ao consumir uma string de entrada, incluindo transições-ε entre os símbolos.
    """
        states = self.epsilon_closure({state})  # começa com fecho-epsilon do estado inicial

        print( "[DEBUG] ", "epsilom fecho ", state, " " , states)

        for symbol in inputString:
            if symbol not in self.alphabet:
                raise ValueError(f"Símbolo inválido: {symbol}")

            next_states = set()
            for st in states:
                destinations = self.getDestinationStatesFromTransition(st, symbol)
                print( "[DEBUG] ", "destinations: ", st, symbol, "->", destinations)
                next_states.update(destinations)

            states = self.epsilon_closure(next_states)

        return states
    
    def deltaHatSet(self, states: Set[State], inputString: str) -> Set[State]:
        result = set()
        for state in states:
            result |= self.deltaHat(state, inputString)
        return result

        '''