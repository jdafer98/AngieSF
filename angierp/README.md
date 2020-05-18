# AngieARPS

Herramienta de customización de peticiones HTTP/HTTPS como parte del framework AngieSF.

## Requisitos funcionales
  
 - RF1: El software debe ser capaz de aceptar un paquete HTTP en texto plano.
 - RF2: El software debe ser capaz de enviar el paquete via HTTP y HTTPS.
 - RF3: El software debe ser capaz de establecer una conexión TCP con un servidor.
 - RF4: El software debe ser capaz de enviar el mismo paquete varias veces en bucle.

## Requisitos no funcionales

 - RNF1: Los paquetes de entrada deberán poder ser leidos en texto plano.
 - RNF2: El software debe realizar la conexión en un tiempo razonable.
 - RNF3: En caso de no poder establecer la conexión, el software debe informar del error.
 - RNF4: El software tendrá como input un fichero de texto plano.
 - RNF5: El fichero de texto solo será leido si las lineas del fichero acaban con un delimitador propio de la aplicación.
