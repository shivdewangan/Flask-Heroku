from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.itemModel import ItemModel

class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('itemprice', type=float,required=True,help="This field cannot be left blank!")
    parser.add_argument('storeid', type=int,required=True,help="This field cannot be left blank!")
    
    @jwt_required()
    def get(self,itemname):
        item = ItemModel.find_by_name(itemname)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
    
    def post(self,itemname):
        item = ItemModel.find_by_name(itemname)
        if item:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        
        data = ItemResource.parser.parse_args()#
        item = ItemModel(itemname,**data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        
        return item.json(), 201
    
    
    
    def delete(self,itemname):
        item = ItemModel.find_by_name(itemname)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404
    
    
    def put(self,itemname):
        data = ItemResource.parser.parse_args()
        item = ItemModel.find_by_name(itemname)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(itemname, **data)
        
        item.save_to_db()
        return item.json()
    
    
    
class ItemResourceList(Resource):
        def get(self):
           return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        

        