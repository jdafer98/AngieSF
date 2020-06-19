Angie Crawler
=============

Descripción
^^^^^^^^^^^
   Angie Crawler es una herramienta de Bruteforcing a directorios en aplicaciones web (o brutefrocing en general, si se desea) como parte del framework AngieSF. Seleccionando un set entre los disponibles, uno de propia creación, o un diccionario y un modo (fijo o incremental. Solo si se ha seleccionado un set) podemos descubrir directorios ocultos en aplicaciones web pero que estén expuestos al usuario realizando peticiones.
   
Uso básico
^^^^^^^^^^
   Siempre es posible ejecutar el siguiente trozo de código para explorar la funcionalidad de la herramienta::
   
    python3 angiearps.py --help

   Las opciones básicas de la herramienta son::

    --url TEXT          dirección objetivo del ataque (NECESARIA)

    --fixed INTEGER     ataque de combinaciones de longitud fija

    --dictionary TEXT   path al diccionario customizado

    --custom_set TEXT   Path al set customizado. Si se especifica, no se
                      incluyen los diccionarios minus, mayus, numbers,
                      special

    --minus INTEGER     Incluir minusculas en el ataque. 0 off 1 on

    --mayus INTEGER     Incluir mayusculas en el ataque. 0 off 1 on

    --numbers INTEGER   Incluir numeros 0-9 en el ataque. 0 off 1 on

    --special INTEGER   Incluir caracteres especiales en el ataque. 0 off 1 on

    --size INTEGER      Incluir la longitud fija del ataque de fuerza bruta
                      fija. Solo tiene efecto si --fixed está activo

    --nthreads INTEGER  Número de hebras con las que realizar el ataque

   **Nota:** Se puede optar por usar un set predefinido, uno propio o un diccionario pero al menos un set debe estar presente si se desea hacer un ataque combinatorio o un diccionario si el modo *--dictionary* Está activo.

   Un ejemplo para un ataque de fuerza bruta combinatorio, incremental y con un set de minusculas de la a-z y mayusculas A-Z podría ser::

    python3 angiearps.py --url www.example.com --minus 1 --mayus 1

   Se entiende por incremental, probar todas las combinaciones del conjunto potencia del set, excepto el conjunto vacío. Fixed, será probar todos los elementos de un subconjunto del conjunto potencia tal que su cardinal sea el especificado en --size. Por defecto vale 1.


Sets y Diccionarios
^^^^^^^^^^^^^^^^^^^

   Sets disponibles:

   - **minus:** Carácteres ASCII de la a-z
   - **mayus:** Carácteres ASCII de la A-Z
   - **numbers:** Carácteres ASCII numéricos del 0-9
   - **special:** Carácteres ASCII imprimibles, no pertenecientes a las anteriores categorias. De aquí se excluyen algunos carácteres que pueden crear conflicto con la *query string* en una petición GET de HTTP.


Crear Sets personalizados
~~~~~~~~~~~~~~~~~~~~~~~~~

   Si ninguno de los sets o combinaciones de ellos satisface las necesidades del usuario, Angie Crawler permite la opción de crear sets personalizados.

   Simplemente se trata de un fichero de texto que cumple las siguientes normas:

   - Cada elemento que exista en el fichero será un carácter del set (se permiten incluso agrupaciones de carácteres o palabras completas)
   - Entre cada dos carácteres, debe existir una coma para separarlos.
   - Para introducir una coma como carácter, se debe escribir el caracter '..'

   Un ejemplo sería un fichero que contenga::

    a,b,2,*


Crear Dicionarios personalizados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Por compatibilidad con diccionarios clásicos como *rock_you.txt*, Angie Crawler reconoce diccionarios de formato similar. Un diccionario válido será aquel que contenga palabras o cadenas de caracteres separadas por un salto de linea.

   Por ejemplo::

    palabra1
    palabra2
    palabra3


Clases
^^^^^^
   A continuación se presenta una breve descripción de cada una de las clases y la funcionalidad que presentan.

Crawler
~~~~~~~
   Spoofer es la clase que incorpora toda la funcionalidad necesaria para llevar a cabo el ataque. Incorpora métodos para configurar las variables internas de la clase así como métodos para realizar la inyección de paquetes por un interfaz en función de esas variables.

   **Atributos de la clase:**

   ``(Variable de clase) code:`` Lista de enteros que representa una nueva combinación a generar para la aplicación. Los enteros representan la posición de un caracter en el set de caractéres especificado. 

   ``(Variable de clase) turn:`` Número entero que representa la siguiente entrada del diccionario que debe leer una hebra. Utilizada para sincronización de hebras.

   ``(Variable de clase) code_lock:`` Cerrojo para modificar las variables compartidas por varias hebras.

   ``isFixed:`` Booleano que expresa si el ataque de fuerza bruta se realiza con longitud fija o no.

   ``size:`` Entero que expresa la longitud del ataque de fuerza bruta de longitud fija. Solo tiene efecto si se selecciona este ataque.

   ``result:`` Lista de cadenas de caracteres que recogen el resultado final después del ataque.

   ``custom_set_path:`` Cadena de caracteres que representa la ruta hasta el fichero que contiene el set de caracteres que se desea usar en el ataque.

   ``custom_dict_path:`` Cadena de caracteres que representa la ruta hasta el fichero que contiene el diccionario que se desea usar en el ataque.

   ``dictionary:`` Representación interna del diccionario cargado desde un fichero.

   ``url:`` Cadena de caracteres que representa el sitio web de destino al que realizar el ataque.

   ``nthreads:`` Número de hebras que se desea usar en el ataque.

   ``final_set:`` lista de caracteres que representan el set final usado en el ataque, como resultado de combinaciones de sets incluidos en la aplicación o cargado desde un fichero.

   ``minus_selected:`` Booleano que representa si el diccionario *'minus'* está seleccionado

   ``minus:`` Lista de caracteres que representa un diccionario. El contenido del diccionario es el especificado en el apartado **Sets y Diccionarios**.

   ``mayus_selected:`` Booleano que representa si el diccionario *'mayus'* está seleccionado.

   ``mayus:`` Lista de caracteres que representa un diccionario. El contenido del diccionario es el especificado en el apartado **Sets y Diccionarios**.

   ``numbers_selected:`` Booleano que representa si el diccionario *'numbers'* está seleccionado

   ``numbers:`` Lista de caracteres que representa un diccionario. El contenido del diccionario es el especificado en el apartado **Sets y Diccionarios**.

   ``special_selected:`` Booleano que representa si el diccionario *'special'* está seleccionado

   ``special:`` Lista de caracteres que representa un diccionario. El contenido del diccionario es el especificado en el apartado **Sets y Diccionarios**.

   **Funcionalidad de la clase:**

   ``Crawler():`` 
   
   - Constructor de la clase. 
   
   - no tiene parámetros formales.

   - devuelve una instancia de Crawler.

   ``set_custom_set_path(p):`` 
   
   - Asigna el valor de p a la variable interna custom_set_path.
   
   - *p* es el path a un fichero que contiene el diccionario.

   - devuelve None.

   ``set_custom_dict_path(p):`` 
   
   - Asigna el valor de p a la variable interna custom_dict_path.
   
   - *p* es la ip del router objetivo.

   - devuelve None.

   ``set_isFixed(f):``

   - Asigna el valor de f a la variable interna isFixed.

   - *f* es un booleano que indica si se desea activar isFixed.

   - Devuelve None.

   ``init_sets():``

   - (Método Privado). Inicializa los sets que la aplicación trae por defecto

   - No tiene parámetros formales.

   - Devuleve None.

   ``set_url(u):``

   - Asigna el valor de u a la variable interna url.

   - *u* representa la url objetivo del ataque.

   - Devuelve None.

   ``set_nthreads(n):``

   - Asigna el valor de n a la variable interna nthreads.

   - *n* representa el número de hebras con las que se desea hacer el ataque.

   - Devuelve None.

    
   ``set_size(s):``

   - Asigna el valor de s a la variable interna size.

   - *s* representa la longitud fija del ataque de fuerza bruta si isFixed está activo.

   - Devuelve None.

   ``select_sets(mi,my,num,es):``

   - Método que permite seleccionar los sets con los que se va a llevar a cabo el ataque.

   - *mi,my,num,es* son booleanos que representa si se desean añadir los diccionarios *minus*,*mayus*,*numbers*,*special*.

   - Devuelve None.

   ``read_custom_set():``

   - Método utilizado para leer el set ubicado en la variable local custom_set_path.

   - No tiene parámetros formales.

   - Devuelve None.

   ``read_custom_dict():``

   - Método utilizado para leer el diccionario ubicado en la variable local custom_dict_path.

   - No tiene parámetros formales.

   - Devuelve None.

   ``gen_one_combination(code_lock,result,final_set,size,url):``

   - Método que genera la siguiente combinación de caracteres a partir del código y comprueba si ese directorio existe en la url objetivo (función ejecutada por las hebras).

   - *code_lock* es una variable de tipo Lock, *result* es la variable donde se almacenarán los resultados, *final_set* es el set con el que se realizará el ataque y *url* es la dirección objetivo a la que realizar el ataque.

   - Devuelve un.

   ``request_from_dictionary(dictionary,result,url,turn,code_lock):``

   - Método que toma la siguiente palabra del diccionario seleccionado y comprueba si el directorio existe en la url seleccionada.

   - *code_lock* es una variable de tipo Lock, *result* es la variable donde se almacenarán los resultados, *final_set* es el set con el que se realizará el ataque y *url* es la dirección objetivo a la que realizar el ataque.

   - Devuelve None.

   ``begin_crawl(mode):``

   - Método que coordina y lleva a cabo todo el proceso de descubimiento de directorios en la url especificada. Inicializa o lee los sets o diccionarios (dependiendo del parámetro mode).

   - *mode* Indica el modo de ataque (fueza bruta o diccionario).

   - Devuelve None.
