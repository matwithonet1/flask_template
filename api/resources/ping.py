import time
import services.external_api as external_api
from flask.ext.restful import reqparse, Resource


__doc__ = """
The following routes are supported:
GET     /ping
GET     /pong
"""

# Custom parsing
parser = reqparse.RequestParser()


# Resource classes
class PingResource(Resource):
    def get(self):
        """
        General health check route.
        **Example request**:
        .. sourcecode:: http
            GET /ping
        **Example response**:
        .. sourcecode:: http
            HTTP/1.1 200 OK
            Vary: Accept
            {"message": "PONG"}
        """
        return {'message': "PONG"}


class PongResource(Resource):
    def _get_failed_response(self, message="Unable to attempt service. System error."):
        """Uniform way of returning a failed response."""
        return {
            'response': "FAIL",
            'message': message,
            'response_time': 0
        }

    def _get_service_response(self, service_method, *args, **kwargs):
        """Uniform way of executing a service_method, and returning a formatted response."""
        start_time = time.time()
        resp = {}
        try:
            service_method(*args, **kwargs)
            resp['response'] = "OK"
            resp['message'] = "PONG"
        except Exception as e:
            resp['response'] = "ERROR"
            resp['message'] = "Error: {}".format(e)
        finally:
            resp['response_time'] = int((time.time() - start_time) * 1000)

        return resp


    def get(self):
        """
        Connects to various services used and returns response. Response time is in milliseconds.
        The `response` attribute may have one of three values.
            * `OK` indicates a healthy response.
            * `ERROR` indicates a connection or execution error.
            * `FAIL` indicates a system error not directly related to the service.
        **Example request**:
        .. sourcecode:: http
            GET /pong
        **Example response**:
        .. sourcecode:: http
            HTTP/1.1 200 OK
            Vary: Accept
            {
                "message": "OK",
                "services": {
                    "external_api": {
                        "response": "OK",
                        "message": "PONG"
                        "response_time": 40
                    }
                }
            }
        """
        resp = {'services': {}}
        resp['services']['external_api'] = self._get_service_response(external_api.ping)

        if all((s['response'] == "OK" for s in resp['services'].values())):
            resp['message'] = "OK"
        else:
            resp['message'] = "FAIL"

        return resp
