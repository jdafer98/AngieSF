Angie Port Scanner
==================

Descripción
^^^^^^^^^^^
   Angie Port Scanner es un escáner de puertos basado en linea de comandos que aprovecha el paralelismo del ordenador para explorar servicios activos en un host especificado. En general, la herramienta considera la exploración de un puerto como una tarea y las dispone en una cola. Los moles extraen las tareas de la cola, las procesan, y guardan el resultado. Si quedan más tareas en la cola, cogerán otra más.
   
Uso básico
^^^^^^^^^^
   Siempre es posible ejecutar el siguiente trozo de código para explorar la funcionalidad de la herramienta::
   
    python3 angieps.py --help

   Las opciones más características son::

    --host (IP|DOMAIN_NAME) host objetivo del escáner

    --initial_port INTEGER  puerto de inicio

    --end_port INTEGER      puerto final

    --verbose INTEGER       Muestra más información. 0 off, 1 on

    --moles INTEGER         Numero de moles (hebras) que ejecutan el scaneo en paralelo
                          
    --dn INTEGER            El Host es pasado como nombre de dominio. 0 off, 1 on

    --sweep INTEGER         Modo barrido. Activado, se ignora el rango de puertos y el host debe pasarse en formato ip/host. 0 off, 1 on.

   Un uso recurrente de la herramienta puede ser analizar los primeros 1024 puertos de un host concreto::

    python3 angieps.py --host 192.168.1.100 --ini_port 1 --end_port 1024 --moles 512

   también es posible ejecutar una resolución de nombre de dominio de un host con la opción ``--dn`` puesta a 1::

    python3 angieps.py --host www.example.com --ini_port 1 --end_port 1024 --moles 512 --dn 1

   Asímismo puede usarse la herramienta para detectar que hosts están activos en una red::

    python3 angieps.py --sweep 1 --moles 512 --host 192.168.0.0/24

Clases
^^^^^^
   A continuación se presenta una breve descripción de cada una de las clases y la funcionalidad que presentan.

AngieTask
~~~~~~~~~
   AngieTask es la estructura de datos básica que representa un puerto de un host a escanear. También puede representar una ip de un host que deseamos comprobar si está activo. En este último caso se ignora el puerto.

   **Atributos de la clase:**
   
   ``current_task_id:`` Es una variable auxiliar para autogenerar las ids de las tareas.

   ``task_port:`` Puerto del host que se desea escanear.

   ``task_id:`` Es la variable que identifica a la tarea. Es autogenerada cuando se construye la instancia.

   **Funcionalidad de la clase:**

   ``AngieTask(p,ip):`` 
   
   - Constructor de la clase. 
   
   - *p* es el puerto a escanear mientras que *ip* es la ip del host objetivo.

   - devuelve una instancia de AngieTask.

   ``get_port():``

   - Devuelve el puerto propio de la instancia.

   - No tiene parámetros formales.

   - devuelve un entero correspondiente al puerto de entrada.

   ``get_ip():``

   - Devuelve la ip propia de la instancia.

   - No tiene parámetros formales.

   - Devuelve una cadena de caracteres correspondiente a la ip de la tarea.

   ``get_id():``

   - Devuelve la identificación propia de la tarea.

   - No tiene parámetros formales.

   - Devuelve un entero correspondiente a la id de la tarea.


Mole
~~~~
   Representa una versión de una thread de python con funcionalidad extendida, adaptada para los propósitos de la aplicación.

   **Atributos de la clase:**
   
   ``verbose:`` Indica la salida por pantalla de mensajes de *feedback*. Vale True o False

   ``target`` y ``args`` son dos variables propias del módulo threading nativo de python pero también es utilizado por la herramienta.

   **Funcionalidad de la clase:**

   ``Mole(f,a):`` 
   
   - Constructor de la clase. 
   
   - *f* es una referencia a la función que se deseé que la hebra ejecute y *args* son los argumentos de dicha función.

   - devuelve una instancia de Mole.

   ``set_verbose(v):``

   - asigna el valor proporcionado a la variable verbose de la instancia Mole.

   - *v* es un booleano que representa la presencia de los mensajes por salida estandar o no.

   - devuelve None.

   ``scan_port(ip,port,v):``

   - Método de clase que informa acerca del estado de un puerto.

   - *ip* es una cadena de caracteres que representa la ip del host objetivo, *port* es un entero que representa el puerto a probar y *v* es un booleano que hace que la función proporcione output o no.

   - Devuelve una lista con dos valores [p,e], que corresponden con un entero representando un puerto y un booleano que informa si el puerto está cerrado o no.
   
   ``ping(host)``

   - Envia un paquete ICMP Echo Request a un host especificado como argumento. Puede ser una ip o un nombre de dominio.

   - *host* es una cadena de caracteres que representa un host o un nombre de dominio que identifican al host objetivo.

   - Devuelve un booleano que será verdadero si el host está activo (si se recibe un echo request). Falso en caso contrario.

 
Mole
~~~~
   Representa una versión de una thread de python con funcionalidad extendida, adaptada para los propósitos de la aplicación.

   **Atributos de la clase:**
   
   ``verbose:`` Indica la salida por pantalla de mensajes de *feedback*. Vale True o False

   ``target`` y ``args`` son dos variables propias del módulo threading nativo de python pero también es utilizado por la herramienta.

   **Funcionalidad de la clase:**

   ``Mole(f,a):`` 
   
   - Constructor de la clase. 
   
   - *f* es una referencia a la función que se deseé que la hebra ejecute y *args* son los argumentos de dicha función.

   - devuelve una instancia de Mole.
