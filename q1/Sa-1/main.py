class AssignmentsSubmission:
    def __init__(
        self,
        student_name: str,
        student_id: str,
        assignment_title: str,
        due_date: str,
    ):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date

        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score: float) -> bool:
        return 0 <= score <= 100

    def __check_submission_status(self) -> bool:
        return len(self.__submitted_files) > 0

    def __is_duplicate(self, filename: str) -> bool:
        return filename in self.__submitted_files

    def add_file(self, filename: str) -> bool:
        if self.__grade is not None:
            return False

        if self.__is_duplicate(filename):
            return False

        self.__submitted_files.append(filename)
        self.__is_submitted = True
        return True

    def remove_file(self, filename: str) -> bool:
        if self.__grade is not None:
            return False

        if filename not in self.__submitted_files:
            return False

        self.__submitted_files.remove(filename)

        if len(self.__submitted_files) == 0:
            self.__is_submitted = False

        return True

    def assign_grade(self, score: float) -> bool:
        if not self.__validate_grade(score):
            return False

        if not self.__check_submission_status():
            return False

        self.__grade = score
        self.__is_submitted = True
        return True

    def get_grade(self):
        return self.__grade

    def view_files(self) -> str:
        return str(self.__submitted_files)

    def get_file_count(self) -> int:
        return len(self.__submitted_files)

    def get_status_report(self) -> str:
        status = "Submitted" if self.__is_submitted else "Missing"
        grade = self.__grade if self.__grade is not None else "Not Graded"

        return (
            f"ID: {self.student_id} | "
            f"Name: {self.student_name} | "
            f"Status: {status} ({len(self.__submitted_files)} files) | "
            f"Grade: {grade}"
        )


print("\n--- INITIALIZING DROPBOX FOR STUDENTS ---\n")

student1 = AssignmentsSubmission(
    student_name="Alex Gonzaga",
    student_id="pshs-1090-x",
    assignment_title="CS-101",
    due_date="2026-10-01",
)

student2 = AssignmentsSubmission(
    student_name="Adelle",
    student_id="pshs-1020-x",
    assignment_title="CS-103",
    due_date="2026-10-01",
)

student3 = AssignmentsSubmission(
    student_name="Juan dela Cruz",
    student_id="pshs-1033-x",
    assignment_title="CS-101",
    due_date="2026-10-01",
)

student4 = AssignmentsSubmission(
    student_name="Maria Santos",
    student_id="pshs-1044-x",
    assignment_title="CS-101",
    due_date="2026-10-01",
)

student5 = AssignmentsSubmission(
    student_name="Jose Reyes",
    student_id="pshs-1055-x",
    assignment_title="CS-101",
    due_date="2026-10-01",
)

print("--- TEST SCENARIO 1: Multiple Files via List ---")

if student1.add_file("main.py"):
    print(
        f"--> [Success] Alex Gonzaga attached 'main.py'. "
        f"Total files: {student1.get_file_count()}"
    )

if student1.add_file("report.pdf"):
    print(
        f"--> [Success] Alex Gonzaga attached 'report.pdf'. "
        f"Total files: {student1.get_file_count()}"
    )

if student1.assign_grade(95):
    print("--> [Success] Grade 95 officially assigned to Alex Gonzaga.")

print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")

if student2.add_file("wrong_homework.docx"):
    print(
        f"--> [Success] Adelle attached 'wrong_homework.docx'. "
        f"Total files: {student2.get_file_count()}"
    )

if student2.remove_file("wrong_homework.docx"):
    print("--> [Success] Adelle removed 'wrong_homework.docx'.")

if student2.add_file("correct_project.py"):
    print(
        f"--> [Success] Adelle attached 'correct_project.py'. "
        f"Total files: {student2.get_file_count()}"
    )

if student2.assign_grade(88):
    print("--> [Success] Grade 88 officially assigned to Adelle.")

print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")

if student3.add_file("script.py"):
    print(
        f"--> [Success] Juan dela Cruz attached 'script.py'. "
        f"Total files: {student3.get_file_count()}"
    )

if not student3.add_file("script.py"):
    print("--> [Warning] script.py is already attached!")

print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")

if student4.add_file("exam_answers.pdf"):
    print(
        f"--> [Success] Maria Santos attached 'exam_answers.pdf'. "
        f"Total files: {student4.get_file_count()}"
    )

if student4.assign_grade(75):
    print("--> [Success] Grade 75 officially assigned to Maria Santos.")

if not student4.remove_file("exam_answers.pdf"):
    print(
        "--> [Warning] Maria Santos cannot remove files. "
        "Assignment already graded."
    )

print()

print("--- TEST SCENARIO 5: Empty List Handling ---")

if student5.add_file("draft.txt"):
    print(
        f"--> [Success] Jose Reyes attached 'draft.txt'. "
        f"Total files: {student5.get_file_count()}"
    )

if student5.remove_file("draft.txt"):
    print("--> [Success] Jose Reyes removed 'draft.txt'.")

if not student5.assign_grade(100):
    print("--> [Error] Cannot grade. No files submitted for Jose Reyes.")

print()

print("--- FINAL SYSTEM REPORT ---")

print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
