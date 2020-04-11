from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    itemid = db.Column(db.Integer, primary_key = True)
    itemname = db.Column(db.String(100))
    itemprice = db.Column(db.Float(precision=2))
    storeid = db.Column(db.Integer, db.ForeignKey('stores.storeid'))
    store = db.relationship('StoreModel')
    
    def __init__(self,itemname,itemprice,storeid):
        self.itemname = itemname
        self.itemprice = itemprice
        self.storeid = storeid
        
    @classmethod
    def find_by_name(cls,itemname):
        return cls.query.filter_by(itemname=itemname).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def json(self):
        return {'itemname': self.itemname, 'itemprice': self.itemprice}
