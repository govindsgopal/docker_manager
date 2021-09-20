import os
import json

def menu():
	print("1.Show container status")
	print("2.Download new image")
	print("3.Run container")
	print("4.Delete container")
	print("5.Network details of container")
	print("6.Modify network details of container")
	print("7.Exit")
def container_status():
	command = 'docker ps -a '
	res = os.popen(command).read()
	print(res)
	
def download_image():
	img_name = input("Enter the name of docker image to download :  ")
	img = os.popen("docker pull"+" " +img_name).read()
	print(img)
	print("Download complete")
	
def run_container():
	img_name = input("Enter the name of image file to run :  ")
	cont_name = input("Enter a name for the container :  ")
	command = f'docker run --name {cont_name} {img_name}'
	res = os.popen(command).read()
	print(res)
def delete_container():
	container_status()
	cont_name = input("Enter the name of the container to remove :  ")
	command = f'docker rm {cont_name}'
	result = os.popen(command).read()
	print(result)
	print(f"Docker container {cont_name} was succesfully removed :  ")
def container_network_details():
	command = 'docker network inspect bridge'
	result = os.popen(command).read()
	print(result)	
def mod_menu():
	print("1.Disconnect container from network")
	print("2.Connect container to network")
	print("3.Exit")
def disconnect_form_network():
	command = 'docker network ls'
	res = os.popen(coomand).read()
	print(res)
	net_id = input("Enter the network id :  ")
	cont_name = input("Enter the container to disconnect from network :  ")
	command = f'docker network disconnect {net_id} {cont_name}'
	result = os.popen(command).read()
	print(result)	
def connect_to_network():
	command = 'docker network ls'
	res = os.popen(coomand).read()
	print(res)
	net_id = input("Enter the network id :  ")
	cont_name = input("Enter the container to connect to network :  ")
	command = f'docker network connect {net_id} {cont_name}'
	result = os.popen(command).read()
	print(result)	
def mod_container_network_details():
	mod_menu()
	choice = input("Enter your choie")
	if choice == '1':
		disconnect_form_network()
	elif choice == '2':
		connect_to_network()
while True:
	menu()
	ch = input("Enter your choice :  ")
	if ch == '1':
		container_status()
	elif ch == '2':
		download_image()
	elif ch == '3':
		run_container()
	elif ch == '4':
		delete_container()
	elif ch == '5':
		container_network_details()
	elif ch == '6':
		mod_container_network_details()
	elif ch == '7':
		break
	else:
		print("Invalid input, try again")
