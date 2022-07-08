import utils
import services.user as user_service
from flask.ext.restful import reqparse, Resource, abort

# Custom parsing
parser = reqparse.RequestParser()
parser.add_argument('first_name', type=str, help="User's first name")
parser.add_argument('last_name', type=str, help="User's last name")
parser.add_argument('city', type=str, help="User's home city")

class UserResource(Resource):

    def get(self, user_id):
        """
	Return a JSON representation of the user

        **Example request**:
        .. sourcecode:: http
            GET /user/<user_id>
        **Example response**:
        .. sourcecode:: http
            HTTP/1.1 200 OK
            Vary: Accept
	    {
		'id': 123,
		'first_name': 'Derek',
		'last_name': 'Janni',
		'city': 'Portland'
	    }

        :status 404: User not found - "This should never happen"
        :status 400: Bad info passed in, e.g. id is cast as an integer
        """
        args = utils.parse_args(parser)
        first_name = args.get('first_name')
        last_name = args.get('last_name')
        city = args.get('city')

        additional_info = {
            'first_name': first_name,
            'last_name': last_name,
            'city': city
        }
        return user_service.get_user(user_id, **additional_info)
