""" AngiePS: Escáner de puertos escrito como parte del framework AngieSF. """

__author__ = "Javier de Ángeles Fernández"
__email__ = "jdafer98@correo.ugr.es"
__license__ = "GPL v3.0"
__copyright__ = "2020"

from mole import Mole
from port_scanner import PortScanner
from angie_colors import AngieColors
import click


@click.command()
@click.option('--host', default="none", help='host objetivo del escáner')
@click.option('--initial_port', default=1, help='puerto de inicio')
@click.option('--end_port', default=1024, help='puerto final')
@click.option('--verbose', default=0, help='Muestra más información. 0 off, 1 on')
@click.option('--moles', default=5, help='Numero de moles (hebras) que ejecutan el scaneo en paralelo')
@click.option('--dn', default=0, help='El Host es pasado como nombre de dominio. 0 off, 1 on')
@click.option('--sweep', default=0, help='Modo barrido. Activado, se ignora el rango de puertos y el host debe pasarse en formato ip/host. 0 off, 1 on')
def angieps(host,initial_port,end_port,verbose,moles,dn,sweep):
    dn2 = False

    if not sweep and dn == 1:
        dn2 = True

    ps = PortScanner(host,initial_port,end_port,dn=dn2)
    if verbose == 1:
        ps.set_verbose(True)
    else:
        ps.set_verbose(False)
    
    ps.set_nmoles(moles)

    if not sweep:
        ps.begin_scan()
    else:
        print("Sweep Started...")
        ps.begin_sweep()

if __name__ == '__main__':
    angieps()

