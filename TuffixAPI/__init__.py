from flask import Flask
from flask_restful import Api
from TuffixAPI.Resources import *

name = "TuffixAPI"

application = Flask(name)
api = Api(application)

api.add_resource(ImagesList, '/wallpaper/all')
api.add_resource(LatestImage, '/wallpaper/latest')

from TuffixAPI import Resources
