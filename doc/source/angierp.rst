Angie Repeater
==============

Descripción
^^^^^^^^^^^
   Angie Repeater es una herramienta de customización y envio de paquetes HTTP. La herramienta es capaz de leer un fichero con un formato determinado, crear un paquete a partir de el y enviarlo a un destino y un puerto determinado. Posteriormente se puede visualizar la respuesta. Esta herramienta es especialmente interesante cuando se quiere testear una API o algún servicio web que puede tener un comportamiento indeseado al recibir de alguna fuente un paquete malicioso que contenga algún campo http modificado malintencionadamente. La herramienta también soporta https y es capaz de enviar el paquete un número determinado de veces.

   La libreria utilizada para hacer la interfaz cli es click (https://click.palletsprojects.com/en/7.x/).
   
Uso básico
^^^^^^^^^^
   Siempre es posible ejecutar el siguiente trozo de código para explorar la funcionalidad de la herramienta::
   
    python3 angiearps.py --help

   Las opciones necesarias para ejecutar la herramienta son::

    --filename TEXT  Archivo donde se encuentra el paquete que se desea enviar (NECESARIA)
    --count INTEGER  Cuantas veces se desea enviar el paquete. -1 para infinito
    --url TEXT       Url del sitio donde se quiere enviar el paquete.
    --port TEXT      Puerto donde se desea enviar la petición. (por defecto, 80 para http 443 para https)
    --https INTEGER  https habilitado (por defecto deshabilitado)
    --help           Show this message and exit.

   Un ejemplo para enviar un paquete http podría ser::

    python3 angierp.py --filename ehttp --url info.cern.ch --port 80

   Para dirigir la salida a un fichero puede hacerse::
    python3 angierp.py --filename ehttp --url info.cern.ch --port 80 > salida.out

   Si no se desea salida, puede hacerse (en Linux)::
    python3 angierp.py --filename ehttp --url info.cern.ch --port 80 > /dev/null


Formato
^^^^^^^

   El formato de un paquete http debe de seguir el siguiente esquema:

   - Existe una cadena de caracteres reservada para hacer un salto de linea en el paquete. Por defecto es ``@@ANGIE_ENDL``. Si se usa la clase Repeater de la aplicación, ésta proporciona métodos para cambiar esta cadena.

   - No importa los saltos de linea o caracteres \n o \r que se introduzcan en el fichero ya que estos son eliminados en el procesamiento interno, pero es NECESARIO que las lineas del paquete acaben en el delimitador citado en la regla anterior.

   - En la última linea, debido a la implementación de http (RFCs 7230-7237), el paquete debe terminarse con dos delimitadores.

   - Por todo lo demás, el paquete debe escribirse en texto plano. Cada carácter escrito será transformado a bytes y enviado por la red al destino especificado.

   EJEMPLO::

    GET / HTTP/1.1@@ANGIE_ENDLN
    Host: info.cern.ch@@ANGIE_ENDLN
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0@@ANGIE_ENDLN
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8@@ANGIE_ENDLN
    Accept-Language: en-US,en;q=0.5@@ANGIE_ENDLN
    Accept-Encoding: gzip, deflate@@ANGIE_ENDLN
    DNT: 1@@ANGIE_ENDLN
    Connection: keep-alive@@ANGIE_ENDLN
    Upgrade-Insecure-Requests: 1@@ANGIE_ENDLN@@ANGIE_ENDLN


Clases
^^^^^^
   A continuación se presenta una breve descripción de cada una de las clases y la funcionalidad que presentan.

Repeater
~~~~~~~~

   Spoofer es la clase que incorpora toda la funcionalidad necesaria para leer un paquete http desde un fichero que obedezca el formato anteriormente descrito en el apartado formato, perparar el paquete http y enviarlo a su destinatario.

   **Atributos de la clase:**
   
   ``ENDL`` cadena de caracteres constante que representa el delimitador de salto de linea para la correcta lectura y procesamiento del paquete.

   **Funcionalidad de la clase:**

   ``Repeater():`` 
   
   - Constructor de la clase. 
   
   - no tiene parámetros formales.

   - devuelve una instancia de Repeater.

   ``set_endl(s):`` 
   
   - asigna el valor de s a la variable interna ENDL.
   
   - *s* es el nuevo delimitador deseado.

   - devuelve None.

   ``read_from_file(path):`` 
   
   - lee el fichero ubicado en **path** y transforma la cadena a una lista para ser enviada. 
   
   - *path* es la ruta donde está ubicada el fichero.

   - devuelve una cadena de caracteres con la cadena lista para enviar.

   ``send_http(http_str,url,p):``

   - método que envía en forma de bytes la cadena de caracteres *http_str* a la *url* y *puerto* especificados. Recive la respuesta y la muestra en salida estándar.

   - *http_str* es la cadena a enviar, *url* es el destino y *p* es el puerto objetivo.

   - Devuelve una cadena de caracteres correspondiente a la respuesta.

   ``send_http(http_str,url,p):``

   - método que envía en forma de bytes la cadena de caracteres *http_str* a la *url* y *puerto* especificados envolviendo los datos http en un protocolo intermedio (preferentemente TLS 1.3) para formar https. Recive la respuesta y la muestra en salida estándar.

   - *http_str* es la cadena a enviar, *url* es el destino y *p* es el puerto objetivo.

   - Devuelve una cadena de caracteres correspondiente a la respuesta.

