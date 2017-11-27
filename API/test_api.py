from _student_database import _student_database 
import unittest

class TestStudentDatabase(unittest.TestCase):

    # Unit tests for Participation Service API

    sdb = _student_database()

    def reset_data(self):
        self.sdb.reset_classes()
        self.sdb.reset_students()
        self.sdb.reset_images()
        self.sdb.load_classes("../data/classes.csv")
        self.sdb.load_students("../data/students.csv")
        self.sdb.load_images("../data/students.csv")

    def test_get_student(self):
        self.reset_data()
        student = self.sdb.get_student(1)
        correct_student = "Matthew Fabian"
        self.assertEqual(student, correct_student)

    def test_get_image(self):
        self.reset_data()
        url = self.sdb.get_image(1)
        correct_url = "https://ag.purdue.edu/profileimages/ander909.jpg"
        self.assertEqual(url,correct_url)

    def test_get_points(self):
        self.reset_data()
        points = self.sdb.get_points(4,2)
        correct_points = 5
        self.assertEqual(points, correct_points)

    def test_set_points(self):
        self.reset_data()
        self.sdb.set_points(4,2,self.sdb.get_points(4,2)-1)
        points = self.sdb.get_points(4,2)
        correct_points = 4
        self.assertEqual(points, correct_points)

    def test_get_students(self):
        self.reset_data()
        students = self.sdb.get_students(1)
        correct_students = [1,3,6,8,10,11,12,13,14]
        self.assertEqual(students, correct_students)   

    def test_get_professor(self):
        self.reset_data()
        prof = self.sdb.get_professor(0)
        correct_prof = "Prof. Kumar"
        self.assertEqual(prof, correct_prof)

    def test_get_class(self):
        self.reset_data()
        course = self.sdb.get_class(3)
        correct_course = "Accountancy"
        self.assertEqual(course, correct_course)

    def test_get_goal(self):
        self.reset_data()
        goal = self.sdb.get_goal(4)
        correct_goal = 50
        self.assertEqual(goal, correct_goal)

    def test_set_goal(self):
        self.reset_data()
        self.sdb.set_goal(4, 5000)
        goal = self.sdb.get_goal(4)
        correct_goal = 5000
        self.assertEqual(goal, correct_goal)

    def test_calculate_average(self):
        self.reset_data()
        average = self.sdb.calculate_average(0)
        correct_average = 28.11111111111111
        self.assertEqual(average, correct_average)

    def test_calculate_max(self):
        self.reset_data()
        max_points = self.sdb.calculate_max(1)
        correct_max = 11
        self.assertEqual(max_points, correct_max)


if __name__ == '__main__':
    unittest.main()
