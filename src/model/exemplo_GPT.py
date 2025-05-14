from collections import defaultdict, deque
from typing import Set, Dict, FrozenSet

# Sem minhas classes exemplos.

class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto  # o alfabeto NÃO inclui 'ε'
        self.transicoes = transicoes  # Dict[estado, Dict[simbolo, Set[estados]]]
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def fechamento_epsilon(self, estado):
        """Retorna o ε-fechamento de um estado como um conjunto de estados."""
        stack = [estado]
        fechamento = set([estado])

        while stack:
            atual = stack.pop()
            for destino in self.transicoes.get(atual, {}).get('ε', []):
                if destino not in fechamento:
                    fechamento.add(destino)
                    stack.append(destino)
        return fechamento

    def fechamento_epsilon_conjunto(self, estados):
        """Retorna o ε-fechamento de um conjunto de estados."""
        resultado = set()
        for estado in estados:
            resultado |= self.fechamento_epsilon(estado)
        return resultado


class AFD:
    def __init__(self):
        self.estados: Set[FrozenSet[str]] = set()
        self.alfabeto = set()
        self.transicoes: Dict[FrozenSet[str], Dict[str, FrozenSet[str]]] = {}
        self.estado_inicial: FrozenSet[str] = frozenset()
        self.estados_finais: Set[FrozenSet[str]] = set()

    def mostrar(self):
        print("Estados (AFD):", self.estados)
        print("Estado inicial:", self.estado_inicial)
        print("Estados finais:", self.estados_finais)
        print("Transições:")
        for estado, trans in self.transicoes.items():
            for simbolo, destino in trans.items():
                print(f"  {estado} --{simbolo}--> {destino}")


def converter_afn_para_afd(afn: AFN) -> AFD:
    afd = AFD()
    afd.alfabeto = afn.alfabeto

    inicial_afd = frozenset(afn.fechamento_epsilon(afn.estado_inicial))
    afd.estado_inicial = inicial_afd

    fila = deque()
    fila.append(inicial_afd)
    afd.estados.add(inicial_afd)

    while fila:
        atual = fila.popleft()
        afd.transicoes[atual] = {}

        for simbolo in afn.alfabeto:
            destinos = set()
            for estado in atual:
                trans = afn.transicoes.get(estado, {}).get(simbolo, set())
                destinos |= afn.fechamento_epsilon_conjunto(trans)

            if destinos:
                destino_frozenset = frozenset(destinos)
                afd.transicoes[atual][simbolo] = destino_frozenset

                if destino_frozenset not in afd.estados:
                    afd.estados.add(destino_frozenset)
                    fila.append(destino_frozenset)

    for estado in afd.estados:
        if any(s in afn.estados_finais for s in estado):
            afd.estados_finais.add(estado)

    return afd

# Exemplo de uso:

estados = {'q0', 'q1', 'q2'}
alfabeto = {'a', 'b'}
transicoes = {
    'q0': {'ε': {'q1', 'q2'}},
    'q1': {'a': {'q1'}, 'b': {'q1'}},
    'q2': {'b': {'q2'}}
}
estado_inicial = 'q0'
estados_finais = {'q1'}

afn = AFN(estados, alfabeto, transicoes, estado_inicial, estados_finais)
afd = converter_afn_para_afd(afn)
afd.mostrar()


## com meus codigos
def convert_nfa_to_dfa(nfa: NFA) -> DFA:
    from collections import deque

    dfa = DFA(nfa.alphabet)
    state_map: Dict[frozenset, State] = {}  # Conjuntos de estados NFA → estados DFA
    queue = deque()

    # Estado inicial do DFA é o fecho-ε do inicial do NFA
    start_closure = frozenset(nfa.epsilon_closure({nfa.initial_state}))
    dfa_start = State(name=",".join(sorted(s.name for s in start_closure)), is_initial=True,
                      is_final=any(s.is_final for s in start_closure))
    dfa.addState(dfa_start)
    state_map[start_closure] = dfa_start
    queue.append(start_closure)

    while queue:
        current_set = queue.popleft()
        current_dfa_state = state_map[current_set]

        for symbol in nfa.alphabet:
            if symbol == nfa.epsilon:
                continue

            # Conjunto de estados alcançados com esse símbolo
            move_set = set()
            for state in current_set:
                for transition in state.transitions:
                    if transition.input_symbol == symbol:
                        move_set.add(transition.target_state)

            if not move_set:
                continue

            # Fecho-ε dos estados alcançados
            closure = frozenset(nfa.epsilon_closure(move_set))

            if closure not in state_map:
                new_state = State(
                    name=",".join(sorted(s.name for s in closure)),
                    is_initial=False,
                    is_final=any(s.is_final for s in closure)
                )
                dfa.addState(new_state)
                state_map[closure] = new_state
                queue.append(closure)

            # Adiciona a transição no DFA
            transition = Transition(
                source_state=current_dfa_state,
                input_symbol=symbol,
                target_state=state_map[closure]
            )
            dfa.addTransition(transition)

    return dfa
