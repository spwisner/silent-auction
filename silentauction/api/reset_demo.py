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
        payload = request.get_json()
        should_reset_stripe = False if payload is None else payload.get('should_reset_stripe', False)
        print(f"should_reset_stripe: {should_reset_stripe}")

        if auth_header == SERVER_TOKEN:
            nuke_pave(should_reset_stripe)
            return {"message": f"Demo reset successfully. should_reset_stripe={should_reset_stripe}"}, 200
        else:
            return {"message": "Unauthorized"}, 401

api.add_resource(DemoReset, '/demo-reset')  # Add the Resource to the Api instance