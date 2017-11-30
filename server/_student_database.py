class _student_database:

    # student database class constructor. It initializes three data
    # members to empty dictionaries. One containing student information,
    # one containing class information, and one containing image information.
    def __init__(self):
        self.students = {}
        self.classes = {}
        self.images = {}

    # Opens a file with the name given as a parameter and loads the class
    # data from that file into a dictionary with class ID as a key
    def load_classes(self, file_name):
        self.classes.clear()
        f = open(file_name)
        for line in f:
            class_info = line.strip().split(",")
            cid = int(class_info[0])
            students = []
            for sid in range(4, len(class_info)):
                students.append(int(class_info[sid]))
            class_info = class_info[1:4]
            class_info[2] = int(class_info[2])
            class_info.append(students)
            self.classes[cid] = class_info
        f.close()

    # Open a file with the name given as a parameter and loads the student
    # data from that file into a dictionary with student ID as the key
    def load_students(self, file_name):
        self.students.clear()
        f = open(file_name)
        for line in f:
            student_info = line.strip().split(",")
            sid = int(student_info[0])
            classes = []
            for cid in range(3, len(student_info),2):
                class_info = {}
                class_info[student_info[int(cid)]] = student_info[int(cid)+1]
                classes.append(class_info)
            parsed_info = []
            parsed_info.append(student_info[1])
            parsed_info.append(classes)
            #print("TESTING LOAD_STUDENTS")
            #print(classes)
            self.students[sid] = parsed_info
        print(self.students)
        print("\n\n\n\n\n\n")
        f.close()

    # Open a file with the name given as a parameter and loads the student
    # image url from that file into a dictionary with student ID as the key
    def load_images(self, file_name):
        self.images.clear()
        f = open(file_name)
        for line in f:
            image_info = line.strip().split(",")
            sid = int(image_info[0])
            url = image_info[2]
            self.images[sid] = url
        f.close()

    # Clear all databases  
    def reset_all(self):
        self.classes.clear()
        self.students.clear()
        self.images.clear()

    # Clears the database of all class information
    def reset_classes(self):
        self.classes.clear()

    # Clears the database of all student information
    def reset_students(self):
        self.students.clear()

    # Clears the database of all image information
    def reset_images(self):
        self.images.clear()

    # Returns a student's name based on their student id
    def get_student(self, sid):
        sid = int(sid)
        return self.students[sid][0]

    # Returns the url for the student's image based on their student id
    def get_image(self, sid):
        sid = int(sid)
        return self.images[sid]

    # Returns the number of participation points a particular student has in a particular class.
    # Based on student id and class id.
    def get_points(self, sid, cid):
        sid = int(sid)
        cid = int(cid)
        #print(self.students)
        for class_id in self.students[sid][1]:
            for points in class_id:
                if int(points) == int(cid):
                    return int(class_id[points])

    # Sets the number of points a student has in a particular class to the user inputted value.
    # Based on student id and class id.
    def set_points(self, sid, cid, points):
        sid = int(sid)
        cid = int(cid)
        for i, item in enumerate(self.students[sid][1]):
            if str(cid) in item:
                #print(item[str(cid)])
                self.students[sid][1][i].pop(str(cid),0)
                self.students[sid][1][i][str(cid)] = str(points)

    # Returns a list of student ID's representing the ID's of the students
    # in that class
    def get_students(self, cid):
        cid = int(cid)
        return self.classes[cid][3]

    # Return the name of the professor teaching the class indicated by the 
    # given class ID.
    def get_professor(self, cid):
        cid = int(cid)
        return self.classes[cid][1]

    # Return the name of the class indicated by the given class ID
    def get_class(self, cid):
        cid = int(cid)
        return self.classes[cid][0]
       
    # Return the participation point goal of the class indicated by the given
    # class ID
    def get_goal(self, cid):
        cid = int(cid)
        return self.classes[cid][2]

    # Set the participation point goal of the class indicated by the given class
    # ID to the number indicated by the given point_num
    def set_goal(self, cid, point_num):
        cid = int(cid)
        point_num = int(point_num)
        self.classes[cid][2] = point_num

    # Calculates the average number of points that have been awarded to all students in a 
    # specific class
    def calculate_average(self, cid):
        cid = int(cid)
        student_list = self.get_students(cid)
        counter = 0
        point_sum = 0
        for i, student in enumerate(student_list):
            counter = counter + 1
            point_sum = point_sum + int(self.get_points(student_list[i],cid))
        return point_sum/counter

    # Return the highest number of participation points a student in the class has
    def calculate_max(self, cid):
        cid = int(cid)
        student_list = self.get_students(cid)
        highest_point_value = -1
        for i, student in enumerate(student_list):
            #print(student_list)
            current_point_value = self.get_points(student_list[i],cid)
            if int(current_point_value) > highest_point_value:
                highest_point_value = int(current_point_value)
        return highest_point_value



if __name__ == '__main__':
    sdb = _student_database()
    sdb.load_classes("../data/classes.csv")
    sdb.load_students("../data/students.csv")
    print(sdb.get_goal(2))
    print(sdb.get_points(1,1))
    sdb.set_goal(2, 100)
    print(sdb.get_goal(2))
