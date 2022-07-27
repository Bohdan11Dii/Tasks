class Course:
    def info_course(self, course_name):
        print(f"Your course  - {course_name}")


class Student:
    def info_student(self, name):
        print(f'Hello, {name}')


class Mediator:
    def __init__(self):
        self.user = Student()
        self.course = Course()

    def get_info_user(self, name):
        self.user.info_student(name)

    def get_info_course(self, course_name):
        self.course.info_course(course_name)


if __name__ == "__main__":
    us1  = Mediator()
    us1.get_info_user('Dima')
    us1.get_info_course("Python Deveoper")

    us2 = Mediator()
    us1.get_info_user('Diana')
    us1.get_info_course("Java Deveoper")



