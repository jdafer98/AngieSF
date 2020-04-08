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

 
PortScanner
~~~~~~~~~~~

   Agrupa una lista de tareas (instancias de AngieTask) a realizar y una colección de hebras (Instancias de Mole) que las ocupan, las realizan y devuelven resultados ciclicamente. Además incorpora toda la funcionalidad y la lógica necesaria para hacer los escaneo de puertos.

   **Atributos de la clase:**
   
   ``task_queue:`` Representa una cola de instancias de AngieTask.

   ``results:`` Es una lista que contendrá los resultados ([puerto,estado]. Donde puerto es un entero y estado es un booleano.) provenientes del escaneo de un puerto.

   ``host:`` Cadena de caracteres que representan el host objetivo al que se desea realizar le escaneo. Puede ser un nombre de dominio o una ip.

   ``ini_port:`` Entero que representa el puerto inicial del rango de puertos a escanear.

   ``end_port:`` Entero que representa el puerto final del rango de puertos a escanear.

   ``nmoles:`` Numero de Moles (hebras) con las que se realizará el escaneo. Por defecto 5.

   ``dn:`` Booleano que representa si el host se proporciona como nombre de dominio.

   ``verbose:`` Booleano. *Feedback* por pantalla o no.

   ``sweep_mode:`` Booleano que indica si el escaneo se realiza en modo barrido. El modo barrido ignora los puertos y se demanda el host en modo ip/mask. El resultado solo informa que host están activos en esa red.

   **Funcionalidad de la clase:**

   ``PortScanner(host,ini_port,end_port,dn):`` 
   
   - Constructor de la clase. 
   
   - Los parámetros formales son idénticos a los atributos de clase con el mismo nombre.

   - devuelve una instancia de PortScanner.

   ``init_queue()``

   - Método de instancia que inicializa en función de los atributos de dicha instancia la cola de tareas, creando y añadiendo AngieTasks por cada puerto especificado.

   - No tiene parámetros formales.

   - Devuelve None.

   ``set_verbose(v)``

   - Asigna el valor dado a la variable verbose.

   - *v* es un booleano que vale True si se desea el modo verbose. False en caso contrario.

   - Devuelve None.

   ``set_sweep_mode(sm)``

   - Asigna el valor dado a la variable sweep_mode.

   - *sm* es un booleano que vale True si se desea realizar un barrido en modo sweep_mode. False en caso contrario.

   - Devuelve None.

   ``fmole(q,results,v,sm)``

   - Función que ejecuta una mole. Dependiendo de si sweep_mode está activo, realizará un escaneo de puertos a un host o un barrido a una red determinada. Cada hebra coge una tarea y la realiza. Al finalizar informa de que ha terminado y coge otra tarea si el número de tareas no está vacío.

   - *q* es la cola de tareas, *results* es la lista donde se devolverán los resultados, *v* es un booleano (verbose) y sm es también un booleano (sweep_mode).
   - Devuelve None

   ``parse_ipmask(ipmask)``

   - Se encarga de coger una ip/mascara_red y devolver la dirección de la primera ip de esa red (la dirección de la propia red). El cálculo brevemente consiste en realizar una operación & entre la máscara y la direción dada. En realidad se trabaja solo con el octeto que resulta de hacer mascara módulo 8 pero el concepto es el mísmo.

   - El parámetro de entrada es una cadena de caracteres que representa una dirección ip con su máscara de red correspondiente.

   - devuelve una lista [final_ip,mask] que representa la primera ip de la subred y la máscara que fue proporcionada en un origen.

   ``make_report()``

   - Elabora un resumen en base a los resultados que ha proporcionado cada hebra. En caso de ser un escaneo de puertos, informa sobre los puertos abiertos. En caso de ser un escaneo de hosts activos, informa sobre que host responden a peticiones icmp.

   - No tiene parámetros formáles.

   - Devuelve una lista con todos los hosts o puertos que dan positivo en el escaneo realizado.

   ``launch_moles()``

   - Función que inicializa toda la lista de moles de la instancia PortScanner. Posteriormente quedará en espera bloqueada hasta que todas las moles terminen su función.

   - No tiene parámetros formales

   - Devuelve None.

   ``set_nmoles(n):``

   - asigna el valor n a la variable de instancia nmoles de la clase PortScanner.

   - *n* es un entero que representa el número de moles deseadas.

   - Devuelve None.

   ``lookup():``

   - Resuelve un nombre de dominio si la variable de instancia *dn* de la clase PortScanner está activa. El nombre de dominio debe especificarse en la variable de instancia *host*.

   - No tiene parámetros formales.

   - Devuelve una cadena de caracteres que representa la ip resultado de la consulta DNS del nombre de dominio.

   ``begin_scan()``

   - Función que prepara todo el proceso de escaneo y lanza las hebras. También calcula el tiempo de ejecución de todo el proceso y muestra los resultados por pantalla. Es la función estandar a ejecutar después de crear una instancia PortScanner.

   - No tiene parámetros formales.

   - Devuelve None.

   ``begin_sweep()``

   - Análoga a *begin_scan()* pero esta vez se realizará un barrido a la ip/máscara especificada en la variable de instancia *host*.

   - No tiene parámetros formales.

   - Devuelve None.

AngieColors
~~~~~~~~~~~

   Adicionalmente existe un módulo llamado AngieColors que no representa funcionalidad pero es utilizado como variable enumerada para imprimir colores por pantalla. Sus opciones son:

   - DEFAULT
   - HEADER
   - OKBLUE
   - OKGREEN
   - WARNING
   - FAIL
   - ENDC
   - BOLD
   - UNDERLINE

   En especial, ENDC no es un color, sino que desactiva las modificaciones hechas anteriormente.

   Un ejemplo de su uso puede ser::

    print(AngieColors.OKGREEN + "Texto en verde")


