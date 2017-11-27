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
            cid = class_info[0]
            students = []
            for sid in range(3, len(class_info)):
                students.append(class_info[sid])
            class_info = class_info[1:3]
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

if __name__ == '__main__':
    sdb = _student_database()
    sdb.load_classes("../data/classes.csv")
