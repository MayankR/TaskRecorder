import os.path

def startInput():
	inp = "";
	while True and inp != "exit":
		inp = raw_input("Next command: ")
		s = inp.split()
		if s[0] == "start":
			print "Starting task"
		elif s[0] == "end":
			print "Ending task"
		elif s[0] == "create":
			create_task(s[1])
		elif s[0] == "exit":
			print "Bye Bye"

def create_task(task_name):
	if os.path.isfile("tasks/{0}.txt".format(task_name)):
		print "Task already exists"
		return
	task_file = open("tasks/{0}.dat".format(task_name), "a+")
	task_file.write(task_name + "\n")
	task_file.close()
	print "\"{0}\" task created".format(task_name)
	return

startInput()