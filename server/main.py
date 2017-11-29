from _student_database import _student_database
import cherrypy
import re, json

##################################
# STUDENT HANDLER
##################################

class Students(object):

	def __init__(self, db):
		self.sdb = db
		self.sdb.reset_all()
		self.sdb.load_classes('/home/mfabian1/classes.csv')
		self.sdb.load_students('/home/mfabian1/students.csv')
		self.sdb.load_images('/home/mfabian1/students.csv')

	#GET for /students/{studentID}
	def GET(self, id=None):
		output = {'result':'success'}
		student = self.sdb.get_student(id)
		if student is None:
			output['result'] = 'error'
			output['message'] = 'key not found'
		else:
			output['id'] = id
			output['name'] = student
		return json.dumps(output)

##################################
# CLASS HANDLER
##################################

class Classes(object):
	def __init__(self, db):
		self.sdb = db
		self.sdb.reset_all()
		self.sdb.load_classes('/home/mfabian1/classes.csv')
		self.sdb.load_students('/home/mfabian1/students.csv')
		self.sdb.load_images('/home/mfabian1/students.csv')



##################################
# IMAGE HANDLER
##################################

class Images(object):
	def __init__(self, db):
		self.sdb = db
		self.sdb.reset_all()
		self.sdb.load_classes('/home/mfabian1/classes.csv')
		self.sdb.load_students('/home/mfabian1/students.csv')
		self.sdb.load_images('/home/mfabian1/students.csv')


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

	#GET:
	dispatcher.connect('student_get', '/student/:id',controller=student,action = 'GET',conditions=dict(method=['GET']))


	# Classes

	# Images

	# Configuration
	conf = {'global': {'server.socket_host': 'student04.cse.nd.edu/mfabian1/particip8', 'server.socket_port': 80}, '/' : {'request.dispatch':dispatcher}}