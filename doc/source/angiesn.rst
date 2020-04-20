Angie Sniffer
==================

Descripción
^^^^^^^^^^^
   Angie Sniffer es un analizador de paquetes ligero escrito en python que provee toda la funcionalidad necesaria para captar tráfico de red y analizar cabeceras de paquetes, puertos destino, origen, tamaño de los paquetes y otra información que puede resultar útil para conocer que ocurre en la red y realizar estudios estadísticos con el fin de optimizar el flujo de información de tu infraestructura. Tan solo es necesario ejecutar el programa en un interfaz y analizar el paquete deseado.

   La biblioteca principal que hace la abstracción de la tarjeta de red utilizada es *scapy* (https://scapy.readthedocs.io/en/latest/). Tambien hace uso de la libreria nativa de python *Threading*

Uso básico
^^^^^^^^^^
   Para ejecutar AngieSN simplemente usa::
    
    sudo python3 angiesn

   **(es necesario poseer privilegios de superusuario)**

   Una vez hecho esto, angieSN detectará automáticamente los interfaces de los que dispone el equipo que lo ejecuta. Escribiendo el nombre del interfaz y pulstando <enter>, angiesn comenzará a capturar tráfico entrante y saliente del interfaz deseado. Manteniendo pulsado <ctrl izq> el proceso dejará de capturar tráfico.
   Seguidamente, nos encontramos un proceso iterativo donde angiesn pregunta por un paquete a analizar (todos identificados por un número). Escribiendo el número de paquete, el software nos proporciona toda la información que puede sernos útil acerca de ese paquete en concreto.
   Cuando no se desee analizar más paquetes, sencillamente escribiremos "no" o "n" en la terminal. 
   Es posible que deseemos guardar la captura de paquetes para analizarla más tarde con otra herramienta, o hacer gráficos y otros estudios. Angiesn nos pregunta al final si deseamos guardar nuestra captura en un fichero pcap y el nombre de destino del fichero.
   

Clases
^^^^^^
   A continuación se presenta una breve descripción de cada una de las clases y la funcionalidad que presentan.

Sniffer
~~~~~~~

   La clase *Sniffer* es la clase que proporciona toda la funcionalidad necesaria para capturar el tráfico de red, detectar interfaces y en general llevar el flujo de control del proceso de captura. Una instancia de esta clase dentro de una funcion principal, es de hecho todo lo necesario para conformar esta herramienta.

   **Atributos de la clase:**
   
   ``selected_iface:`` (string) Cadena de caracteres que representa el nombre del interfaz sobre el que se realizará la captura de tráfico.

   ``total_rows:`` (list:packets) Conjunto de todos los paquetes que se capturan.

   ``signal:`` (boolean) variablle de control que se utiliza para enviar una notificación al proceso de captura. Normalmente utilizada para indicar la prada del proceso.

   ``count:`` (int) Es la variable que toma la cuenta de todos los paquetes capturados.

   **Funcionalidad de la clase:**

   ``Sniffer():`` 
   
   - Constructor de la clase. 
   
   - No tiene parámetros de entrada.

   - devuelve una instancia de Sniffer.

   ``detect_ifaces():``

   - Método que devuelve una cadena de carácteres que representa los interfaces detectados en el equipo.

   - No tiene parámetros formales.

   - devuelve un string correspondiente a los interfaces detectados.

   ``select_iface(i):``

   - Modifica la variable de instancia *selected_iface* para indicar que un nuevo interfaz ha sido selecionado.

   - *i* es la cadena de caracteres que representa el interfaz que se desea selecionar.

   - Devuelve None.

   ``waiting_thread():``

   - Función que lanza una hebra que recibirá la petición de parada del proceso de captura.

   - No tiene parámetros formales.

   - Devuelve None.

   ``inter(x):``

   - Método privado de instancia que realiza una operación con el último paquete capturado

   - *x* es un paquete.

   - Devuelve None.
    
   ``sniff_pcks(n,f):``

   - método que comienza un proceso de captura de paquetes. Es posible especificar un número de paquetes y un filtro.

   - *n* es el número de paquetes a sniffar y f es un filtro con sintáxis BPF.

   - Devuelve None.


   ``begin_sniff(f):``

   - Método que lleva acabo todo el proceso de sniffado de paquetes, gestionando el análisis posterior de los paquetes capturados y el guardado en un archivo pcap.

   - *f* es un filtro BPF que utiliza el método para seleccionar el tráfico filtrado.

   - Devuelve None.
