"""Replaces temperature with query"""


class Employer:
    """Represents employer"""

    def __init__(self, name):
        self.name = name

    def send(self, students):
        """Returns a print statement with student contact info"""
        print(f'''{students} contact info were sent to {self.name}.''')


class Student:
    """Represents students"""
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        """Returns students gpa"""
        return self.gpa

    def send_congrat_email(self):
        """Prints congradulation statement"""
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    """Represents school"""
    def __init__(self, students):
        self.students = students

    def process_graduation(self):
        """Find the students in the school who have successfully graduated"""
        min_gpa = 2.5  # minimum acceptable GPA
        passed_students = []
        for student in self.students:
            if student.get_gpa() > min_gpa:
                passed_students.append(student)

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for student in passed_students:
            print(student.name)
        print('****************************')
        # Send congrat emails to them.
        for student in passed_students:
            student.send_congrat_email()
        # Find the top 10% of them and send their contact to the top employers
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer(
            'Free Software Foundation'), Employer('Google')]
        for employee in top_employers:
            employee.send(top_10_percent)


students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'),
            Student(3.9, 'naruto'), Student(3.2, 'kami'), Student(3, 'guts')]
school = School(students)
school.process_graduation()
