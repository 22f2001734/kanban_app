from flask import Flask

app = None #initially none


def init_app():
    kanban_app = Flask(__name__) #Object of Flask
    kanban_app.debug = True
    kanban_app.app_context().push() #Direct access app by other modules(db, authentication, etc)
    print("kanban application started....")
    return kanban_app

app = init_app()
from backend.controllers import *

if __name__=="__main__":
    app.run()