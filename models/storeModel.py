from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"
    storeid = db.Column(db.Integer, primary_key = True)
    storename = db.Column(db.String(100))
    storeitems = db.relationship('ItemModel', lazy='dynamic')
    
    def __init__(self,storename):
        self.storename = storename

        
    @classmethod
    def find_by_name(cls,storename):
        return cls.query.filter_by(storename=storename).first()
        
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def json(self):
        return {'storename': self.storename, 'storeitems': [storeitem.json() for storeitem in self.storeitems.all() ]}





        
    
        