Purple="\033[0;35m"
c = "\033[036m"
Green="\033[0;32m"

print("		{}##########################".format(Purple))
print("		#    Caesar Decryptor    #")
print("		#                        #")
print("		#                        #")
print("		#            By SO3HT3T  #")
print("		##########################\n")


words = input("{}Enter Your String :: {}".format(c,Green))
final = ""
for i in range(1,26):
	for word in words:
		if word.islower():
			rot = ord(word)+i
			if rot > 122:
				rot = rot - 26
			elif rot < 97:
				rot = rot + 26
			final += chr(rot)
		elif word.isupper():
			rot = ord(word)+i
			if rot > 90:
				rot = rot - 26
			elif rot < 65:
				rot = rot + 26
			final += chr(rot)
	print("ROT "+ str(i) + " :: "+final)
	final = ""

