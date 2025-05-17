# Code based on: https://viterbi-web.usc.edu/~breichar/teaching/2011cs360/NFAtoDFA.py
# Adapted by: Bruno, Davi, Julia Gazolla


import model.fa as fa
import model.dfa as dfa
import model.nfa as nfa
from functools import reduce  # necessário para usar reduce

def NFAtoDFAconversion(nfa: nfa.FA) -> dfa.DFA:
    """Converts the input NFA into a DFA.  

    The output DFA has a state for every *reachable* subset of states in the input NFA.  
    In the worst case, there will be an exponential increase in the number of states.
    """

    # Cria o DFA com alfabeto sem &
    # afd = dfa.AFD(nfa.alphabet.discart("&"))

    # Cria um frozenset para poder usar como chave em dicionários
    q0 = frozenset([nfa.initial_state])  # frozensets are hashable, so can key the delta dictionary

    Q = set([q0])
    unprocessedQ = Q.copy()  # unprocessedQ tracks states for which delta is not yet defined

    # Transições
    delta = {}

    # Estados finais
    F = []

    # Enquanto os estados não forem marcados
    while len(unprocessedQ) > 0: 
        # Retira um conj de estados dos que não foram marcados e processa
        qSet = unprocessedQ.pop()

        # Transições daquele estado vazias
        delta[qSet] = {}

        # Para cada elemento do alfabeto do NFA
        for s in nfa.alphabet: 
            # Obtém todos estados alcançáveis com símbolo s
            nextStates = reduce(lambda x, y: x | y, [nfa.deltaHat(q, s) for q in qSet])
            nextStates = frozenset(nextStates)

            # Transição do estado atual pelo símbolo vai para próximo estado
            delta[qSet][s] = nextStates

            # Se o estado identificado não existe ainda, será adicionado aos estados finais e aos não marcados
            if nextStates not in Q: 
                Q.add(nextStates)
                unprocessedQ.add(nextStates)

    for qSet in Q: 
        # Verifica se o estado final da NFA está naquele novo estado
        if (qSet & nfa.F): 
            F.append(qSet)

	# Aqui vou ter: 
	# Q - set de todos os estados, com diversos frozensets, que são combinação de estados da NFA
    # F - set de todos estados finais
    # delta [estado] [simbolo do alfabeto]

    #M = dfa.DFA(delta, q0, F)

    return Q, F




