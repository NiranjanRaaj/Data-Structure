class node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.pre=None
		
class dl:
	def __init__(self):
		self.head=None
		
	def disp(self):
		t=self.head
		while(t):
			print(t.data)
			t=t.next

n1=dl()
n1.head=node(1)
n2=node(2)
n3=node(3)
n4=node(4)

n1.head.next=n2
n2.next=n3
n3.next=n4

n2.pre=n1
n3.pre=n2
n4.pre=n3

n1.disp()
			


		
		
		