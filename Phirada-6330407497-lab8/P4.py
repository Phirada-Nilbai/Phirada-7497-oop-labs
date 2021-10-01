#Phirada Nilbai 633040749-7 P4
class ComEnStudent:
     def __init__(self,name,courses):
          self.name = name
          self.courses = courses

     def take_courses(self, *courses):
          for courses in courses:
               self.courses.append(courses)

     def __str__(self):
          return f"{self.name} has taken these courses:{self.courses}"


class CoEStudent(ComEnStudent):
     def __init__(self,name,courses):
          super().__init__(name,courses)


class DMEStudent(ComEnStudent):
     def __init__(self,name,courses):
         super().__init__(name,courses)

     def make_content_type(self,content_type):
          self.content_type = content_type
          (f"specialized in creating content type:{self.content_type}")

     def __str__(self):
         return (f"{super().__str__()}\nspecialized in creating content type:{self.content_type}")


if __name__ == "__main__":
     com_student = []
     manee = CoEStudent("Manee",["EN813701"])
     mana =  DMEStudent("Mana",["EN842004"])
     manee.take_courses("EN813702","EN811301","EN811302")
     mana.take_courses("EN842005")
     mana.make_content_type("Infographics")
     com_student.append(manee)
     com_student.append(mana)
     for com_student in com_student:
          com_student.take_courses("SC401206")
          print(com_student)



