from fabric import task
from invoke import run

#Instalación de dependencias
@task
def build(name):
	run("pip install -r requirements.txt")

#evaluación con test
@task
def test(name):
	run("pytest")
