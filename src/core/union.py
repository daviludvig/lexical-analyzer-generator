import model.fa as fa
import model.nfa as nfa

def union(fa1: fa.FA, fa2: fa.FA) -> nfa.NFA:
    """
    Cria um novo autômato que aceita a união de duas linguagens aceitas por dois autômatos.

    Args:
        fa1 (FA): O primeiro autômato.
        fa2 (FA): O segundo autômato.

    Returns:
        NFA: Um novo autômato que aceita a união das linguagens de fa1 e fa2.
    """
    # Cria um novo autômato
    new_nfa = nfa.NFA(fa1.alphabet.union(fa2.alphabet))

    # Cria um novo estado inicial
    new_initial_state = fa.State(name="union_q0", is_final=False)
    new_nfa.addState(new_initial_state)

    # Adiciona todos os estados e transições do primeiro autômato
    new_nfa.addStates(fa1.states.copy())
    new_nfa.addTransitions(fa1.transitions.copy())

    # Adiciona todos os estados e transições do segundo autômato
    new_nfa.addStates(fa2.states.copy())
    new_nfa.addTransitions(fa2.transitions.copy())
    