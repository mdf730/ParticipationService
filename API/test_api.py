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

if __name__ == '__main__':
    sdb = _student_database()
    sdb.load_classes("../data/classes.csv")
    test_all(sdb)
