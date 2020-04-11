from flask_restful import Resource, reqparse
from models.storeModel import StoreModel

class StoreResource(Resource):
    def get(self,storename):
        store = StoreModel.find_by_name(storename)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    def post(self,storename):
        store = StoreModel.find_by_name(storename)
        #print("store1 = ", store)
        if store:
            return {'message': "A store with name '{}' already exists.".format(name)}, 400
        
        #print("Shiv : storename being passed to class StoreModel is :  ", storename)
        store = StoreModel(storename)
        #print("store2 = ", store.storename)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500
        
    def delete(self,storename):
        store = StoreModel.find_by_name(storename)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreResourceList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}


        
            