# Code based on: https://viterbi-web.usc.edu/~breichar/teaching/2011cs360/NFAtoDFA.py
# Adapted by: Bruno, Davi, Julia Gazolla


import model.fa as fa
import model.dfa as dfa
import model.nfa as nfa
from functools import reduce  # necessário para usar reduce

def NFAtoDFA(nfa: nfa.FA) -> dfa.DFA:
    """Converts the input NFA into a DFA.  

    The output DFA has a state for every *reachable* subset of states in the input NFA.  
    In the worst case, there will be an exponential increase in the number of states.
    """

    # Cria o DFA com alfabeto sem &
    # afd = dfa.AFD(nfa.alphabet.discart("&"))

    # Cria um frozenset do e-fecho de estado inicial para poder usar como chave em dicionários
    qo_closure = nfa.epsilon_closure([nfa.initial_state])
    q0 = frozenset(qo_closure)  # frozensets are hashable, so can key the delta dictionary

    Q = set([q0])
    unprocessedQ = Q.copy()  # unprocessedQ tracks states for which delta is not yet defined

    # Transições
    delta = {}

    # Estados finais
    F = []

    # Enquanto os estados não forem marcados
    while unprocessedQ: 
        
        # Retira um conj de estados dos que não foram marcados e processa
        qSet = unprocessedQ.pop()

        # Transições daquele estado vazias
        delta[qSet] = {}

        # Para cada elemento do alfabeto do NFA
      
        for a in nfa.alphabet:
            if a != "&":
                moveResult = set()
                for q in qSet:
                    try:
                        moveResult |= nfa.deltaHat(q,a)
                    except KeyError:
                        pass
                nextStates = frozenset(nfa.epsilon_closure(moveResult))
                delta[qSet][a] = nextStates
                if nextStates not in Q:
                    Q.add(nextStates)
                    unprocessedQ.add(nextStates)

    for qSet in Q: 
        # Verifica se o estado final da NFA está naquele novo estado
        if (qSet & nfa.final_states): 
            F.append(qSet)

	# Aqui vou ter: 
	# Q - set de todos os estados, com diversos frozensets, que são combinação de estados da NFA
    # F - set de todos estados finais
    # delta [estado] [simbolo do alfabeto]

    #Cria DFA
    DFA_alphabet = nfa.alphabet - {"&"}
    
    final_DFA = dfa.DFA(DFA_alphabet)
    DFA_states = set()
    DFA_transitions = set()
    states_list = list()
    i = 0
    # Cria objetos estado da DFA
    for j, subset in enumerate(Q):

        is_initial = (subset == q0)
        is_final = bool(subset & nfa.final_states)

        if len(subset) > 0:
            qi = fa.State(name='q' + str(i), is_initial=is_initial, is_final=is_final)

            DFA_states.add(qi)
            states_list.append((qi,subset))
            i+=1

    #Transições DFA - precisa mapear Delta
    # Set -> ordem não é garantida
    for subset in Q:

        for s in DFA_alphabet:
            # Se aquele conjunto é vazio, passa para o proximo
            if (subset) == frozenset():
                continue
            # Se a transição leva para um vazio, passa para o proximo
            if delta[subset][s] == frozenset():
                continue

            # Para cada tupla na lista
            for state_tuple in states_list:
                
                if subset in state_tuple:
                    source_state = state_tuple[0]
                if delta[subset][s] in state_tuple:
                    target_state = state_tuple[0]
            


            ti : fa.Transition = fa.Transition(source_state=source_state, input_symbol=s, target_state=target_state)
            DFA_transitions.add(ti)

    
    final_DFA.addStates(DFA_states)
    final_DFA.addTransitions(DFA_transitions)


    return final_DFA
