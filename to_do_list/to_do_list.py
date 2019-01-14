class ToDoList:

	def __init__(self,to_do,done):
		self.to_do = []
		self.done = []

	def add(self):
		n = eval(input("Enter the no. of tasks:"))
		for i in range(n):
			task = input("Enter the tasks:")
			self.to_do.append(task)
			
	def mark_done(self):
		t = input("enter the tasks done:")
		self.to_do.remove(t)
		self.done.append(t)

	def see_tasks(self):
		print(self.to_do)
		print(self.done)
