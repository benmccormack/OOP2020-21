# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: Ben McCormack
# date: 13-11-2020

class Student:
    """
    The component class of the composition.
    This class contains information about the Student
    ...
    Attributes:
        UNDERGRADUATE, POSTGRADUATE = range(2)
        used to define the level of study of a student.
        There are class variables / global variables
        Can be accessed via student.POSTGRADUATE

        __study_type : range(2)
        Only allowed the predefined class variables of
        UNDERGRADUATE and POSTGRADUATE.

        __f_name : str
        First name of a student

        __l_name : str
        Last name of a student

        __courses : list
        contains a list of courses that the student is enrolled into.
        This is empty by default.

    Methods:
        study_type : property
            returns either UNDERGRADUATE or POSTGRADUATE. Also available as a setter
            an error is raised if the returned value does not match the tuple

        first_name : property
            returns the first name of the student if this value is a string,
            otherwise an exception is raised. Cannot be used as a setter

        last_name : property
            returns the last name of a student if this value is a string,
            otherwise and exception is raised. Can be used as a setter

        courses : property
            returns the list of courses a student is enrolled in. Also contains
            a setter that allows student to enroll in a new course
    """

    #STUDY_TYPE = (UNDERGRADUATE, POSTGRADUATE)
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, study_type, f_name, l_name):
        if study_type not in (Student.UNDERGRADUATE, Student.POSTGRADUATE):
            raise ValueError

        self.__study_type = study_type
        self.__f_name = f_name
        self.__l_name = l_name
        self.__courses = []

    # getter for study_type
    @property
    def study_type(self):
        return self.__study_type

    # setter for study_type
    @study_type.setter
    def study_type(self, value):
        if value == "UNDERGRADUATE" or value == "POSTGRADUATE":
            self.__study_type = value
        else:
            raise Exception("Error: Study type cannot be set")

    # getter for first name
    @property
    def first_name(self):
        return self.__f_name

    # getter for last name
    @property
    def last_name(self):
        return self.__l_name

    # setter for last name
    @last_name.setter
    def last_name(self, value):
        if type(value) == str:
            self.__l_name = value
        else:
            raise Exception("Error, Surname provided is not a string")

    # getter for courses
    @property
    def courses(self):
        return self.__courses

    # setter for courses - we want to add newly entered courses to a list using append
    @courses.setter
    def courses(self, value):
        if type(value) == str:
            # adding the course to the list
            self.__courses.append(value)
        else:
            raise Exception("Course entered is not a string")

    # get all student data
    def get_all_student_data(self):
        return self.study_type, self.first_name, self.last_name, self.courses


class RegistrationData:
    """
    This class holds information about the registration data related
    to the student

    Attributes:
        __address : str
            returns the address. Also available as a setter

        __registration_fee : int
            returns the fee to be paid by the student

        __s_id : str
            Originally the student id of a student in NA
            This is changed later down the line

        __student_obj : Student
            Student object, takes f_name, l_name and study_type
            as Arguments from Student
    Methods:
        student_object_property : property
            returns __student_obj

        student_id_property : property
            returns the __s_id of a student, also available
            as a setter and an error check to ensure supplied id is a string

        address_property : property
            returns __address, also available as a setter

        registration_fee_property
            returns __registration_fee, also available as a setter

        display_student_data
            prints all available information on the student to the screen
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.__address = address
        self.__registration_fee = registration_fee
        self.__s_id = s_id
        try:
            self.__student_obj = Student(study_type, f_name, l_name) # object of the student class
        except Exception as e:
            pass

    @property
    def student_object_property(self):
        return self.__student_obj

    # student id getter
    @property
    def student_id_property(self):
        return self.__s_id

    # student id setter
    @student_id_property.setter
    def student_id_property(self, value):
        if type (value) != str:
            raise TypeError
        else:
            self.__s_id = value

    # address property getter
    @property
    def address_property(self):
        return self.__address

    # address property setter
    @address_property.setter
    def address_property(self, value):
        if type (value) != str:
            raise TypeError
        else:
            self.__address = value

    # registration fee getter
    @property
    def registration_fee_property(self):
        return self.__registration_fee

    # registration fee setter
    @registration_fee_property.setter
    def registration_fee_property(self,value):
        self.__registration_fee = value

    # method to display student data
    def display_student_data(self):
        print("Student Info:",self.student_object_property.get_all_student_data(), self.student_id_property)
        print("Address:", self.address_property)
        print("Registration Fee:", self.registration_fee_property)


r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object_property.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)
