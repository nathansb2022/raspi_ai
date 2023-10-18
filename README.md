# raspi_ai

Build a RaspberryPi chatbot with ChatGPT API key integrated. Very similar to a smart speaker. It is configured to send responses to email for archiving. See link below to email chatGPT repsonse. This is just to initiate the conversation by using keyword "Jarvis" and you will receive a "Working Now". Once you hear "Working Now", you will be able to ask your
questions. Remember to end the conversation with sleep, bye, or exit. This will allow you exit the inner loop and go back to listenting for the keyword "Jarvis".

The python program translates speech to text, uses Google to recognize audio, and asks chatgpt(OpenAI) a question. A verbal reponse will be provided on the asked question.
Your AI partner is stored in openAIJarvis.py and openAISpeech2Text.py. Install the packages and start asking questions on your raspberrypi.
Remember to install required packages, add api key, language model, gmail address, and name of AI. Tested on "Ubuntu 23.10" 6.5.0-1005-raspi.

# Add Variables

Add variables in openAIJarvis.py or add at runtime.

# Sources

[Python_ChatGPT](https://www.analyticsvidhya.com/blog/2023/05/how-to-use-chatgpt-api-in-python/)

[text2Speech_Python](https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/)

Set hostname=localhost instead of what is mentioned in this link
[Archive via email](https://learnubuntu.com/send-emails-from-server/#google_vignette)

# How to Use

Put in opt directory
```bash
cd /opt; git clone https://github.com/nathansb2022/raspi_ai.git
```   
For AI initialization
```bash
python3 openAIJarvis.py
```               

# Install Requirements

To get python squared away:
```bash
sudo pip3 install speechrecognition pyttsx3 openai pandas pyfiglet --break-system-packages
```
To get linux squared away:
```bash
sudo apt install espeak jackd2 python3-pyaudio flac
```
