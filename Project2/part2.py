import os
def main():
	#name of the win/lose file goes here
	while os.path.isfile('./end_game') == False:
		if os.path.isfile('./GroupX.go') == True:

			os.system('python project2.py')

if __name__ == "__main__":
	main() 
