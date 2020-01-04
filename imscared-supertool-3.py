def banner():
	print("=====IMSCARED (2016) Supertool=====")
	print()
	print("Originally written by Parzival Wolfram in Python 2")
	print("Cleaned up and updated to Python 3 by QuarkSR")
	print()
	print("I wish people still put their heart and soul into their programs...")
	print("I miss the DOS days. And I wasn't even alive yet at that time!")
	print()
	print("===================================")
	print()

def cleanup(status):
	from os import remove
	if status == 0:
		remove("imscared.zip")
	elif status == 1:
		remove("imscared.zip")
		exit()
	else:
		print("Unknown cleanup status. Exiting.")
		exit()

def choose():
	choice = -1

	print("Enter a number corresponding to an option below:")
	print()

	while True:
		print("1 - Download and automatically extract the filled \"imscared\" folder.")
		print("(Recommend dropping this program on the desktop first!)")
		print("2 - Time-set script! Use this to set the time to the Lucky Ticket times automatically!")
		print("3 - Reset your progress (for set up of a new run)")
		print("4 - Patch the revolver! INFINITE AMMO!")
		print()
		print("0 - Exit")
		print()

		try:
			choice = int(input("> "))
			assert choice in range(5)

			if choice == 0:
				exit()
			elif choice == 1:
				downloadAndExtract()
			elif choice == 2:
				setTime()
			elif choice == 3:
				reset()
			elif choice == 4:
				revolver()
		except ValueError:
			print()
		except AssertionError:
			print()

def downloadAndExtract():
	from zipfile import ZipFile
	from os.path import exists
	from urllib.request import urlretrieve

	zip = "https://uploads-from-an-external-server.weebly.com/uploads/1/1/6/2/116274509/imscared.zip"

	print()
	print("Downloading imscared.zip...")
	urlretrieve(zip, "imscared.zip")

	print()
	print("Extracting imscared.zip...")
	with ZipFile("imscared.zip") as z:
		z.extractall()

	print()
	print("Checking it extracted properly...")
	if exists("imscared\\revolver.ini"):
		print("Everything looks good.")
		print("Cleaning up...")
		cleanup(0)
		print()
		print("===================================")
		print()
	else:
		print("Looks like something went wrong.")
		print("Cleaning up and then aborting.")
		cleanup(1)

def setTime():
	from time import sleep
	from urllib.request import urlopen
	from os import system

	print("Setting clock to 7:45 AM...")
	system("time 07:45:00 AM")
	sleep(10)

	print("Setting clock to 8:23 PM...")
	system("time 08:23:00 PM")
	sleep(10)

	print("Setting clock to 12:00 AM...")
	system("time 12:00:00 AM")
	sleep(10)

	print("Restoring correct time from the internet...")
	realTime = urlopen("https://just-the-time.appspot.com/").read().decode("utf-8").strip()
	system(f"time {realTime[11:]}")
	print("Time restored.")

	print()
	print("===================================")
	print()

def reset():
	from os import getenv, system, remove
	dataDir = getenv("APPDATA")
	dataDir += "\\IMSCARED"

	print("Erasing save data...")

	system("taskkill /im imscared.exe /f")
	remove(f"{dataDir}\\white.ini")
	remove(f"{dataDir}\\workshop.ini")

	print("Done!")

	print()
	print("===================================")
	print()

def revolver():
	from os import getenv, system, remove
	from shutil import copyfile
	dataDir = getenv("APPDATA")
	dataDir += "\\IMSCARED"

	print("Patching...")

	with open("revolver.ini", "w") as f:
		f.write("[revolver]\nbullets=\"6.000000\"")

	system("taskkill /im imscared.exe /f")
	remove(f"{dataDir}\\revolver.ini")
	copyfile("revolver.ini", f"{dataDir}\\revolver.ini")
	system("attrib %APPDATA%\\IMSCARED\\revolver.ini +r")

	print("Done!")

	print()
	print("===================================")
	print()

banner()

while True:
	choose()
