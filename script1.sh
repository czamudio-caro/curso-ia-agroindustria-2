#!/bin/bash

# 1. Crear la carpeta llamada 'carpeta1'
# Usamos -p para que no dé error si la carpeta ya existe
mkdir -p carpeta1

# 2. Crear un archivo dentro de esa carpeta y guardar la lista de archivos
# El comando 'ls /' lista la raíz. 
# El operador '>' redirige esa lista al archivo especificado.
ls / > carpeta1/lista_raiz.txt

# 3. Confirmación visua
echo "Proceso finalizado con éxito."
echo "Se ha creado 'carpeta1' y el archivo 'lista_raiz.txt' con el contenido."
