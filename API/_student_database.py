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
        for line in open(file_name):
            class_info = line.strip().split(",")
            cid = int(class_info[0])
            students = []
            for sid in range(4, len(class_info)):
                students.append(int(class_info[sid]))
            class_info = class_info[1:4]
            class_info[2] = int(class_info[2])
            class_info.append(students)
            self.classes[cid] = class_info

    # Clears the database of all class information
    def reset_classes(self):
        self.classes.clear()

    # Clears the database of all student information
    def reset_students(self):
        self.students.clear()

    # Clears the database of all image information
    def reset_images(self):
        self.images.clear()

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

    # Return the highest number of participation points a student in the class
    # has
    #
    # CAN'T MAKE TEST FOR THIS UNTIL get_points IS IMPLEMENTED
    #
    #
    def calculate_max(self, cid):
        cid = int(cid)
        students = self.get_students(cid)
        highest_point_value = -1
        for student in students:
            current_point_value = self.get_points(student)
            if current_point_value > highest_point_value:
                highest_point_value = current_point_value
        return highest_point_value

if __name__ == '__main__':
    sdb = _student_database()
    sdb.load_classes("../data/classes.csv")
    print(sdb.get_goal(2))
    sdb.set_goal(2, 100)
    print(sdb.get_goal(2))
