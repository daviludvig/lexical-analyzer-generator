class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        """
        Inicializa um Autômato Finito Não Determinístico (AFN)
        
        Args:
            estados: conjunto de estados do AFN
            alfabeto: conjunto de símbolos do alfabeto (sem incluir epsilon)
            transicoes: dicionário onde a chave é uma tupla (estado, símbolo) e o valor é um conjunto de estados destino
                        símbolo pode ser uma string normal ou 'ε' para transições epsilon
            estado_inicial: estado inicial do AFN
            estados_finais: conjunto de estados finais
        """
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        """
        Inicializa um Autômato Finito Determinístico (AFD)
        
        Args:
            estados: conjunto de estados do AFD
            alfabeto: conjunto de símbolos do alfabeto
            transicoes: dicionário onde a chave é uma tupla (estado, símbolo) e o valor é um único estado destino
            estado_inicial: estado inicial do AFD
            estados_finais: conjunto de estados finais
        """
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

def epsilon_fecho(afn, estado):
    """
    Calcula o epsilon-fecho de um estado em um AFN
    
    Args:
        afn: o autômato finito não determinístico
        estado: o estado para calcular o epsilon-fecho
        
    Returns:
        Um conjunto contendo todos os estados alcançáveis a partir do estado dado usando apenas transições epsilon
    """
    fecho = {estado}
    stack = [estado]
    
    while stack:
        atual = stack.pop()
        # Verifica se há transições epsilon a partir do estado atual
        proximos = afn.transicoes.get((atual, 'ε'), set())
        
        for proximo in proximos:
            if proximo not in fecho:
                fecho.add(proximo)
                stack.append(proximo)
                
    return fecho

def epsilon_fecho_conjunto(afn, estados):
    """
    Calcula o epsilon-fecho para um conjunto de estados
    
    Args:
        afn: o autômato finito não determinístico
        estados: conjunto de estados para calcular o epsilon-fecho
        
    Returns:
        União dos epsilon-fechos de todos os estados do conjunto
    """
    resultado = set()
    for estado in estados:
        resultado.update(epsilon_fecho(afn, estado))
    
    return resultado

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
    estado_inicial_afd = frozenset(epsilon_fecho(afn, afn.estado_inicial))
    
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
        for simbolo in afn.alfabeto:
            # Calcula o conjunto de estados alcançáveis usando o símbolo
            alcancaveis = mover(afn, estado_atual, simbolo)
            
            # Calcula o epsilon-fecho desses estados
            novo_estado = frozenset(epsilon_fecho_conjunto(afn, alcancaveis))
            
            # Se o novo estado não está vazio, adiciona a transição
            if novo_estado:
                transicoes_afd[(estado_atual, simbolo)] = novo_estado
                estados_afd.add(novo_estado)
    
    # Identifica os estados finais do AFD
    estados_finais_afd = {estado for estado in estados_afd if estado.intersection(afn.estados_finais)}
    
    # Converte os frozensets para identificadores de string para facilitar a leitura
    mapeamento_estados = {estado: f"q{i}" for i, estado in enumerate(estados_afd)}
    
    estados_afd_convertidos = set(mapeamento_estados.values())
    estado_inicial_afd_convertido = mapeamento_estados[estado_inicial_afd]
    estados_finais_afd_convertidos = {mapeamento_estados[estado] for estado in estados_finais_afd}
    
    transicoes_afd_convertidas = {}
    for (origem, simbolo), destino in transicoes_afd.items():
        transicoes_afd_convertidas[(mapeamento_estados[origem], simbolo)] = mapeamento_estados[destino]
    
    # Cria e retorna o AFD
    return AFD(
        estados_afd_convertidos,
        afn.alfabeto,
        transicoes_afd_convertidas,
        estado_inicial_afd_convertido,
        estados_finais_afd_convertidos
    )

def imprimir_afn(afn):
    """Imprime as informações do AFN de forma legível"""
    print("AFN:")
    print(f"  Estados: {afn.estados}")
    print(f"  Alfabeto: {afn.alfabeto}")
    print(f"  Estado Inicial: {afn.estado_inicial}")
    print(f"  Estados Finais: {afn.estados_finais}")
    print("  Transições:")
    
    for estado in sorted(afn.estados):
        for simbolo in sorted(list(afn.alfabeto) + ['ε']):
            destinos = afn.transicoes.get((estado, simbolo), set())
            if destinos:
                print(f"    δ({estado}, {simbolo}) = {destinos}")

def imprimir_afd(afd):
    """Imprime as informações do AFD de forma legível"""
    print("\nAFD:")
    print(f"  Estados: {afd.estados}")
    print(f"  Alfabeto: {afd.alfabeto}")
    print(f"  Estado Inicial: {afd.estado_inicial}")
    print(f"  Estados Finais: {afd.estados_finais}")
    print("  Transições:")
    
    for estado in sorted(afd.estados):
        for simbolo in sorted(afd.alfabeto):
            destino = afd.transicoes.get((estado, simbolo))