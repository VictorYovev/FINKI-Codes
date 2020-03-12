class Student:
    table = {}

    def __init__(self, name, surname, index, subject, theory, practice, labs):
        mark = (theory + practice + labs) // 10 if (theory + practice + labs) % 10 == 0 else ((
                                                                                                      theory + practice + labs) // 10) + 1
        if mark < 5:
            mark = 5
        if not self.table.__contains__(index):
            self.table[index] = [name, surname, [(subject, mark), ]]
        else:
            stu = self.table[index]
            stu1 = list(stu[2])
            stu1.append((subject, mark))
            stu[2] = stu1
            self.table[index] = stu

    @staticmethod
    def print(self):
        students = self.table.values()
        for stu in students:
            print('Student: %s %s' % (stu[0], stu[1]))
            for sub in stu[2]:
                print('\t%s: %d' % (sub[0], sub[1]))
            print()


while True:
    i = input().split(",")
    if i[0] == 'end':
        break
    Student(i[0], i[1], i[2], i[3], int(i[4]), int(i[5]), int(i[6]))
Student.print(Student)
