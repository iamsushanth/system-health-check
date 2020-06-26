import requests
import socket
import shutil
import psutil


def check_localhost():
	localhost = socket.gethostbyname('localhost')
	return localhost == '127.0.0.1'

def connectivity_check():
	request = requests.get('https://www.google.com')
	return request.ok

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
	print("Error!")
elif check_localhost() and connectivity_check():
	print("Everything ok!")
else:
	print("Network check failed!")

