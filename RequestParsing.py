from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')

# push and array of name in body
parser.add_argument('name', action='append', required=True, help='Name cannot be blank')
args = parser.parser_args()

# Other Destinations
parser.add_argument('name', dest='public_name')
args = parser.parser_args()
args['public_name']



# -------------------- Argument Locations -----------------

# Look only on POST body
parser.add_argument('name', type=int, location='form')

# Look only on 
parser.add_argument('PageSize', type=int, location='args')

# From the request header
parser.add_argument('User-Agent', location='headers')

# From http Cookie
parser.add_argument('session_id', location='cookies')

# From file uploads
parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')


# Multiple Locations
parser.add_argument('text', location=['headers', 'values'])



