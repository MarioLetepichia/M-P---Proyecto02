# Proyecto 2 Modelado y Programación - Esteganografia por LSB
Repositorio correspondiente al Proyecto 2 de Modelado y Programacion


Proyecto 2 Modelado y Programación - Esteganografía por el método LSB
---
### Contribuidores

-  Mario Letepichia Romero  (MarioLetepichia) 
-  Celic Aislinn Liahut Ley  (Aislinn-Liahut) 
-  Ivette González Mancera   (Ivette612)

---

## Instalaciones y prerequisitos:

1. **Instalar python (version 3+)**
Para verificarlo usa 
```bash
python3 --version
```

2. **Instalar opencv en python**

```bash
pip install opencv-python
```
 
 Lo anterior para poder realizar los requests a las APIs 

 3. **Instalar Pillow** 

```bash
pip install Pillow
```

 4. **Instalar pytest**
```bash
sudo apt install python-pytest
```



## Instrucciones para compilar y obtener la salida:
1. Ya que realizaste los prerequisitos anteriores colocate en el directorio MP_Proyecto02:
```bash
cd 
```

2. Ejecuta las siguientes instrucciones para correr el programa,hay dos opciones  

### Correrarlo con la interfaz
```bash
python3 src/userInterface.py
```
Una vez hecho, se abrira una interfaz lista para usar el programa (siguie las indicaciones para el buen uso del programa)

### Correrlo en la terminal compilación para _main.py_

Si se quiere evitar lidiar con la interfaz gráfica puede optar por correr el archivo _main.py_ en su lugar; ubicandose en el directorio __Proyecto02__ y ejecutando el siguiente comando:

````
python3 src/main.py <opcion> [direcciones]
````

Dependiendo la opcion específicada las direcciones requeridas pueden variar, siendo la opción __h__ para ocultar un mensaje:
```
h <texto> <imagen> <imagenResultante>
```
Y usamos la opción __u__ para develar un mensaje oculto:
````
u <imagenDevelar> <textoResultante>
````
Como estos parámetros son requeridos al mismo tiempo que se ejecuta el programa, los archivos generados se guardan automáticamente en las direcciones proporcionadas.




## Instrucciones para correr pruebas:

Colocate en el directorio del codigo fuente  MP_Proyecto02 y ejecuta el siguiente comando:

```bash
pytest
```

## Observaciones extras
- Los detalles del proyecto se encuentran en Proyecto02.pdf ubicado en el directorio __docs__.

-El caracter apostrofe "´" se omite al enseñar el mesaje ya que se neceitas 16 bits para ser representado.
