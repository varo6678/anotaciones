#!/usr/bin/env python3

# dnn.py

# internos.
import numpy as np

# externos.
from llamy.py.core._typing import *


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
    

    

class Perceptron:
    """
    Perceptrón con soporte para retropropagación.
    """
    
    def __init__(
        self, 
        funcion_activacion, 
        funcion_activacion_derivada, 
        tolerancia: float = 1e-3
        ) -> None:
        
        self.funcion_activacion = funcion_activacion
        self.funcion_activacion_derivada = funcion_activacion_derivada
        self.tolerancia = tolerancia
        self.w = None
        self.bias = None

    def __call__(self, input: np.ndarray, random_bias: bool = True) -> np.ndarray:
        
        self.input = input
        
        # Inicializar pesos con inicialización Xavier/Glorot
        self.w = np.random.rand(*input.shape)
        
        if random_bias:
            self.bias = np.random.uniform(0,1)
        else:
            self.bias = 0.0

        # Forward: Producto de los pesos con las entradas, más el sesgo
        self.z = self.mul(self.w, self.input) + self.bias
        
        # Aplicar la función de activación
        self.output = self.funcion_activacion(self.z)
        
        return self.output

    
    def backward(self, d_output, tasa_aprendizaje):
        """
        Calcula la retropropagación y ajusta los pesos.
        """
        # Derivada del error con respecto a z (antes de la activación)
        d_z = d_output * self.funcion_activacion_derivada(self.z)
        
        # Gradiente de los pesos
        d_w = d_z * self.input
        d_bias = d_z

        # Actualización de los pesos y bias
        self.w -= tasa_aprendizaje * d_w
        self.bias -= tasa_aprendizaje * d_bias
        
        # Devolver el error para la capa anterior (gradiente con respecto a la entrada)
        return d_z * self.w

    def mul(self, inputs: np.ndarray, weights: np.ndarray) -> np.ndarray:
        return np.dot(weights.T, inputs)

    
class CapaPerceptron:
    """
    Clase para representar una capa de perceptrones en una red neuronal multicapa.
    """
    def __init__(self, n_neuronas: int, n_entradas: int, funcion_activacion=None, funcion_activacion_derivada=None):
        # Crear una lista de perceptrones (uno por cada neurona en la capa)
        self.neuronas = [
            Perceptron(funcion_activacion=funcion_activacion, funcion_activacion_derivada=funcion_activacion_derivada)
            for _ in range(n_neuronas)
        ]
    
    def forward(self, entradas: np.ndarray) -> np.ndarray:
        """
        Calcula la salida de la capa aplicando cada perceptrón a las entradas.
        """
        # Almacena las salidas de cada neurona (perceptrón)
        salidas = []
        for neurona in self.neuronas:
            salida_neurona = neurona(entradas)
            salidas.append(salida_neurona)
        return np.array(salidas)
    
    def backward(self, d_output: np.ndarray, tasa_aprendizaje: float):
        """
        Retropropaga el error a través de la capa.
        """
        # Crear una lista para acumular los gradientes que se propagan hacia la capa anterior
        d_inputs = np.zeros((len(self.neuronas), len(self.neuronas[0].input)))
        
        for i, neurona in enumerate(self.neuronas):
            # Realizamos la retropropagación para cada neurona
            d_inputs[i] = neurona.backward(d_output[i], tasa_aprendizaje)
        
        # Devolver la suma de los gradientes con respecto a las entradas
        return np.sum(d_inputs, axis=0)



class MLP:
    """
    Clase que representa una red neuronal multicapa usando perceptrones.
    """
    def __init__(self, capas: list):
        # Lista de capas que forman la red
        self.capas = capas
    
    def forward(self, entradas: np.ndarray) -> np.ndarray:
        """
        Realiza una pasada hacia adelante a través de todas las capas.
        """
        salida = entradas
        for capa in self.capas:
            salida = capa.forward(salida)
        return salida
    
    def backward(self, d_output: np.ndarray, tasa_aprendizaje: float):
        """
        Retropropaga el error a través de todas las capas.
        """
        for capa in reversed(self.capas):
            d_output = capa.backward(d_output, tasa_aprendizaje)


if __name__ == '__main__':
    
    # Crear las capas usando perceptrones con función ReLU y inicialización Xavier para la primera capa
    capa_1 = CapaPerceptron(n_neuronas=3, n_entradas=1, funcion_activacion=Activacion.relu, funcion_activacion_derivada=Activacion.relu_derivada)
    
    # Usamos la función identidad en la última capa (sin activación)
    capa_2 = CapaPerceptron(n_neuronas=1, n_entradas=3, funcion_activacion=lambda x: x, funcion_activacion_derivada=lambda x: 1)

    # Crear el MLP con dos capas
    mlp = MLP(capas=[capa_1, capa_2])

    # Datos de entrada (x) y salida esperada (y = 2x + 1) para la regresión
    entradas = np.array([[0], [1], [2], [3], [4], [5]])
    salidas_esperadas = np.array([[1], [3], [5], [7], [9], [11]])  # y = 2x + 1

    # Parámetros de entrenamiento
    tasa_aprendizaje = 0.001  # Reducimos la tasa de aprendizaje
    epochs = 50000  # Aumentamos el número de epochs

    # Entrenamiento
    for epoch in range(epochs):
        total_error = 0
        for entrada, salida_esperada in zip(entradas, salidas_esperadas):
            # Forward pass
            salida = mlp.forward(entrada)
            
            # Cálculo del error (diferencia entre la salida esperada y la obtenida)
            error = salida_esperada - salida
            
            # Backward pass (retropropagación)
            mlp.backward(error, tasa_aprendizaje)
            
            # Acumular el error cuadrático medio
            total_error += np.sum(error ** 2)
        
        # Mostrar el error cada 1000 epochs
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Error: {total_error}")

    # Prueba final
    print("\nResultados finales de regresión:")
    for entrada in entradas:
        salida = mlp.forward(entrada)
        print(f"Entrada: {entrada}, Salida predicha: {salida}")







