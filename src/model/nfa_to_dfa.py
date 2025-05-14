from .fa import FA, State, Set
import model.dfa as dfa
import model.nfa as nfa


#inspiração Claude AI

def mover(afn, estados, simbolo):
    """
    Calcula o conjunto de estados alcançáveis a partir de um conjunto de estados usando um símbolo específico
    
    Args:
        afn: o autômato finito não determinístico
        estados: conjunto de estados de origem
        simbolo: símbolo de entrada
        
    Returns:
        Conjunto de estados alcançáveis usando o símbolo dado
    """
    alcancaveis = set()
    
    for estado in estados:
        alcancaveis.update(afn.transicoes.get((estado, simbolo), set()))
        
    return alcancaveis

def converter_afn_para_afd(afn):
    """
    Converte um AFN com transições epsilon em um AFD
    
    Args:
        afn: o autômato finito não determinístico com transições epsilon
        
    Returns:
        Um AFD equivalente ao AFN dado
    """
    # Calcula o epsilon-fecho do estado inicial do AFN
    estado_inicial_afd = frozenset(nfa.epsilon_closure({nfa.initial_state}))
    
    # Inicializa as estruturas para o AFD
    estados_afd = {estado_inicial_afd}
    estados_marcados = set()
    transicoes_afd = {}
    
    # Algoritmo de construção de subconjuntos
    while estados_afd - estados_marcados:
        # Pega um estado não marcado
        estado_atual = next(iter(estados_afd - estados_marcados))
        estados_marcados.add(estado_atual)
        
        # Para cada símbolo do alfabeto
        for simbolo in nfa.alfabeto:
            # Calcula o conjunto de estados alcançáveis usando o símbolo
            alcancaveis = mover(nfa, estado_atual, simbolo)
            
            # Calcula o epsilon-fecho desses estados
            novo_estado = frozenset(nfa.epsilon_closure(alcancaveis))
            
            # Se o novo estado não está vazio, adiciona a transição
            if novo_estado:
                transicoes_afd[(estado_atual, simbolo)] = novo_estado
                estados_afd.add(novo_estado)


    # MUITOS AJUSTES PARA O FORMATO ADEQUADO AQUI
    # Identifica os estados finais do AFD
    estados_finais_afd = {estado for estado in estados_afd if estado.intersection(nfa.final_states)}
    
    # Converte os frozensets para identificadores de string para facilitar a leitura
    mapeamento_estados = {estado: f"q{i}" for i, estado in enumerate(estados_afd)}
    
    estados_afd_convertidos = set(mapeamento_estados.values())
    estado_inicial_afd_convertido = mapeamento_estados[estado_inicial_afd]
    estados_finais_afd_convertidos = {mapeamento_estados[estado] for estado in estados_finais_afd}
    
    transicoes_afd_convertidas = {}
    for (origem, simbolo), destino in transicoes_afd.items():
        transicoes_afd_convertidas[(mapeamento_estados[origem], simbolo)] = mapeamento_estados[destino]
    
    # Cria dfa e retorna

    det_fa : dfa.DFA = dfa.DFA(alphabet=alphabet)
    det_fa.addStates({q0,q1,q2})
    det_fa.addTransitions({t1,t2,t3})
    return DFA(
        estados_afd_convertidos,
        afn.alfabeto,
        transicoes_afd_convertidas,
        estado_inicial_afd_convertido,
        estados_finais_afd_convertidos
    )