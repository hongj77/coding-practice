# Complete the functions below.

# key will be respective IDs
classes = {}
students = {}

# key will be class ID, value is student IDs who have enrolled
enrolled = {}

def addClass(id, capacity, time):
    if id in classes:
        return "Error adding class " + str(id)
    else:
        # if id is in classes => id is in enrolled
        # cap, time, # that can enroll
        classes[id] = (capacity, time, capacity)
        enrolled[id] = []
        return "Successfully added class " + str(id)
  
  # If the class is added successfully, 
  # return "Successfully added class ID". 
  # Otherwise, return "Error adding class ID".
  
def removeClass(id):
    if id not in classes:
        return "Error removing class " + str(id)
    else:
        # id is in classes
        # clear enrolled list
        del classes[id]
        for studentId in enrolled[id]:
            # update counts
            s_cap, s_start, s_end, s_currentNum = students[studentId]
            s_new = s_currentNum-1
            students[studentId] = (s_cap, s_start, s_end, s_new)
        del enrolled[id]
        return "Successfully removed class " + str(id)
    
  # If the class is removed successfully,
  # return "Successfully removed class ID". 
  # Otherwise, return "Error removing class ID".
  
def infoClass(id):
    if id not in classes:
        return "Class " + str(id) + " does not exist" 
    else:
        # id is in classes => id is in enrolled
        if len(enrolled[id]) == 0:
            return "Class " + str(id) + " is empty"
        else:
            res = "Class " + str(id) + " has the following students: "
            enrolled_list = enrolled[id].sort()
            listString = ""
            
            string_list = str(enrolled_list).replace("[","").replace("]","").replace(" ","")
            res += string_list
            return res
         
  # If the class does not exist, 
  # return "Class ID does not exist". 
  # If the class is empty, 
  # return "Class ID is empty". 
  # Otherwise, return the string 
  # "Class ID has the following students: LIST" 
  # where LIST is a sorted, comma-separated list 
  # of student IDs corresponding to students currently 
  # in the class.
  
def addStudent(id, capacity, start, end):
    if id not in students:
        # cap, start, end, currentNum
        students[id] = (capacity, start, end, 0)
        return "Successfully added student " + str(id) 
    else:
        # already student with given ID
        return "Error adding student " + str(id) 
        
  # If the student is added successfully, 
  # return "Successfully added student ID". 
  # Otherwise, return "Error adding student ID".
  
def removeStudent(id):
    if id not in students:
        return "Error removing student " + str(id)
    else:
        # remove student
        del students[id]
        # unenroll student from all enrolled classes
        for classes, enrolled_list in enrolled.iteritems():
            for student_id in enrolled_list:   
                isInClass = False
                
                if student_id == id:
                    isInClass = True
                    
                if isInClass == True:
                    enrolled_list.remove(id)
                    
        return "Successfully removed student " + str(id)
    
  # typo in the instructions
  # If the student is removed successfully, 
  # return "Successfully removed student ID". 
  # Otherwise, return "Error removing student ID".
  
def infoStudent(id):
    if id not in students:
        return "Student " + str(id) + " does not exist"
    else:
        classList = []
        
        for classid, enrollment_list in enrolled.iteritems():
            if id in enrollment_list:
                classList.append(classid)
        
        if len(classList) == 0:
            return "Student " + str(id) + " is not taking any classes"
        else:
            res = "Student " + str(id) + " is taking the following classes: "
            classList.sort()
            res += str(classList).replace("[","").replace("]","").replace(" ", "")
            return res 
            
     
  # If the student does not exist, 
  # return "Student ID does not exist". 
  # If the student is not taking any classes, 
  # return "Student ID is not taking any classes". 
  # Otherwise, return the string 
  # "Student ID is taking the following classes: LIST" 
  # where LIST is a sorted, comma-separated list of class IDs 
  # corresponding to classes that the student is 
  # currently taking.
  
def enrollStudent(studentId, classId):
    # valid student
    if studentId in students:
        # valid class
        if classId in classes:
            enrolledList = enrolled[classId]
            # not currently enrolled in class
            if studentId not in enrolledList:
                s_cap, s_start, s_end, s_currentNum = students[studentId]
                # student has cap to take the class
                if s_currentNum < s_cap:
                    c_cap, c_time, c_currentNum = classes[classId]
                    # class has space for student
                    if c_currentNum > 0:
                        # class fits in student's time
                        if (c_time <= s_end) and (c_time >= s_start):
                            # if student is not already taking a class at that time
                            enrolledClasses = [] # list of all the classes enrolled for student
                            for classesId, enrollment_list in enrolled.iteritems():
                                if studentId in enrollment_list:
                                    enrolledClasses.append(classesId)
                                    
                            conflict = False
                            for classesId in enrolledClasses:
                                if classesId == classId:
                                    conflict = True
                            # no other classes at this time
                            if conflict == False:
                                # enroll the student
                                enrolled[classId].append(studentId)
                                # update the counts
                                s_new = s_currentNum+1
                                students[studentId] = (s_cap, s_start, s_end, s_new)
                                c_new = c_currentNum-1
                                classes[classId] = (c_cap, c_time, c_new)
                                return "Number of free spots left in class "+ str(classId) + ": " + str(c_new)
                                
    return "Enrollment of student " + str(studentId) + " in class " + str(classId) + " failed"
            

  # If enrollment of the student in the class succeeded,
  # return "Number of free spots left in class CLASSID: FREESPOTS" 
  # where FREESPOTS is the number of free spots left 
  # in the class after the student enrolls. 
  # Otherwise, return "Enrollment of student STUDENTID in class CLASSID failed".

def unenrollStudent(studentId, classId):
    if studentId in students:
        if classId in classes:
            if studentId in enrolled[classId]:
                # unenrolling the student
                enrolled[classId].remove(studentId)
                # update counts
                s_cap, s_start, s_end, s_currentNum = students[studentId]
                s_new = s_currentNum-1
                students[studentId] = (s_cap, s_start, s_end, s_new)
                c_cap, c_time, c_currentNum = classes[classId]
                c_new = c_currentNum+1
                classes[classId] = (c_cap, c_time, c_new)
                return "Number of free spots left in class "+ str(classId) + ": " + str(c_new)
            
    return "Unenrollment of student " + str(studentId) + " in class " + str(classId) + " failed"
                
                
  # If unenrollment of the student in the class succeeded,
  # return "Number of free spots left in class CLASSID: FREESPOTS" 
  # where FREESPOTS is the number of free spots left in the class 
  # after the student unenrolls. Otherwise, return "Unenrollment 
  # of student STUDENTID in class CLASSID failed".
 