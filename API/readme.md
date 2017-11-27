 README
 Participation Web Service
 -------------------------

 This API should be used in conjunction with a web service that tracks participation points for 
 students in a class. From a broad perspective, this would be accomplished in two different frames. 
 First would be with a professor view. This view allows a specific professor (determined with 
 get_professor()) to access their class data. This dat includes the name of the class (using 
 get_class()), the goal for participation points over the semester (using get_goal()), the current 
 average points earned per student (using calculate_average()), the maximum points earned (using 
 calculate_max()), and a smaller widget for each student in the class. To determine the students in 
 the class, the get_students() method would be used. From there, a loop would be used to determine 
 from each unique student id the student's name (using get_student()), their image (stored at a url 
 from get_image()), and their participation points in the class (using get_points()). The dynamic 
 aspect of this page includes the professor having the ability to increase or decrease each 
 student's score (using a combination of get_points() and set_points()). Use cases for this include 
 tracking attendance, in class exerciese, discussion participation, asking questions during lecture,
 and more. Additionally, the professor would have the opportunity to change the target points for 
 the semester at any time (using set_points()).

 The second view would be for a specific student. The student, identified from their student id or 
 name (get_student()), would be able to see a table with real-time information about their 
 participation scores in all of their classes. This table would include the name of the class 
 (get_class()), their current point total in that class (get_points()), the goal total 
 (get_goal()), the average points students have earned (calculate_average()), and the max points 
 earned (calculate_max()). There would be no dynamic options for the student, as they shouldn't be 
 able to change their own participation scores.