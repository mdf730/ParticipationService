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

	#GET for /students/{studentID}/{classID}
	def GET_POINTS(self, sid=None, cid=None):
		output = {'result':'success'}
		points = self.sdb.get_points(sid,cid)
		if points is None:
			output['result'] = 'error'
			output['message'] = 'key not found'
		else:
			output['id'] = cid
			output['points'] = str(points)
		return json.dumps(output)

	#PUT for /students/{studentID}/{classID}
	def PUT_POINTS(self,sid=None,cid=None):
		output = {'result':'success'}
		data = json.loads(cherrypy.request.body.read())
		try:
			info = data["points"]
			self.sdb.set_points(sid,cid,info)
		except Exception as ex:
			output['result'] = str(ex)
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

	#GET for /class/:id
	def GET_ALL(self, id=None):
		output = {'result':'success'}
		output['students'] = []
		for sid in self.sdb.get_students(id):
			student = self.sdb.get_student(sid)
			info = {}
			info['id'] = int(sid)
			info['name'] = student
			if student is not None:
				output['students'].append(info)
		return json.dumps(output)

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
	
	#GET for /images/{studentID}
	def GET(self, id=None):
		output = {'result':'success'}
		url = self.sdb.get_image(id)
		if url is None:
			output['result'] = 'error'
			output['message'] = 'key not found'
		else:
			output['id'] = id
			output['url'] = url
		return json.dumps(output)

##################################
# FUNCTIONS
##################################
def start_service():
	sdb = _student_database()
	students = Students(sdb)
	classes = Classes(sdb)
	images = Images(sdb)
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	# Students

	#GET:
	dispatcher.connect('student_get', '/student/:id',controller=students,action = 'GET',conditions=dict(method=['GET']))
	dispatcher.connect('points_get', '/student/:sid/:cid',controller=students,action = 'GET_POINTS',conditions=dict(method=['GET']))
	#PUT
	dispatcher.connect('points_put','/student/:sid/:cid',controller=students,action = 'PUT_POINTS',conditions=dict(method=['PUT']))

	# Classes
	dispatcher.connect('class_get', '/class/:id',controller=classes,action = 'GET_ALL',conditions=dict(method=['GET']))

	# Images

	#GET:
	dispatcher.connect('image_get', '/image/:id',controller=images,action = 'GET',conditions=dict(method=['GET']))


	# Configuration
	conf = {'global': {'server.socket_host': 'student04.cse.nd.edu', 'server.socket_port': 51029},'/' : {'request.dispatch':dispatcher}}

	#Update configuration and start the server
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


if __name__ == '__main__':
	start_service()