import falcon
import json
from russiannames.parser import NamesParser

parser = NamesParser()

class Api:
    def on_get(self, req, res):
        qs = falcon.uri.parse_query_string(req.query_string)
        fullName = qs.get('fullName')
        res.body = json.dumps(parser.parse(fullName))

app = falcon.App()

app.add_route('/name', Api())

