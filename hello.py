class student:
    

    def __init__(self, id, name) -> None:
        self.id= id
        self.name= name
        self.next= None

    def __display():
        print(f"id: (self.id), name: (self.name)")

student1= student(1, "KShama")
student2= student(2, "Yash")
student3= student(3, "Sneha")
student4= student(4, "Shweta")

l= [1,2,3,4,5]

for i in range(len(l)):
    print(i)

#student1.display()

student1.next= student2
student2.next= student3
student3.next= student4
student4.next= None

head= student1

while(head.next!= None):
    print(head.display())
    head= head.next 