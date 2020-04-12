from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity


from resources.userResource import UserResource
from resources.itemResource import ItemResource, ItemResourceList
from resources.storeResource import StoreResource, StoreResourceList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'user1'

api = Api(app)

#@app.before_first_request
#def create_table():
    #db.create_all()    

jwt = JWT(app,authenticate,identity)

api.add_resource(StoreResource, '/store/<string:storename>') # Like add_resource encapsulating Class and it's attributes(resources)
api.add_resource(StoreResourceList, '/stores')

api.add_resource(ItemResource, '/item/<string:itemname>')
api.add_resource(ItemResourceList, '/items')

api.add_resource(UserResource, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)







