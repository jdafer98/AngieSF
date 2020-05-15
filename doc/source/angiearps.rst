Angie Port Scanner
==================

Descripción
^^^^^^^^^^^
   Angie ARP Spoofing es una pequeña herramienta de customización de paquetes basados en el protocolo ARP para la realización del clásico ataque MITM conocido como ARP Spoofing. Introducciendo en la aplicación una ip de víctima y una ip de puerta de enlace común entre el usuario y la víctima, la aplicación comenzará a inyectar paquetes ARP en la red envenenando las tablas ARP de los dispositivos haciendo creer a estos que deben enviar tráfico al usuario de la aplicación situandose este en medio de la "conversación".

   La libreria utilizada para hacer la interfaz cli es click (https://click.palletsprojects.com/en/7.x/).
   
Uso básico
^^^^^^^^^^
   Siempre es posible ejecutar el siguiente trozo de código para explorar la funcionalidad de la herramienta::
   
    python3 angiearps.py --help

   Las opciones necesarias para ejecutar la herramienta son::

    --target_ip STRING ip objetivo del ataque.

    --router_ip STRING ip de la puerta de enlace.


   Un ejemplo podría ser::

    python3 angiearps.py --router_ip 192.168.1.1 --target_ip 192.168.1.130

Clases
^^^^^^
   A continuación se presenta una breve descripción de cada una de las clases y la funcionalidad que presentan.

Spoofer
~~~~~~~
   Spoofer es la clase que incorpora toda la funcionalidad necesaria para llevar a cabo el ataque. Incorpora métodos para configurar las variables internas de la clase así como métodos para realizar la inyección de paquetes por un interfaz en función de esas variables.

   **Atributos de la clase:**
   
   ``target_ip:`` cadena de caracteres que representa la ip del objetivo a realizar el ataque.

   ``router_ip:`` cadena de caracteres que representa la ip de la puerta de enlace a la que está conectado el objetivo.

   **Funcionalidad de la clase:**

   ``Spoofer():`` 
   
   - Constructor de la clase. 
   
   - no tiene parámetros formales.

   - devuelve una instancia de Spoofer.

   ``set_router_ip(rip):`` 
   
   - asigna el valor de rip a la variable interna router_ip. 
   
   - *rip* es la ip del router objetivo.

   - devuelve None.

   ``set_target_ip(tip):`` 
   
   - asigna el valor de tip a la variable interna target_ip. 
   
   - *tip* es la ip del router objetivo.

   - devuelve None.

   ``spoof():``

   - método que utiliza las variables internas previamente asignadas para fabricar los paquetes ARP necesarios para realizar el ataque. Envia una pareja de paquetes ARP. Uno con ip = router_ip y otro con ip = target_ip haciendo entender que el atacante es el router.

   - No tiene parámetros formales.

   - Devuelve None.

   ``request_mac(ip):``

   - Crea un paquete ARP que pregunta por la dirección MAC especificada.

   - *ip* es una cadena de caracteres que representa la ip que se quiere resolver mediante ARP a MAC.

   - Devuleve una cadena de caracteres con la dirección MAC de la ip solicitada o bien -1 si no se ha podido encontrar.

   ``begin_spoof():``

   - Método que coordina y lleva a cabo todo el proceso del ataque con los métodos de instancia y las variables de instancia especificadas. En resumen, toma las ip de router y objetivo, resuelve a direcciones MAC y si todo ha salido correctamente, inyecta los paquetes ARP con las direcciones MAC de router y objetivo con objeto de envenenar sus tablas ARP.

   - No tiene parámetros formales.

   - Devuelve None.

