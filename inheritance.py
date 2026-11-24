policyList=[]
studentDict = {"student": 1.75,
               "student2": 2.0,
               "student3": 1.5}
class CD:
    def __init__(self, newPolicy):
        self.newPolicy = newPolicy

    def implementPolicy(self):
        self.newPolicy.append(policyList)

    def announcePolicy(self):
        print(self.newPolicy)

class CID(CD):
    def __init__(self, newPolicy, newCurriculum):
        super().__init__(newPolicy)
        self.newCurriculum = newCurriculum
        self.implementedNewCurriculum = False
        self.curriculumStatus = "Pending"
        self.curriculumScore = 0

    def implementCurriculum(self):
        self.implementedNewCurriculum = True
        self.curriculumStatus = "Implemented"
        print(f"Curriculum implemented: {self.newCurriculum}")

    def evaluateCurriculum(self, score):
        self.curriculumScore = score
        self.curriculumStatus = "Evaluated"
        print(f"Curriculum evaluation score: {score}")

class SSD(CD):
    def __init__(self, newPolicy, codeOfConduct, programs):
        super().__init__(newPolicy)
        self.codeOfConduct = codeOfConduct
        self.programs = programs

    def addProgram(self, program):
        self.programs.append(program)
        print(f"Program added: {program}")

    def checkStudentSupport(self, studentName):
        print(f"Checking support for {studentName} under {self.codeOfConduct}")

class Dormitory(SSD):
    def __init__(self, newPolicy, codeOfConduct, programs):
        super().__init__(newPolicy, codeOfConduct, programs)

class Adviser(CID):
    def __init__(self, newPolicy, newCurriculum, students):
        super().__init__(newPolicy, newCurriculum)
        self.students = students

    def showGrade(self, name):
        print(name.self.students)

class Teacher(CID):
    def __init__(self, newPolicy, newCurriculum):
        super().__init__(newPolicy, newCurriculum)

class IDK(CID):
    def __init__(self, newPolicy, newCurriculum):
        super().__init__(newPolicy, newCurriculum)

class Student(Adviser):
    def __init__(self, newPolicy, newCurriculum, students, name):
        super().__init__(newPolicy, newCurriculum, students)
        self.studentName = name

    def askGrade(self):
        print(self.showGrade(self.studentName))
