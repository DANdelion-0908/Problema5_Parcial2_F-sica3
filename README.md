# Problema 5

## Requisitos

Para que el programa funcione correctamente, es necesario instalar Python desde Microsoft Store o su página oficial y los siguientes módulos mediante el comando "pip install":

- pillow

## Descripción

Implementar un programa que permita colocar una plano infinito o esfera cargados negativamente (carga uniforme) y que permita disparar una partícula positiva desde su superficie, en dirección perpendicular a la esfera o plano, y que muestre cuánto es lo más que logra alejarse antes de volver a caer al plano o esfera. El programa debe calcular y colocar en algún lugar visible la velocidad de escape para la esfera. Esta velocidad es a la cual la partícula ya no volverá a regresar. Se tiene que poder comprobar esa velocidad de escape disparando partículas con esa velocidad (o mayor) y ver que ya no vuelve a caer. El programa debe prohibir ingresar una velocidad inicial a la partícula móvil que sea mayor que la de la luz en el vacío. El programa debe indicar cuando la esfera se ha convertido en un “agujero negro” electrostático. Al simular la distancia máxima de alejamiento el programa debe mostrar esta cantidad en metros.

## Parámetros de entrada

- Tipo de carga central fija (esfera o plano).
- Para la esfera pedir radio y carga (distribuida homogéneamente).
- Para el plano pedir la densidad superficial de carga.
- Carga, masa y rapidez inicial de la partícula móvil.

## Parámetros de salida

- Distancia de máximo alejamiento en metros.
- Para la esfera, la velocidad de escape o bien, si la esfera se ha convertido en un agujero negro electrostático.

### Bono: que puedan dispararse partículas conocidas como protones, positrones, partículas alfa. Núcleos de algunos átomos. Mínimo 5 distintos [COMPLETADO]
