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

        #DELETE for /students/{studentID}/{classID}
	def DELETE(self,sid=None,cid=None):
		output = {"result" : "success"}
		sid = int(sid)
		cid = int(cid)
		try:
			print(self.sdb.classes)
			self.sdb.delete_from_class(sid, cid)
			print(self.sdb.classes)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)            
                 
	#GET for /students/
	def GET_ALL(self):
		output = {'result':'success'}
		try:
			entries = []
			for cid in self.sdb.students:
				student = {}
				student_info = self.sdb.students[cid]
				print(student_info)
				student["sid"] = int(cid)
				student["Student"] = student_info[0]
				student["points"] = student_info[1]
				entries.append(student)
			output["entries"] = entries

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	#DELETE for /students/
	def DELETE_ALL(self):
		output = {"result" : "success"}
		try:
			self.sdb.students.clear()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	                

	#PUT for /students/:sid
	def PUT(self, sid):
		output = {"result" : "success"}
		sid = int(sid)
		data = json.loads(cherrypy.request.body.read())
		try:
			Student = data["Student"]
			points = data["points"]
			self.sdb.students[sid] = [Student, points]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
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

        #GET for /class/
	def GET(self):
		output = {"result" : "success"}
		try:
			entries = []
			for cid in self.sdb.classes:
				my_class = {}
				class_info = self.sdb.classes[cid]
				my_class["name"] = class_info[0]
				my_class["prof"] = class_info[1]
				my_class["point_goal"] = int(class_info[2])
				my_class["students"] = class_info[3]
				entries.append(my_class)
			output["classes"] = entries

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
	            

	#DELETE for /class/
	def DELETE(self):
		output = {"result" : "success"}
		try:
			self.sdb.classes.clear()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	#PUT for /class/:cid
	def PUT(self, cid):
		output = {"result" : "success"}
		body = cherrypy.request.body.read().decode()
		cid = int(cid)
		try:
			body = json.loads(body)
			name = body["name"]
			prof = body["prof"]
			students = body["students"]
			point_goal = body["point_goal"]
			class_info = [name, prof, point_goal, students]
			self.sdb.classes[cid] = class_info
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	#DELETE for /class/:cid
	def DELETE_CLASS(self, cid):
		cid = int(cid)
		output = {"result" : "success"}
		try:
			del self.sdb.classes[cid]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
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

	###### Students ######

	#GET:
	dispatcher.connect('student_get', '/student/:id',controller=students,action = 'GET',conditions=dict(method=['GET']))
	dispatcher.connect('points_get', '/student/:sid/:cid',controller=students,action = 'GET_POINTS',conditions=dict(method=['GET']))
	dispatcher.connect('student_get_all','/student/',controller=students,action ='GET_ALL',conditions=dict(method=['GET']))
	#PUT
	dispatcher.connect('points_put','/student/:sid/:cid',controller=students,action = 'PUT_POINTS',conditions=dict(method=['PUT']))
	dispatcher.connect('student_put','/student/:sid',controller=students,action = 'PUT',conditions=dict(method=['PUT']))


        #DELETE
	dispatcher.connect('student_delete','/student/:sid/:cid',controller=students,action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('student_delete_all','/student/',controller=students,action= 'DELETE_ALL', conditions=dict(method=['DELETE']))

	###### Classes ######
        
	#GET
	dispatcher.connect('class_get', '/class/:id',controller=classes,action = 'GET_ALL',conditions=dict(method=['GET']))
	dispatcher.connect('class', '/class/',controller=classes,action = 'GET',conditions=dict(method=['GET']))

	#DELETE
	dispatcher.connect('delete_classes', '/class/',controller=classes,action = 'DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('delete_class', '/class/:cid',controller=classes,action = 'DELETE_CLASS', conditions=dict(method=['DELETE']))

	#PUT
	dispatcher.connect('class_put','/class/:cid',controller=classes,action = 'PUT',conditions=dict(method=['PUT']))

	###### Images ######

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
