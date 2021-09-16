#Phirada Nilbai 633040749-7
class Teacher:


    def __init__(self,name,office_no,research_work,*courses_work):
        self.name = name
        self.courses_work = courses_work
        self.office_no = office_no
        self.research_work = research_work


    def print_office_no(self):
        print (f'{self.name} has the office at {self.office_no}')


    def print_research_work(self):
        print (f'{self.name} is doing research in these topic {self.research_work}')


    def print_courses_work(self):
        print (f'{self.name} teaches these courses {self.courses_work}')

if __name__ =='__main__':
    manee = Teacher("Manee","Rm .4203","Artificial Intelligence","EN842004","EN8130701")
    mana = Teacher("Mana","Rm .4209","Internet of Things","EN842005","EN813703")
    manee.print_office_no()
    manee.print_research_work()
    manee.print_courses_work()
    mana.print_office_no()
    mana.print_research_work()
    mana.print_courses_work()
