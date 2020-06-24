class Caesar(object):
	''' THE KEY FOR ENCRYPTION AND DECRYPTION SHOULD BE BETWEEN 1 AND 25 (1 AND 25 INCLUDED)'''
	def __init__(self, key):
		self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.numbers = ['0','1','2','3','4','5','6','7','8','9']
		self.key = key
		self.sentenceList = []


	def __repr__(self):
		return f"Caesar encryption/decryption obejet with KEY : {self.key}"


	def encrypt(self, word):
		conc_list = []
		for c in word:
			if c.upper() in self.letters:
				ind = self.letters.index(c.upper())
				e_ind = ind + self.key 
				if e_ind > 25:
					e_ind = self.key - (25 - ind) - 1
				e_c = self.letters[e_ind]
				if c == c.upper():
					conc_list.append(e_c)
				else:
					conc_list.append(e_c.lower())
			elif c in self.numbers:
				if 9 < self.key < 19:
					self.key = self.key - 9
				elif 19 <= self.key <= 25:
					self.key = self.key - 18
				ind = self.numbers.index(c)
				e_ind = ind + self.key 
				if e_ind > 9:
					e_ind = self.key - (9 - ind) - 1
				e_c = self.numbers[e_ind]
				conc_list.append(e_c)
			else:
				e_c = c 
				conc_list.append(e_c)
		return ''.join(conc_list)


	def decrypt(self, word):
		conc_list = []
		for c in word:
			if c.upper() in self.letters:
				ind = self.letters.index(c.upper())
				d_ind = ind - self.key 
				if d_ind < 0:
					d_ind = (ind - self.key) + 26
				d_c = self.letters[d_ind]
				if c == c.upper():
					conc_list.append(d_c)
				else:
					conc_list.append(d_c.lower())
			elif c in self.numbers:
				if 9 < self.key < 19:
					self.key = self.key - 9
				elif 19 <= self.key <= 25:
					self.key = self.key - 18
				ind = self.numbers.index(c)
				d_ind = ind - self.key
				if d_ind < 0:
					d_ind = (ind - self.key) + 10
				d_c = self.numbers[d_ind]
				conc_list.append(d_c)
			else:
				d_c = c 
				conc_list.append(d_c)
		return ''.join(conc_list)


	def encrypt_file(self, read_file, write_file):
		with open(read_file, 'r') as r_file:
			Lines = r_file.readlines()
			for line in Lines:
				formatted_line = line.split(' ')
				self.sentenceList.append(formatted_line)
		w_file = open(write_file, 'w')
		for sentence in self.sentenceList:
			for word in sentence:
				conc_list = []
				for c in word:
					if c.upper() in self.letters:
						ind = self.letters.index(c.upper())
						e_ind = ind + self.key 
						if e_ind > 25:
							e_ind = self.key - (25 - ind) - 1
						e_c = self.letters[e_ind]
						if c == c.upper():
							conc_list.append(e_c)
						else:
							conc_list.append(e_c.lower())
					elif c in self.numbers:
						if 9 < self.key < 19:
							self.key = self.key - 9
						elif 19 <= self.key <= 25:
							self.key = self.key - 18
						ind = self.numbers.index(c)
						e_ind = ind + self.key 
						if e_ind > 9:
							e_ind = self.key - (9 - ind) - 1
						e_c = self.numbers[e_ind]
						conc_list.append(e_c)
					else:
						e_c = c 
						conc_list.append(e_c)
				s = ''.join(conc_list)
				w_file.write(s)
				if sentence.index(word) != len(sentence)-1:
					w_file.write(" ")
		w_file.close()


	def decrypt_file(self, read_file, write_file):
		with open(read_file, 'r') as r_file:
			Lines = r_file.readlines()
			for line in Lines:
				formatted_line = line.split(' ')
				self.sentenceList.append(formatted_line)
		w_file = open(write_file, 'w')
		for sentence in self.sentenceList:
			for word in sentence:
				conc_list = []
				for c in word:
					if c.upper() in self.letters:
						ind = self.letters.index(c.upper())
						d_ind = ind - self.key 
						if d_ind < 0:
							d_ind = (ind - self.key) + 26
						d_c = self.letters[d_ind]
						if c == c.upper():
							conc_list.append(d_c)
						else:
							conc_list.append(d_c.lower())
					elif c in self.numbers:
						if 9 < self.key < 19:
							self.key = self.key - 9
						elif 19 <= self.key <= 25:
							self.key = self.key - 18
						ind = self.numbers.index(c)
						d_ind = ind - self.key 
						if d_ind < 0:
							d_ind = (ind - self.key) + 10
						d_c = self.numbers[d_ind]
						conc_list.append(d_c)
					else:
						d_c = c 
						conc_list.append(d_c)
				s = ''.join(conc_list)
				w_file.write(s)
				if sentence.index(word) != len(sentence)-1:
					w_file.write(" ")
		w_file.close()





