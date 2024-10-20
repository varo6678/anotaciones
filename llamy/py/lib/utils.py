# /llamy/py/lib/utils.py

from llamy.py.core._typing import *
from llamy import (
    re,
    requests
)

__all__ = (
    'tokenizador',
    'creador_de_vocabulario',
    'obtener_texto_desde_url'    
)

def tokenizador(texto: str) -> List[str]:
    
    """
    Lo que hace es separar el texto.
    Lo convierte en una lista de palabras, estas no tienen por que ser unicas.
    """
    
    # Limpiar texto de símbolos especiales y convertir a minúsculas.
    texto_limpio = re.sub(r"[^a-zA-Z0-9\s]", "", texto)
    return texto_limpio.lower().split()

def creador_de_vocabulario(lista_de_tokens: List[str]) -> Dict[str, int]:
    
    """
    Crear vocabulario asignando un índice único a cada palabra.
    Luego el resultado si contendra palabras unicas.
    """
    
    # Crear vocabulario asignando un índice único a cada palabra
    return {palabra : indice for indice, palabra in enumerate(set(lista_de_tokens))}

def obtener_texto_desde_url(url: str) -> str:
    
    """
    Ejemplo de uso:
    >>> url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    >>> texto = obtener_texto_desde_url(url)
    >>> print(texto[:500])
    """
    
    try:
        # Hacer una solicitud GET a la URL.
        respuesta = requests.get(url)
        # Verificar si la solicitud fue exitosa (codigo 200).
        respuesta.raise_for_status()
        # Retornar el contenido como texto.
        return respuesta.text
    except requests.exceptions.RequestException as e:
        # Manejar cualquier error de conexión o de HTTP
        print(f"Error al intentar descargar el archivo: {e}")
        return ""
