from crawler import Crawler
import click

#'https://home.cern'



@click.command()
@click.option('--url', default=None, help='dirección objetivo del ataque (NECESARIA)')
@click.option('--fixed', default=0, help='ataque de combinaciones de longitud fija')
@click.option('--dictionary', default=None, help='path al diccionario customizado')
@click.option('--custom_set', default=None, help='Path al set customizado. Si se especifica, no se incluyen los diccionarios minus, mayus, numbers, special')
@click.option('--minus', default=0, help='Incluir minusculas en el ataque. 0 off 1 on')
@click.option('--mayus', default=0, help='Incluir mayusculas en el ataque. 0 off 1 on')
@click.option('--numbers', default=0, help='Incluir numeros 0-9 en el ataque. 0 off 1 on')
@click.option('--special', default=0, help='Incluir caracteres especiales en el ataque. 0 off 1 on')
@click.option('--size', default=1, help='Incluir la longitud fija del ataque de fuerza bruta fija. Solo tiene efecto si --fixed está activo')
@click.option('--nthreads', default=1, help='Número de hebras con las que realizar el ataque')

def angiecr(url,fixed,dictionary,custom_set,minus,mayus,numbers,special,size,nthreads):

    cr = Crawler()

    if url != None:
        cr.set_url(url)
        cr.set_size(size)
        cr.set_isFixed(True if fixed==1 else False)
        if nthreads != 1:
            cr.set_nthreads(nthreads)

        if dictionary != None:
            cr.set_custom_dict_path(dictionary)
            cr.read_custom_dict()
            cr.begin_crawl(1)
        else:
            if custom_set != None:
                cr.set_custom_set_path(custom_set)
                cr.read_custom_set()
                cr.begin_crawl(0)
            else:
                if minus != 0 or mayus != 0 or numbers != 0 or special != 0:
                    cr.select_sets(True if minus == 1 else False, True if mayus == 1 else False, True if numbers == 1 else False, True if special == 1 else False)
                    cr.begin_crawl(0)
                else:
                    print("Error: Un ataque de fuerza bruta precisa de un set de caracteres. Selecciona minus, mayus, numbers o especial. También puedes construir un custom set o realizar un ataque de diccionario (--help).")
            


    else:
        print('Error: falta la url introducida. Para mas información ejecutar con --help')



if __name__ == '__main__':
    angiecr()


