import os
from flask import Blueprint, request
from flask_restful import Api, Resource
from silentauction.utils.nukepave import nuke_pave

SERVER_TOKEN = os.getenv('SERVER_TOKEN')

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)  # Create an instance of flask_restful.Api

class DemoReset(Resource):
    def post(self):
        auth_header = request.headers.get('Authorization')
        if auth_header == SERVER_TOKEN:
            nuke_pave()
            return {"message": "Demo reset successfully"}, 200
        else:
            return {"message": "Unauthorized"}, 401

api.add_resource(DemoReset, '/demo-reset')  # Add the Resource to the Api instance