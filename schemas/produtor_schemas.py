from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from . import ma
from models.produtor_models import Produtor

class ProdutorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Produtor
        
