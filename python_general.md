# Python General
---

# NumPy

```{python}
X = np.empty((1024, 1024, 1024, 3000))
```

Está creando un arreglo multidimensional (o tensor) con las dimensiones especificadas utilizando NumPy. Veamos lo que está pasando en detalle:

`np.empty()`: Esta función crea un arreglo sin inicializar. Esto significa que se reservará un bloque de memoria del tamaño especificado, pero los valores iniciales del arreglo serán basura (lo que sea que esté en la memoria en ese momento). No se inicializan explícitamente a ceros o cualquier otro valor.

El tamaño del arreglo está determinado por las dimensiones que pasas como argumento: (1024, 1024, 1024, 3000).
- Primera dimensión (1024): El arreglo tendrá 1024 elementos en la primera dimensión. 
- Segunda dimensión (1024): Cada uno de esos 1024 elementos tendrá 1024 subelementos.
- Tercera dimensión (1024): Cada uno de esos subelementos tendrá 1024 subsubelementos.
- Cuarta dimensión (3000): Finalmente, cada subsubelemento tendrá 3000 valores.

En total, el arreglo tendría 1024 x 1024 x 1024 x 3000 elementos.

> **Cálculo del tamaño total**
El número total de elementos en este arreglo sería:
1024×1024×1024×3000=3,221,225,472,000 elementos

> **Tamaño en memoria**
El tamaño en memoria dependerá del tipo de dato de los elementos del arreglo. Si `np.empty()` está usando el tipo de dato por defecto (float64), cada elemento ocupa 8 bytes (un valor de punto flotante de 64 bits). Por lo tanto, el tamaño total en memoria sería:
3,221,225,472,000 elementos×8 bytes por elemento=25,769,803,776,000 bytes≈25.8 terabytes

# Python basico

- La libreria re permite trabajar con expresiones regulares.
Por ejemplo, para quitar los simbolos como los puntos, etc.

```{python}
import re
from typing import List

def frase_a_tokens(frase: str) -> List[str]:
    # Usar una expresión regular para eliminar los símbolos especiales
    frase_limpia = re.sub(r"[^a-zA-Z0-9\s]", "", frase)
    
    # Las palabras se separan por espacios
    lista_de_palabras: List[str] = frase_limpia.split()
    
    return lista_de_palabras
```

- Los exponentes se evaluan de derecha a izquierda.
```{python}
2 ** 3 ** 2 ** 1
```

# Fechas

- Para pasar de datetime a string.
```{python}
import datetime

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")
```

- Para pasar de string a datetime.
```{python}
import datetime

date_str = "2022-01-01 12:00:00"
date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
```

- Para obtener el timestamp.
```{python}
import datetime

now = datetime.datetime.now()
timestamp = datetime.datetime.timestamp(now)
```

- Para pasar de timestamp a string.
```{python}
import datetime

timestamp = 1640995200
date = datetime.datetime.fromtimestamp(timestamp)
date.strftime("%Y-%m-%d %H:%M:%S")
```

- Como restar a una fecha un timedelta.
```{python}
import datetime

date = datetime.datetime.now()
delta = datetime.timedelta(days=1)
new_date = date - delta
```

