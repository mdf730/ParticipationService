from _student_database import _student_database
import cherrypy
import re, json

##################################
# STUDENT HANDLER
##################################

class Students(object):

	def __init__(self, db):
		pass

##################################
# CLASS HANDLER
##################################

class Classes(object):
	def __init__(self, db):
		pass

##################################
# IMAGE HANDLER
##################################

class Images(object):
	def __init__(self, db):
		pass

##################################
# FUNCTIONS
##################################
def start_service()
	sdb = _student_database()
	students = Students(sdb)
	classes = Classes(sdb)
	images = Images(sdb)
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# Students

	# Classes

	# Images

	# Configuration
	conf = {'global': {'server.socket_host': 'student04.cse.nd.edu/mfabian1/particip8', 'server.socket_port': 80}, '/' : {'request.dispatch':dispatcher}}