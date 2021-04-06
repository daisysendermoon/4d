import cherrypy
import pandas as pd
from upload_echo import UPLOAD
from get_echoes import DOWNLOAD

class EchoService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   def upload(self, longitude, latitude, audioFile):
      uploadFile = audioFile.file.read()
      uploader = UPLOAD()
      uploader.upload(longitude, latitude, uploadFile)
      return output

   @cherrypy.expose
   @cherrypy.tools.json_out()
   def getEchoList(self, longitude, latitude):

      downloader = DOWNLOAD()
      ret = downloader.getEchoes(longitude, latitude)   
      return ret

   @cherrypy.expose
   def getEchoFile(self, echoId):

      downloader = DOWNLOAD()
      ret = downloader.getAudioFile(echoId)
      return ret;


if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(EchoService())