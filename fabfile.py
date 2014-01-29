def hello(name="Toki"):
    print("Hello " + name + "!")

from fabric.api import local

def prepare_deploy():
    #local("./manage.py test my_app")
    local("git add -p && git commit")
    local("git push")
