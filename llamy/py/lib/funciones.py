# /llamy/py/lib/funciones.py

from llamy import (
    np
)

__all__ = (
    'Activacion'   
)

class Activacion:
    
    @staticmethod
    def heaviside(n: float) -> int:
        return 1 if n >= 0 else 0
    
    @staticmethod
    def sigmoide(x):
        return 1 / (1 + np.exp(-x))
    
    @staticmethod
    def sigmoide_derivada(x):
        sig = 1 / (1 + np.exp(-x))
        return sig * (1 - sig)

    @staticmethod
    def relu(x):
        return np.maximum(0, x)
    
    @staticmethod
    def relu_derivada(x):
        return np.where(x > 0, 1, 0)