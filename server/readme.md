Port number: 51029

Our webserivce can be used to get information about our participation 
service from a web browser. Below, I'll enumerate specifically what each 
function does and, when applicable, how it fits into the client we will
make.

#GET for /students/{studentID} --> get information on a specific student

#GET for /students/{studentID}/{classID} --> get participation point count for a
certain student in a given class

#PUT for /students/{studentID}/{classID} --> add participation points to a
certain student in a given class

#DELETE for /students/{studentID}/{classID} --> Delete a specific student from
a certain classes roster (ex: if they dropped the class)

#GET for /students/ --> get information on all students

#DELETE for /students/ --> delete all students, this would be useful to delete
all seniors once they're done with their last semester

#PUT for /students/:sid --> add a new student

#GET for /class/:id --> get information on a specific class

#GET for /class/ --> get information on every class

#DELETE for /class/ --> delete all current classes, this would be useful at the
end of the semester before we upload new classes

#PUT for /class/:cid --> adds a new class to the list of classes

#DELETE for /class/:cid --> delete a specific class from our list of classes
(for example, if one class doesn't have enough students and is cancelelled)

#GET for /images/{studentID} --> gives us the filepath to student photos for
display on server

#PUT for /reset/ --> this resets back to our default data for continuity in
tests
