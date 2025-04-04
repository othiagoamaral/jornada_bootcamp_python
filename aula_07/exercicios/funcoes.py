from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado