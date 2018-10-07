import sys 
from string import ascii_lowercase 

alfabeto = ascii_lowercase * 26

if len(sys.argv) <= 4 or len(sys.argv) > 5:
	print("""-->> python vigenere.py '--encrypt' testando '--key' test <<--

--encrypt -->> codifica
--decrypt -->> decodifica
--key -->> chave""")


else:
	if sys.argv[1] == "--encrypt":
	
		def encrypt():
			cont1 = 0
			obj1 = 0 
			key = []

			while len(sys.argv[2]) != len(key):
				if cont1 != len(sys.argv[4]):
					key.append(sys.argv[4][cont1])
					cont1 += 1
					if cont1 == len(sys.argv[4]):
						cont1 = 0

			for enc in sys.argv[2].lower():
				Encr_Index = alfabeto.index(enc)
				Elemento = key[obj1].lower()
				Elem_List = alfabeto.index(Elemento)
				encriptado = Elem_List + Encr_Index
				print(alfabeto[encriptado], end="")
				obj1 += 1

		encrypt()

	elif sys.argv[1] == "--decrypt":

		def decrypt():
			cont1 = 0
			obj1 = 0
			key = []

			while len(sys.argv[2]) != len(key):
				if cont1 != len(sys.argv[4]):
					key.append(sys.argv[4][cont1])
					cont1 += 1
					if cont1 == len(sys.argv[4]):
						cont1 = 0

			for dec in sys.argv[2].lower():
				Decry_Index = alfabeto.index(dec)
				Element = key[obj1].lower()
				List_index = alfabeto.index(Element)
				decriptado = Decry_Index - List_index
				print(alfabeto[decriptado], end="")
				obj1 += 1
		
		decrypt()
