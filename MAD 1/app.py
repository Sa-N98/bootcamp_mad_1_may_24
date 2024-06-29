from flask import Flask, request, render_template as rt , redirect , url_for
from model import * 
from apis import *
from routs import router
import os
from flask_restful import Api


current_dir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ os.path.join(current_dir,"mad-1.sqlite3")


db.init_app(app)
app.app_context().push()

api = Api(app)

api.add_resource(playList ,'/api/playlist' )
api.add_resource(testAPI, '/api/test' , '/api/test/<i>' )

router(app)


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')


