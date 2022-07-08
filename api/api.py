
import flask.ext.restful as flask_restful
import resources.user as user_resource
import resources.ping as ping_resource
from flask import Flask

# Create app.
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = flask_restful.Api(app, catch_all_404s=True)


# Ping Resources
api.add_resource(ping_resource.PingResource, "/ping")
api.add_resource(ping_resource.PongResource, "/pong")

# User Resources
api.add_resource(user_resource.UserResource, '/user/<user_id>')

if __name__ == "__main__":
    app.run(debug=True)
