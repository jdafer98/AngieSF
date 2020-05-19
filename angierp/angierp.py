from repeater import Repeater
import click

@click.command()
@click.option('--filename', default=None, help='Archivo donde se encuentra el paquete que se desea enviar')
@click.option('--count', default=1, help='Cuantas veces se desea enviar el paquete. -1 para infinito')
@click.option('--url', default=None, help='Url del sitio donde se quiere enviar el paquete.')
@click.option('--port', default=None, help='Puerto donde se desea enviar la petición.')
@click.option('--https', default=0, help='https habilitado')



def angierp(filename,count,url,port,https):

    #name = 'ehttps'
    r = Repeater()
    for ii in range(count):
        if filename != None and url != None:
            try:
                content = r.read_from_file(filename)
            except:
                print("No se ha podido abrir el archivo: " + filename)
                exit(1)

            b = False if https == 0 else True

            if not b:
                print(r.send_http(content,url,80 if port == None else int(port) ))
            else:
                print(r.send_https(content,url,443 if port == None else int(port) ))


        else:
            print("Error: Los campos filename y url son necesarios. --help para más información")

if __name__ == '__main__':
    angierp()
