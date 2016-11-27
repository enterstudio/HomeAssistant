import speech_recognition as sr
from os import system


class AudioHandler(object):
	def __init__(self, energy_threshold=None, debug=True):
		self.energy_threshold = energy_threshold
		self.debug = debug
		self.mic = sr.Microphone()
		self.recognizer = sr.Recognizer()
		if self.energy_threshold:
			self.recognizer.energy_threshold = self.energy_threshold
		

	def speak(self, message):
		if self.debug:
			print "Alfred: '" + message + "'"
		system("say -v Fred '" + message + "'")

	def get_audio_as_text(self):
		with self.mic as source:
			if not self.energy_threshold:
				self.recognizer.adjust_for_ambient_noise(source)
			print("Talk to Alfred...")
			audio = self.recognizer.listen(source)
			text_message = self.recognizer.recognize_google(audio)
			# text_message = self.recognizer.recognize_wit(audio, key=access_token) 
			if self.debug:
				print "You: '" + text_message + "'"
			return text_message