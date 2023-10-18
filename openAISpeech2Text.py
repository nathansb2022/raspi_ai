#!/usr/bin/env python3
#
# Build RaspberryPi chatbot with ChatGPT - Similar to smart speaker
# Configured to send responses to email for archiving
#
# Python program to translate
# speech to text, Google to recognize audio and ask chatgpt(OpenAI) a question.
# After reponse has been requested, verbally respond with the answer.
# Install the packages and start asking questions on your linux machine
# Remember to install required packages, add api key, and name of AI
# Tested on PRETTY_NAME="Ubuntu 23.10" 6.5.0-1005-raspi
#
# Sources
# https://www.analyticsvidhya.com/blog/2023/05/how-to-use-chatgpt-api-in-python/
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
# 	Configure email Note: hostname=localhost
# https://learnubuntu.com/send-emails-from-server/#google_vignette
#
# INSTALL
# pip3 install speechrecognition pyttsx3 openai pandas pyfiglet --break-system-packages
# sudo apt install espeak jackd2 python3-pyaudio flac
#
#Be sure to restart RaspberryPi
#
# import these libraries, may have to use pip3 install for many of them (above command)
import speech_recognition as sr, sys, pyttsx3, openai, os, time, pandas as pd, warnings, pyfiglet
from colorama import Fore
import openAIJarvis
warnings.filterwarnings('ignore')

# Variables
OKEY = openAIJarvis.OKEY
name = openAIJarvis.name
flavor = openAIJarvis.flavor
mailaddr = openAIJarvis.mailaddr
# Initialize the recognizer
r = sr.Recognizer()

# reach out and get the response from chatgpt
def get_completion(prompt, flavor):

	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=flavor,
		messages=messages,
		temperature=0,
		)
	return response.choices[0].message["content"]
 
# Function to convert text to
# speech
def SpeakText(command):
	 
	# Initialize the engine
	engine = pyttsx3.init()
	engine.setProperty('rate', 140)
	engine.say(command)
	engine.runAndWait()

# introduction function
def milliDollarQuestion(name):    

	ask = "Hello! This is " + name + ". What would you like to ask?"
	print('')
	print('')
	print(Fore.MAGENTA + ask + "\n")
	SpeakText(ask)

# Loops waiting for the keyword jarvis then asks chatgpt your question utilizing google trans. and
# responds
def interact(r,flavor,OKEY,name,mailaddr):
		# get AI model
	flavor = openAIJarvis.checKAIModel(flavor)
	# input put your api key below if not set above
	OKEY = openAIJarvis.checKAPIKey(OKEY)	
	openai.api_key = OKEY
	# Find out what you named your AI
	name = openAIJarvis.checKAIName(name)
	# check if the email has been input
	mailaddr = openAIJarvis.checkEmail(mailaddr)
	milliDollarQuestion(name)
	# Loops waiting for the request then asks chatgpt your question utilizing google trans. and
	# responds
	while(1):   
		# Exception handling to handle
		# exceptions at the runtime
		try:
			# use the microphone as source for input.
			with sr.Microphone() as source2:
				 
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level
				r.adjust_for_ambient_noise(source2, duration=0.2)
				 
				# listens for the user's input
				audio2 = r.listen(source2)
				 
				# Using google to recognize audio
				MyText1 = r.recognize_google(audio2)
				MyText = MyText1.lower()
				response = get_completion(MyText, flavor)
				print('')
				print('')
				emailCommand = 'myText="' + MyText1 + '";response="' + response + '";when=$(date "+%Y-%m-%d-%T");echo "What was asked: " $myText " Answer: " $response | mail -s $when ' + mailaddr
				os.system(emailCommand)

				# if you hear these exit the program
				if "exit" in str(MyText) or "bye" in str(MyText) or "sleep" in str(MyText):
					SpeakText("Ok bye. Have a goodin!")
					exit()
				# reference for what was asked
				print(Fore.RED + "Did you ask ",MyText)
				print('')
				print('')
				# print response from chatgpt
				print(Fore.YELLOW + response)
				# now speak it
				SpeakText(response)
				print('')
				print('')
				 
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			 
		except sr.UnknownValueError:
			print("unknown error occurred\n")
			
if __name__ == "__main__":
	interact(r,flavor,OKEY,name,mailaddr)

	 
