import sys

morse = {
	"A" : ".-",
	"B" : "-...",
	"C" : "-.-.",
	"D" : "-..",
	"E" : ".",
	"F" : "..-.",
	"G" : "--.",
	"H" : "....",
	"I" : "..",
	"J" : ".---",
	"K" : "-.-",
	"L" : ".-..",
	"M" : "--",
	"N" : "-.",
	"O" : "---",
	"P" : ".--.",
	"Q" : "--.-",
	"R" : ".-.",
	"S" : "...",
	"T" : "-",
	"U" : "..-",
	"V" : "...-",
	"W" : ".--",
	"X" : "-..-",
	"Y" : "-.--",
	"Z" : "--..",
	"0" : "-----",
	"1" : ".----",
	"2" : "..---",
	"3" : "...--",
	"4" : "....-",
	"5" : ".....",
	"6" : "-....",
	"7" : "--...",
	"8" : "---..",
	"9" : "----.",
	"." : ".-.-.-",
	"-" : "-....-"
}

def morse_transformation(character):
	if (character == ' '):
		ret = '/'
	else:
		if character in morse:
			ret = morse[character]
		else:
			print ("Error")
			sys.exit(1)
	return ret

def str_to_morse(str):
	str = str.upper()
	i = 0 
	str_to_print = ""
	# while str[i]: --> this does not work in python
	while i < len(str):
		str_to_print = str_to_print + morse_transformation(str[i])
		# if str[i + 1] != '\0': --> this does not work in python because strings do not end with a '\0'
		if i + 1 < len(str):
			str_to_print = str_to_print + ' '
		i = i + 1
	print(str_to_print)


if len(sys.argv) < 2:
	print("Wrong number fo arguments: minimum 3 expected")
	sys.exit(1)
else:
	str = ' '.join(sys.argv[1:])
	str_to_morse(str)
