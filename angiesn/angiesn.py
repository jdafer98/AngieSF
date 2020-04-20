from sniffer import Sniffer


def angiesn():

    #Creamos un Sniffer
    sn = Sniffer()

    #Detectamos interfaces y preguntamos cual
    #Queremos usar hasta que haya una respuesta correcta

    detected_interfaces = sn.detect_ifaces()

    print("AngieSN HA DETECTADO LOS SIGUIENTES INTERFACES: " + str(detected_interfaces) )
    if_option = input("¿Cual desea usar? -->  ")

    while not if_option in detected_interfaces:
        if_option = input("No existe ese interfaz. Introduzca un interfaz válido:  ")

    #Selecionamos el interfaz y sniffamos
    sn.select_iface(if_option)
    
    filter_option = input("Escribe un filtro con sintáxis BPF (por defecto ninguno):  ")

    if filter_option == '':
        filter_option = None

    res = sn.begin_sniff(filter_option)

if __name__ == '__main__':
    angiesn()
