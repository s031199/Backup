import os, shutil
from datetime import datetime
import traceback

def dateTime():
	now = datetime.now()
	current_time = str(now.strftime("%Y-%m-%d %H:%M:%S:%f"))
	return current_time

def logShowDirectory():
	logShowDirectory = dateTime() + " " + os.getcwd() + "\n"
	return logShowDirectory

def logCopyFolder():
	now = datetime.now()
	current_time2 = str(now.strftime(f"%Y-%m-%d %H-%M-%S"))
	try:
		shutil.copytree('A:/python darbai/test_UVS', f'A:/python darbai/test_UVS_Copy_{current_time2}')
		logCopyFolder = dateTime() + " " + "Folder Backup Is Created\n"
	except Exception as e:
		logCopyFolder = dateTime() + " " + str(e) + "\n"
	return logCopyFolder

def mainfolderexist():
	try:
		if os.path.exists("A:/python darbai/test_UVS") is True:
			mainFolderExist = dateTime() + " " + "Folder Exist\n"
		else:
			mainFolderExist = dateTime() + " " + "Folder Not Exist\n"
	except Exception as e:
		mainFolderExist = dateTime() + " " + str(e) + "\n"
	return mainFolderExist

def configfileexist():
	try:
		if os.path.exists('./Config.txt') is True:
			configFileExist = dateTime() + " " + "Config file Exist\n"
		else:
			configFileExist = dateTime() + " " + "Config file Not Exist\n"
	except Exception as e:
		configFileExist = dateTime() + " " + str(e) + "\n"
	return configFileExist