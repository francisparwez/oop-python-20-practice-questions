class Student:
    
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        
    def display_info(self):
        print(f"Student Name: {self.name}\nStudent ID: {self.student_id}\nGrade: {self.grade}")
        

if __name__ == "__main__":
    student1 = Student('Francis', '38332', 'F')
    student1.display_info()
