import sys, hashlib

end = '\033[0m'
yellow = '\033[33m'
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
pur="\033[0;35m" 

def __start__():
	print
	print green+"[+] Please enter your hash sha384"
	print "    e.x: fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd"+end
	print
	hash = raw_input(brown+'sha384_decoding > hash >>> '+end)
	print
	print green+"[+] Please enter a password file"
	print "    e.x: pass.txt"+end
	print
	file = raw_input(brown+'sha384_decoding > file >>> '+end)
	try:
		fileO = open(file, 'r')
		word = fileO.readlines()
		fileO.close()
	except IOError:
		print
		print red+"[-] Not cant open password file: ",file,end
		print
		sys.exit()
	for password in word:
		password = password.strip()
		h = hashlib.sha384(password).hexdigest()
		if hash == h:
			print
			print green+"[+] Founded!"+end
			print
			print brown+" Hash: ",green,hash,end
			print brown+" Text: ",green,password,end
			print
			break
		else:
			print red+"Try: ",brown,password





