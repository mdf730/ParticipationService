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

    def test_get_students(self):
        self.reset_data()
        students = self.sdb.classes[1][3]
        correct_students = [1,3,6,8,10,11,12,13,14]
        self.assertEqual(students, correct_students)   

    def test_get_professor(self):
        self.reset_data()
        prof = self.sdb.classes[0][1]
        correct_prof = "Prof. Kumar"
        self.assertEqual(prof, correct_prof)

    def test_get_class(self):
        self.reset_data()
        course = self.sdb.classes[3][0]
        correct_course = "Accountancy"
        self.assertEqual(course, correct_course)

    def test_get_goal(self):
        self.reset_data()
        goal = self.sdb.classes[4][2]
        correct_goal = 50
        self.assertEqual(goal, correct_goal)

    def test_set_goal(self):
        self.reset_data()
        self.sdb.set_goal(4, 5000)
        goal = self.sdb.classes[4][2]
        correct_goal = 5000
        self.assertEqual(goal, correct_goal)

if __name__ == '__main__':
    unittest.main()
