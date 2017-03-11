import os.path
import os
from datetime import datetime

def startInput():
	inp = "";
	while True and inp != "exit":
		inp = raw_input("Next command: ")
		s = inp.split()
		corrected = False
		if s[0] == "exit":
			print "Bye Bye"
		elif len(s)==1:
			inp_argv = raw_input("Enter task: ")
			s.append(inp_argv)
			print s
		if len(s)>1:	
			if s[0] == "start":
				start_task(s[1])
			elif s[0] == "end" or s[0] == "stop":
				end_task(s[1])
			elif s[0] == "create" or s[0] == "make":
				create_task(s[1])
			else:
				error_msg = "Incorrect command. ",
				if s[0] == "ls" or s[0] == "list":
					error_msg = "Here,"				
				print error_msg,
				print" Below is the list of commands."
				list_tasks()
				for task in tasks:
					print task

def create_task(task_name):
	if os.path.isfile("tasks/tsk_{0}.dat".format(task_name)):
		print "Task already exists"
		return
	task_file = open("tasks/tsk_{0}.dat".format(task_name), "a+")
	task_file.write(task_name + "\n") # + ";" + str(datetime.now()))
	task_file.close()
	print "\"{0}\" task created".format(task_name)
	return

def start_task(task_name):
	if not os.path.isfile("tasks/tsk_{0}.dat".format(task_name)):
		print "Task does not exist"
		return
	task_file = open("tasks/tsk_{0}.dat".format(task_name), "r+")
	task_lines = task_file.readlines()
	task_lines_num = len(task_lines)
	last_line = task_lines[task_lines_num - 1]
	last_line_split = last_line.split(';')
	if len(last_line_split) == 2 and last_line_split[1] == "":
		print "Task already running"
		return
	elif len(last_line_split) == 2 or len(last_line_split) == 1:
		task_file.write(str(datetime.now())+";")
		print "Task started"
		return

def end_task(task_name):
	if not os.path.isfile("tasks/tsk_{0}.dat".format(task_name)):
		print "Task does not exist"
		return
	task_file = open("tasks/tsk_{0}.dat".format(task_name), "r+")
	task_lines = task_file.readlines()
	task_lines_num = len(task_lines)
	last_line = task_lines[task_lines_num - 1]
	last_line_split = last_line.split(';')
	if len(last_line_split) == 2 and last_line_split[1] != "":
		print "Task not running"
		return
	elif len(last_line_split) == 1:
		print "Task not running"
		return

	task_file.write(str(datetime.now())+"\n")
	print "Task ended"
	return

def list_tasks():
	all_dir = os.listdir("tasks/")
	tasks = []
	for f in all_dir:
		if f[0:4] == "tsk_":
			tasks.append(f[4:len(f)-4])
	return tasks

startInput()