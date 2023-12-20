from letprob import *

class Cipher(object):
	"""This is the Cipher Class"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.encodedString = ''
		self.decodedString = ''

	def __repr__(self):
		s = 'Original String: %s\nEncoded String: %s\nDecoded String: %s' \
		% (self.inputString, self.encodedString, self.decodedString)
		return s

	def encipher(self, n):
		""" Uses helper function positiveShift to encode the imput string. """
		self.encodedString = Cipher.positiveShift(self.inputString, n)

	def positiveShift(self, n):
		""" Checks if there are letters in the string(self)
		before shifting that letter up by n. If that makes
		not a letter, then wrap it around the alphabet. """
		newSelf = ''
		for L in self:
			if ord(L) <= 90 and ord(L) >= 65: #Capital Letters
				if (ord(L) + n) > 90:
					L = chr((ord(L) + n) - 26)
				else:
					L = chr(ord(L) + n)
			elif ord(L) >= 97 and ord(L) <= 122: #Lowercase Letters
				if (ord(L) + n) > 122:
					L = chr((ord(L) + n) - 26)
				else:
					L = chr(ord(L) + n)
			newSelf += L
		return newSelf

	def negativeShift(self, n):
		""" Checks if there are letters in the string(self)
		before shifting that letter down by n. If that makes
		not a letter, then wrap it around the alphabet. """
		newSelf = ''
		for L in self:
			if ord(L) <= 90 and ord(L) >= 65: #Capital Letters
				if (ord(L) - n) < 65:
					L = chr((ord(L) - n) + 26)
				else:
					L = chr(ord(L) - n)
			elif ord(L) >= 97 and ord(L) <= 122: #Lowercase Letters
				if (ord(L) - n) < 97:
					L = chr((ord(L) - n) + 26)
				else:
					L = chr(ord(L) - n)
			newSelf += L
		return newSelf

	def decipherEasy(self, n):
		""" Uses helper function negativeShift to encode the imput string. """
		self.decodedString = Cipher.negativeShift(self.encodedString, n)

	def shiftDecipher(self, n):
		""" Similar to positiveShift but applied to the decipher function. """
		newSelf = ''
		for L in self:
			if ord(L) <= 90 and ord(L) >= 65: #Capital Letters
				if (ord(L) + n) > 90:
					L = chr((ord(L) + n) - 26)
				else:
					L = chr(ord(L) + n)
			elif ord(L) >= 97 and ord(L) <= 122: #Lowercase Letters
				if (ord(L) + n) > 122:
					L = chr((ord(L) + n) - 26)
				else:
					L = chr(ord(L) + n)
			newSelf += L
		return newSelf

	def decipher(self):
		""" Iterates through every possible decipher and
		charater in encodedString. then it checks to see
		which decipher has the most uses of the highest
		monogram probability(letProb). """
		c = 0
		n = 0
		for L in self.encodedString:
			while n <= 26:
				n += 1
				if c < letProb(Cipher.shiftDecipher(L, n)):
					c = letProb(L)
					if c <= letProb(Cipher.shiftDecipher(self.encodedString, n)):
						self.decodedString = Cipher.shiftDecipher(self.encodedString, n)

def main():
	#not sure what to call here when turning in
	myEncoder = Cipher('Caesar cipher? I prefer Caesar salad.')
	myEncoder.encipher(25)
	print(myEncoder)

if __name__ == '__main__':
	main()
