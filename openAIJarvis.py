#!/usr/bin/env python3
#
# Build RaspberryPi chatbot with ChatGPT - Similar to smart speaker
# Configured to send responses to email for archiving
# This is just to initiate the conversation by using keyword "Jarvis" and will receive a "Working Now"
#
# Python program to translate
# speech to text, Google to recognize audio and ask chatgpt(OpenAI) a question.
# After reponse has been requested, verbally respond with the answer.
# Install the packages and start asking questions on your linux machine
# Remember to install required packages, add api key, and name of AI
# Tested on PRETTY_NAME="Ubuntu 23.10" 6.5.0-1005-raspi
# Sources
# https://www.analyticsvidhya.com/blog/2023/05/how-to-use-chatgpt-api-in-python/
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
# 	Configure email Note: hostname=localhost
# https://learnubuntu.com/send-emails-from-server/#google_vignette
#
# In checkAPIKey(), I commented out the env variable for my OpenAI API. Change if you would like
# In checkAIName, I commented out the name, jarvis. Change if you would like
# In checKAIModel(), I commented out the variable for the AI model (gpt-3.5-turbo). Change if you would like
#
# INSTALL
# pip3 install speechrecognition pyttsx3 openai pandas pyfiglet --break-system-packages
# sudo apt install espeak jackd2 python3-pyaudio flac
#
#Be sure to restart RaspberryPi
#
# import these libraries, may have to use pip3 install for many of them (above command)
import speech_recognition as tr, sys, pyttsx3, openai, os, time, pandas as pd, warnings, pyfiglet
from colorama import Fore
warnings.filterwarnings('ignore')

# BAKE IN VARIABLES BELOW
#####################################################################

# Input your Open API key here
# OKEY = os.environ.get('OKEY')
OKEY = ""
# Change name of Bot here
name = ""
# Change model here
# flavor = "gpt-4"
flavor = ""
# Change email here
# mailaddr = "<your email>@gmail.com"
mailaddr = ""

#####################################################################
# Initialize the recognizer
rr = tr.Recognizer()

# Opening art
def art():

	ascii_banner = pyfiglet.figlet_format("RASPI A.I.\n")
	print(Fore.CYAN + ascii_banner)

# check if the name has been input
def checKAIName(name):
	if not name:
		name = "jarvis"

		return name
	else:

		return name

# check if the api has been input
def checKAPIKey(OKEY):
	if not OKEY:
		OKEY = input("Please input the OpenAI API key: \n")

		return OKEY
	else:

		return OKEY

# check if the model has been input
def checKAIModel(flavor):
	if not flavor:
		flavor = input("Please input the model of your AI, i.e. gpt-3.5-turbo : \n")

		return flavor
	else:

		return flavor

# check if the email has been input
def checkEmail(mailaddr):
	if not mailaddr:
		mailaddr = input("Please input the email address to send responses: \n")

		return mailaddr
	else:

		return mailaddr

# Function to convert text to
# speech
def SpeakText1(command):
	 
	# Initialize the engine
	engine = pyttsx3.init()
	engine.setProperty('rate', 140)
	engine.say(command)
	engine.runAndWait()

# Loops waiting for the keyword jarvis then asks chatgpt your question utilizing google trans. and
# responds
def interact(rr,OKEY,name,flavor,mailaddr):
	# art
	art()
	# Loops waiting for keyword "Jarvis"
	while(1):   
		# Exception handling to handle
		# exceptions at the runtime
		try:
			# use the microphone as source for input.
			with tr.Microphone() as source3:
				 
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level
				rr.adjust_for_ambient_noise(source3, duration=0.2)
				 
				# listens for the user's input
				audio3 = rr.listen(source3)
				 
				# Using google to recognize audio
				MyText = rr.recognize_google(audio3)
				MyText = MyText.lower()
				print('')
				print('')
				# if you hear these enter the program
				if name in str(MyText):
					SpeakText1("Working Now!")
					os.system("/opt/raspi_ai/openAISpeech2Text.py")
				print('')
				print('')
		except tr.RequestError as e:
			print("Could not request results; {0}".format(e))
			 
		except tr.UnknownValueError:
			print("unknown error occurred\n")
			
if __name__ == "__main__":
	interact(rr,OKEY,name,flavor,mailaddr)

	 
