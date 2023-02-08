from json import dumps
from typing import List
from marshmallow import Schema, fields
from model.berry import Berry

class BerrySchema(Schema):
    name = fields.Str()
    growth_time = fields.Int()

schema = BerrySchema()


def parse_raw_data_to_berries(data: List):
    return [schema.dump(Berry(item.get('item').get('name'),
                              int(item.get('growth_time'))))
                              for item in data]
        

