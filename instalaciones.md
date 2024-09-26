# Instalaciones
---

## Como instalar `miniconda3`?

1. Primero descargo.

```{bash}
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2. Le cambio los permisos.

```{bash}
chmod u+x ./Miniconda3-latest-Linux-x86_64.sh
```

3. Ejecuto.

```{bash}
./Miniconda3-latest-Linux-x86-64.sh
```

4. Añadir conda al `PATH`:

- `nano ~/.bashrc`
- `export PATH='/home/.../miniconda3/bin:$PATH'`
- `source ~/.bashrc`
