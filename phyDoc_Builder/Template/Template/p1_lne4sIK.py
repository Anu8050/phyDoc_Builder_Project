class Node:
  
#Constructor initializing the node object
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.next = None
  
class LinkedList:
  
#this function is for initialize head
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.head = None

# this function is to sort the name
    def sortedInsert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
  
        
        elif self.head.name >= new_node.name:
            new_node.next = self.head
            self.head = new_node
  
        else :
            current = self.head
            while(current.next is not None and
                 current.next.name < new_node.name):
                current = current.next
              
            new_node.next = current.next
            current.next = new_node
  
#this Function is to insert a new node at the beginning  
    def push(self, name, age, salary):
        new_node = Node(name)
        age = Node(age)
        salary = Node(salary)
        new_node.next = self.head
        self.head = new_node
    
    def personal_details(self,name,age,salary):
        self.name = name 
        self.age = age
        self.salary = salary
    # print("Name: {}\nAge: {}\nsalary{}: ")

#function to print  the LinkedList
    def printList(self,name,age,salary):
        temp = self.head
        print(name)
        print(age)
        print(salary)
        while(temp):
            print(temp.name)
            temp = temp.next
        # print(name)
        # print(age)
        # print(salary)
  
# details =  LinkedList()
linklist = LinkedList()
new_node =Node("vda")
person=("vda",20,4000)
linklist.sortedInsert(new_node)
# linklist.personal_details(person)
# per = ("priya",20,4000)
# new_node = Node("priya")
# linklist.sortedInsert(new_node)
# per = ("divya",20,4000)
# new_node = Node("divya")
# linklist.sortedInsert(new_node)
# per = ("vijet",20,4000)
# new_node = Node("vijet")
# linklist.sortedInsert(new_node)
# per = ("anusha",20,4000)
# new_node =  Node("anusha")
# linklist.sortedInsert(new_node)
# per = ("akshatha",20,4000)
# new_node =  Node("akshatha")
# linklist.sortedInsert(new_node)
# per = ("sada",20,4000)
# new_node = "sada"
# linklist.sortedInsert(new_node)
# per = ("praveen",20,4000)
# new_node = "praveen"
# linklist.sortedInsert(new_node)
# per = ("suhas",20,4000)
# new_node ="suhas"
# linklist.sortedInsert(new_node)
# per = ("atharva",20,4000)
# new_node =  Node("atharva")
# linklist.sortedInsert("new_node")

linklist.printList()