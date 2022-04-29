#Modulo principal en la cual se uniran todos los modulos

"""
***Proceso para ocultar texto en pixeles
Desde esta clase se le entrega un arreglo con los bits que conforman al # del correspondiente caracter
Si el # es pequeno, seguramente ocupara menos de ocho bits, pero para evitar problemas a la hora de querer recuperar el mensaje se entregara siempre numeros de 8 bits
En la clase principal, teniendo dicho arreglo, se encargara de esconder hasta 4 bits dentro del LSB de cada pixel
Asi hasta que se termine el mensaje
"""

"""
**Proceso para leer mensajes 
Capta los primeros 8 bits de la imagen
De ellos, lee su LSB y los guarda en un string para al final entregar su caracter correspondiente
Repite este proceso hasta que se acaben los bits o el mensaje termine...
"""