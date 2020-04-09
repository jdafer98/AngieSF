## AngiePS

Escáner de puertos sencillo como parte del framework AngieSF.

# Requisitos funcionales

RF1: El software debe ser capaz de realizar un escaneo tcp a un host determinado.

RF2: El software debe ser capaz de identificar un host por ip.

RF3: El software debe ser capaz de reconocer a un host por nombre de dominio.

RF4: El software debe ser capaz de realizar el trabajo de forma concurrente.

RF5: El software debe ser capaz de aceptar un rango de puertos.

RF6: El software debe ser capaz de aceptar argumentos por linea de órdenes.

RF7: El software debe ser capaz de recibir como parámetro una red como ip/máscara a escanear.

RF8: El software debe contar con un modo "verbose".

RF9: El software debe realizar un reporte final del trabajo realizado

# Requisitos no funcionales

RNF1: El software debe realizar un escanéo empleando no mayor a 2 segundos por puerto escaneado.

RNF2: Las salidas del software deben mostrarse con colores.

RNF3: Cada tarea debe ser realizada tan solo por una hebra.

RFN4: No debe haber puertos o escaneos a host duplicados
