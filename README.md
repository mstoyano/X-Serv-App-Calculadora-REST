# X-Serv-App-Calculadora-REST
Ejercicio de asignaturas de aplicaciones web. Servicios que interoperan. Calculadora simple versión REST.

## Enunciado

Realizar una calculadora de las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división), siguiendo los principios REST, a la manera del sumador simple versión REST.

## Solución

La calculadora admite 4 recursos:
* /suma
* /resta
* /mult
* /div

Con el método PUT se envían los operandos (ej: 5,9) y el resultado se consulta mediante GET.