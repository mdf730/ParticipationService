from _student_database import _student_database 

def test_all(sdb):
    failures = 0
    if test_get_students(sdb) == True:
        print(".")
    else:
        print("F")
        failures = failures + 1

    if test_get_professor(sdb) == True:
        print(".")
    else:
        print("F")

    if test_get_class(sdb) == True:
        print(".")
    else:
        print("F")

    if test_get_goal(sdb) == True:
        print(".")
    else:
        print("F")

    if test_set_goal(sdb) == True:
        print(".")
    else:
        print("F")

    print("Failed " + str(failures) + " tests")

def test_get_students(sdb):
    if sdb.classes[0][3] != [1,2,3,4,5,6,7,8,9]:
        return False
    elif sdb.classes[1][3] != [1,3,6,8,10,11,12,13,14]:
        return False
    elif sdb.classes[2][3] != [1,2,3,4,5,6,7,8,9]:
        return False
    elif sdb.classes[3][3] != [1,15,16,17,18,19,20 ]:
        return False
    elif sdb.classes[4][3] != [2,3,4,5,6]:
        return False
    else:
        return True    

def test_get_professor(sdb):
   if sdb.classes[0][1] != "Prof. Kumar":
       return False
   elif sdb.classes[1][1] != "Prof. Bui":
       return False
   elif sdb.classes[2][1] != "Prof. Kogge":
       return False
   elif sdb.classes[3][1] != "Prof. Stober":
       return False
   elif sdb.classes[4][1] != "Prof. Kumar":
       return False
   else:
       return True

def test_get_class(sdb):
   if sdb.classes[0][0] != "Programming Paradigms":
       return False
   elif sdb.classes[1][0] != "Computer Ethics":
       return False
   elif sdb.classes[2][0] != "Theory of Computing":
       return False
   elif sdb.classes[3][0] != "Accountancy":
       return False
   elif sdb.classes[4][0] != "Discrete Math":
       return False
   else:
       return True

def test_get_goal(sdb):
    if sdb.classes[0][2] != 50:
       return False
    elif sdb.classes[1][2] != 12:
       return False
    elif sdb.classes[2][2] != 5:
       return False
    elif sdb.classes[3][2] != 35:
       return False
    elif sdb.classes[4][2] != 50:
       return False
    else:
       return True

def test_set_goal(sdb):
    sdb.set_goal(2, 5000)
    if sdb.classes[2][2] != 5000:
       return False
    else:
       return True

if __name__ == '__main__':
    sdb = _student_database()
    sdb.load_classes("../data/classes.csv")
    test_all(sdb)
