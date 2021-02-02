from TuffixAPI.Data import IMAGES
from flask_restful import Resource

class ImagesList(Resource):
  def get(self):
    return IMAGES

class LatestImage(Resource):
    def get(self):
        return IMAGES[0]
