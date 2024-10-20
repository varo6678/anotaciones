# /llamy/__init__.py

# externos.
import numpy as np
import re
import requests

# internos.
from llamy.__version__ import __version__
from llamy.py.lib.utils import (
    obtener_texto_desde_url,
    tokenizador,
    creador_de_vocabulario
)