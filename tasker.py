import os.path
from datetime import datetime

def startInput():
	inp = "";
	while True and inp != "exit":
		inp = raw_input("Next command: ")
		s = inp.split()
		if s[0] == "start":
			start_task(s[1])
		elif s[0] == "end":
			print "Ending task"
		elif s[0] == "create":
			create_task(s[1])
		elif s[0] == "exit":
			print "Bye Bye"

def create_task(task_name):
	if os.path.isfile("tasks/{0}.dat".format(task_name)):
		print "Task already exists"
		return
	task_file = open("tasks/{0}.dat".format(task_name), "a+")
	task_file.write(task_name + "\n") # + ";" + str(datetime.now()))
	task_file.close()
	print "\"{0}\" task created".format(task_name)
	return

def start_task(task_name):
	if not os.path.isfile("tasks/{0}.dat".format(task_name)):
		print "Task does not exist"
		return
	task_file = open("tasks/{0}.dat".format(task_name), "r+")
	task_lines = task_file.readlines()
	# print task_lines
	task_lines_num = len(task_lines)
	# print task_lines_num
	last_line = task_lines[task_lines_num - 1]
	last_line_split = last_line.split(';')
	if len(last_line_split) == 2 and last_line_split[1] == "":
		print "Task already running"
		return
	elif len(last_line_split) == 2 or len(last_line_split) == 1:
		task_file.write(str(datetime.now())+";")
		print "Task started"
		return

startInput()