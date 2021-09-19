import json as simplejson
   
# import only system from os 
from os import system, name
# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#clearing interpriter console
sleep(0.1)
clear()

# license agreement
print (" ")
print (" ")
print (" ")
print ("	      ██╗     ███████╗ ██████╗  █████╗ ██╗         ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗     ")
print ("	      ██║     ██╔════╝██╔════╝ ██╔══██╗██║         ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗    ")
print ("	      ██║     █████╗  ██║  ███╗███████║██║         ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝    ")
print ("	      ██║     ██╔══╝  ██║   ██║██╔══██║██║         ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗    ")
print ("	      ███████╗███████╗╚██████╔╝██║  ██║███████╗    ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║    ")
print ("	      ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    ")
print (" ")
print ("												Ge+Ni Wordlist Generator - 2019 ")
print (" ")
print (" ")
print (" ")
print ("    The program you are using or you are about to use is designed to make combinations/lists of words/passwords/key-codes.  Whatever the task you are/will use it for is none of developers buissness and could possibly be illegal.  But the developper of this program (Ge+Ni), did not create it to cause someone/ some organization any kind of physical/mental/emotional/financial impact or harm.   Ge+Ni is designed to use to check vulnerabilities of your own passwords/key-codes.  Usage of this program to attack targets/ crack targets' passwords without prior mutual consent is illegal. It is end-user's responsibility to obal all kinds of applicable laws if any damages caused by usage of this program (Ge+Ni).  Developpers of this program will not take ant responsobility for any kinds of damage caused by this program.")
print (" ")
print (" ")
print ("            Do you understand and wish to continue? (y/n)")
ts=str(input("                 >   "))
if ts=="y" or ts=="Y":

	#clearing console
	sleep(0.1)
	clear()

	#Ge+Ni is a custom wordlist/ passwords list generator and a key/ code generator.
	#title
	print (" ")
	print (" ")                                                                                         
	print ("                      GGGGGGGGGGGGG                                          NNNNNNNN        NNNNNNNN   iiii  ")
	print ("                   GGG::::::::::::G                                          N:::::::N       N::::::N  i::::i ")
	print ("                 GG:::::::::::::::G                                          N::::::::N      N::::::N   iiii  ")
	print ("                G:::::GGGGGGGG::::G                            +++++++       N:::::::::N     N::::::N         ")
	print ("               G:::::G       GGGGGG     eeeeeeeeeeee           +:::::+       N::::::::::N    N::::::N iiiiiii ")
	print ("              G:::::G                 ee::::::::::::ee         +:::::+       N:::::::::::N   N::::::N i:::::i ")
	print ("              G:::::G                e::::::eeeee:::::ee +++++++:::::+++++++ N:::::::N::::N  N::::::N  i::::i ")
	print ("              G:::::G    GGGGGGGGGG e::::::e     e:::::e +:::::::::::::::::+ N::::::N N::::N N::::::N  i::::i ")
	print ("              G:::::G    G::::::::G e:::::::eeeee::::::e +:::::::::::::::::+ N::::::N  N::::N:::::::N  i::::i ")
	print ("              G:::::G    GGGGG::::G e:::::::::::::::::e  +++++++:::::+++++++ N::::::N   N:::::::::::N  i::::i ")
	print ("              G:::::G        G::::G e::::::eeeeeeeeeee         +:::::+       N::::::N    N::::::::::N  i::::i ")
	print ("               G:::::G       G::::G e:::::::e                  +:::::+       N::::::N     N:::::::::N  i::::i ")
	print ("                G:::::GGGGGGGG::::G e::::::::e                 +++++++       N::::::N      N::::::::N i::::::i")
	print ("                 GG:::::::::::::::G  e::::::::eeeeeeee                       N::::::N       N:::::::N i::::::i")
	print ("                   GGG::::::GGG:::G   ee:::::::::::::e                       N::::::N        N::::::N i::::::i")
	print ("                      GGGGGG   GGGG     eeeeeeeeeeeeee                       NNNNNNNN         NNNNNNN iiiiiiii")
	print (" ")
	print ("                                                                                         ██╗   ██╗     ██╗   ██╗  ██╗ ")
	print ("         Ge+Ni - Custom Wordlist Generator                                               ██║   ██║    ███║   ██║  ██║ ")
	print ("         By                                                                              ██║   ██║    ╚██║   ███████║ ")
	print ("         Dilshan Karunarathne @ team-achelous                                            ╚██╗ ██╔╝     ██║   ╚════██║ ")
	print ("         dilshan.karunarathn@gmail.com                                                    ╚████╔╝      ██║██╗     ██║ ")
	print ("         https://github.com/acheloios/Ge-Ni                                                ╚═══╝       ╚═╝╚═╝     ╚═╝ ")
	print (" ")
	print (" ")

	#Main menu 
	print ("                                 1 - Ge+Ni Wordlist/Passwords Generator")
	print ("                                 2 - How to use Ge+Ni")
	print ("                                 3 - Terms of service")
	print ("                                 4 - About us")
	print ("                                 5 - Donate us")
	print ("                                 6 - Report bug / feedback")
	print ("                                 0 - Exit Ge+Ni")
	print (" ")
	xx=int(input("    >   "))

	#clearing interpriter console
	sleep(0.1)
	clear() 

	#launch geni
	if xx==1:
		# type select
		print (" ")
		print (" ")
		print (" ")
		print ("       .d8888. d88888b db      d88888b  .o88b. d888888b      db      d888888b .d8888. d888888b      d888888b db    db d8888b. d88888b ")
		print ("       88'  YP 88'     88      88'     d8P  Y8 `~~88~~'      88        `88'   88'  YP `~~88~~'      `~~88~~' `8b  d8' 88  `8D 88'     ")
		print ("       `8bo.   88ooooo 88      88ooooo 8P         88         88         88    `8bo.      88            88     `8bd8'  88oodD' 88ooooo ")
		print ("         `Y8b. 88~~~~~ 88      88~~~~~ 8b         88         88         88      `Y8b.    88            88       88    88~~~   88~~~~~ ")
		print ("       db   8D 88.     88booo. 88.     Y8b  d8    88         88booo.   .88.   db   8D    88            88       88    88      88.     ")
		print ("       `8888Y' Y88888P Y88888P Y88888P  `Y88P'    YP         Y88888P Y888888P `8888Y'    YP            YP       YP    88      Y88888P ")
		print (" ")                                                                                                                           
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print ("                     1 - Personal passwords list ")
		print ("                         This type is based on a person's details and interests. ")
		print ("                         DEFAULT")
		print (" ")
		print ("                     2 - Key Generator")
		print ("                         This will allow you to generate codes using letters/numbers/symbols.")
		print ("                         Depend on how many characters should be in the words.")
		print ("                         Little annyoing when there is too much characters.")
		print (" ")
		print ("                     3 - Personal passwords Generator - Wizard Mode")
		print ("                         This asks your option on every step and makes you a personal wordlist.")
		print (" ")
		print (" ")
		print (" ")
		print ("         So.....")
		print ("         What type of wordlist you want to create? ")
		print (" ")
		o0=int(input("         >   "))
		print (" ")
		print (" ")

		#clearing console
		sleep(0.1)
		clear ()

		if o0==1:

			#default mode
			print (" ")
			print (" ")
			print (" ")
			print ("       I8,        8        ,8I                                  88  88  88                            ,ad8888ba,                            ")
			print ("       `8b       d8b       d8'                                  88  88  \"\"               ,d          d8\"'    `\"8b                           ")
			print ("        \"8,     ,8\"8,     ,8\"                                   88  88                   88         d8'                                     ")
			print ("         Y8     8P Y8     8P   ,adPPYba,   8b,dPPYba,   ,adPPYb,88  88  88  ,adPPYba,  MM88MMM      88              ,adPPYba,  8b,dPPYba,   ")
			print ("         `8b   d8' `8b   d8'  a8\"     \"8a  88P'   \"Y8  a8\"    `Y88  88  88  I8[    \"\"    88         88      88888  a8P_____88  88P'   `\"8a  ")
			print ("          `8a a8'   `8a a8'   8b       d8  88          8b       88  88  88   `\"Y8ba,     88         Y8,        88  8PP\"\"\"\"\"\"\"  88       88  ")
			print ("           `8a8'     `8a8'    \"8a,   ,a8\"  88          \"8a,   ,d88  88  88  aa    ]8I    88,         Y8a.    .a88  \"8b,   ,aa  88       88  ")
			print ("            `8'       `8'      `\"YbbdP\"'   88           `\"8bbdP\"Y8  88  88  `\"YbbdP\"'    \"Y888        `\"Y88888P\"    `\"Ybbd8\"'  88       88  ")
			print (" ")
			print (" ")
			print (" ")

			oo=1
			# lists
			#data list
			a=['master','fuck','huner','my','hello','sex','sexy','secret','princess','love','password']
			#final list
			fi=['password','123456789','987654321']
			#prifixes list
			pf=['123','abc','ABC','Abc','qwerty','1111','1234','12345','123456','0123','#']
			#suffixes list
			sf=['','.net','.com','.me','@gmail.com','rock','rox','.lk']
			#breakings list
			br=['','.',',','@','$','!','&','*','+','/']
			print (" ")
			print (" ")
			#input area

			print ("                Make sure the names you enter are all lowercase.")
			print (" ")
			#Names
			n1=str(input("                Enter his/her first name  : "))
			a.append(n1)

			n2=str(input("                Enter his/her middle name : "))
			a.append(n2)
					
			n3=str(input("                Enter his/her last name   : "))
			a.append(n3)
							
			n4=str(input("                Enter his/her nick name   : "))
			a.append(n4)
			print (" ")
			#other names
			q=""
			print ("                (If there no any other names, just type 0)")
			while q!="0":
				q=str(input("                Is there any other signeficant names? :"))
				a.append(q)
				if q=="0":
					del a[-1]
			print (" ")

			#birth year calculation crisis
			by=str(input("                Enter His/Her Birth YEAR  : "))
			a.append(by)
			byc=len(by)
			if byc==4:
				bx=by[2:4]
				a.append(bx)
			elif byc>=5 or byc<=1:
				print (" ")
				print ("                 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|    Awww......!    |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| ")
				print ("                 You must've made a mistake while typing birth year. ")
				print ("                 Birth year that you have entered is seems to be incorrect. ")
				print ("                 If it's not correct, we can't assure you about the results of this custom wordlist.")
				print ("                 To make this more efficient, please double check the data you enter.")
				print ("  ")
				e=str(input("                Enter 0 to rollback.  : "))
				if e=="0":
					del a[-1]
					by=str(input("                Enter His/Her Birth YEAR  : "))
					a.append(by)
					byc=len(by)
					if byc==4:
						bx=by[2:4]
						a.append(bx)
				else :
					print ("                 Unexpected answer..!")
			
			#birth month
			bm=str(input("                Enter His/Her Birth MONTH : "))
			a.append(bm)
			#birth date
			bd=str(input("                Enter His/Her Birth DATE  : "))
			a.append(bd)
			print (" ")
			
			# phone number
			print ("                Enter His/Her Mobile Phone Numbers (with 10 numbers eg: 0714567890).")
			print ("                If you don't know another mobile phone number, just enter 0")
			pn="1"
			while pn!="0":
				pn=str(input("                Enter A Mobile Phone Number   : "))
				pc=len(pn)
				if pc==10:
					ph=pn[-3]+pn[-2]+pn[-1]
					pnn=(pn[1:])
					fi.append(pnn)
					a.append(ph)
					fi.append(pn)
				elif pc==9:
					ph=pn[-3]+pn[-2]+pn[-1]
					a.append(ph)
					fi.append(pn)
				elif pc==12:
					ph=pn[-3]+pn[-2]+pn[-1]
					pn=pn.replace("+94", "0")
					pnn=(pn[1:])
					fi.append(pnn)
					a.append(ph)
					fi.append(pn)
				elif pc==1:
					pn==0
				else:
					print ( "                There must've been an error while you enter mobile phone number.")
					print ( "                Check the number again and re enter it.")
			print (" ")
			
			# nic
			nic=str(input("                Enter His/Her NIC number (if you don't know it, just enter 0)  : "))
			if nic[-1]=="v":
				nic=nic.replace("v", "")
			elif nic[-1]=="V":
				nic=nic.replace("V", "")
			ic=str(nic)
			fi.append(ic)
			fi.append(nic)
			print (" ")

			# other words
			print ("                Is there any other words/phrases/numbers him/her is fond with?")
			print ("                Names of His/Her school or college. His/Her Exam index number.")
			print ("                Or passwords He/She used earlier according to your knowledge.")
			print ("                Or you think he/she would use it as or in his/her password?")
			print ("                If there are any enter them. If there are not, enter 0")
			print (" ")
			ot=1
			while ot!="0":
				ot=str(input("                Enter any other word/phrase/number  : "))
				a.append(ot)
				if len(ot)>3:
					fi.append(ot)
				elif ot=="0":
					del a[-1]
			print (" ")

			#clearing console
			sleep (0.1)
			clear()

			#calculation
			while oo!=0:
				o1=int(input("                How many words do you want to combine to get the password list (1/2/3)  : "))
				o2=str(input("                Do you want to use common suffixes? (y/n) :"))
				o3=str(input("                Do you want to use common prefixes? (y/n) :"))
				# one word
				if o1==1:
					if (o2[0]=="y" or o2[0]=="Y") and (o3[0]=="y" or o3=="Y"):
						for i in a:
							for u in pf:
								for v in sf:
									f=u+i+v
									fi.append(f)
					elif (o2[0]=="y" or o2[0]=="Y") and (o3[0]=="n" or o3=="N"):
						for i in a:
							for v in sf:
								f=i+v
								fi.append(f)
					elif (o2[0]=="n" or o2[0]=="N") and (o3[0]=="y" or o3=="Y"):
						for i in a:
							for u in pf:
								f=u+i
								fi.append(f)
					elif (o2[0]=="n" or o2[0]=="N") and (o3[0]=="n" or o3=="N"):
						for i in a:
							fi.append(i)
					print (" ")
					oo=0
				#two words
				elif o1==2:
					if (o2[0]=="y" or o2[0]=="Y") and (o3[0]=="y" or o3=="Y"):
						for i in a:
							for b in a:
								for u in pf:
									for v in sf:
										f=u+i+b+v
										fi.append(f)
					elif (o2[0]=="y" or o2[0]=="Y") and (o3[0]=="n" or o3=="N"):
						for i in a:
							for b in a:
								for v in sf:
									f=i+b+v
									fi.append(f)
					elif (o2[0]=="n" or o2[0]=="N") and (o3[0]=="y" or o3=="Y"):
						for i in a:
							for b in a:
								for u in pf:
									f=u+i+b
									fi.append(f)
					elif (o2[0]=="n" or o2[0]=="N") and (o3[0]=="n" or o3=="N"):
						for i in a:
							for b in a:
								f=i+b
								fi.append(f)
					print (" ")
					oo=0
				#three words	
				elif o1==3:
					for i in a:
						for b in a:
							for c in a:
								f=i+b+c
					if o2[0]=="y" or o2[0]=="Y":
						for v in sf:
							f=f+v
					print (" ")
					if o3[0]=="y" or o3[0]=="Y":
						for u in pf:
							f=u+f
					fi.append(f)
					print (" ")
					oo=0
				#four words
				elif o1==4:
					#combine four words
					for i in a:
						for b in a:
							for c in a:
								for d in a:
									f=i+b+c+d
					#adding suffixes
					if o2=="y" or o2=="Y":
						for v in sf:
							f=f+v
					if o3=="y" or o3=="Y":
						for u in pf:
							f=u+f
					fi.append(f)
					print (" ")
					oo=0
				else :
					print (" Unexpected answer..!")
					print (" ")

			# outputs
			#clearing console
			sleep(0.1)
			clear()

			c=len(a)
			print (" ")
			print (" ")
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
			print ("             |     Your Custom Wordlist Is Created     |           ")
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
			print (" ")
			print (" Data items are :  ")
			print (a)

			print (" ")
			print (" Item count : ", c)
			print (" ")
			print (" ")
		
		elif o0==2:
			#keygen

			print (" ")
			print (" ")
			print (" ")
			print ("        888    d8P                      .d8888b.                888                 .d8888b.           888b    888 d8b  ")
			print ("        888   d8P                      d88P  Y88b               888                d88P  Y88b          8888b   888 Y8P  ") 
			print ("        888  d8P                       888    888               888                888    888          88888b  888      ") 
			print ("        888d88K      .d88b.  888  888  888         .d88b.   .d88888  .d88b.        888         .d88b.  888Y88b 888 888  ") 
			print ("        8888888b    d8P  Y8b 888  888  888        d88''88b d88' 888 d8P  Y8b       888  88888 d8P  Y8b 888 Y88b888 888  ") 
			print ("        888  Y88b   88888888 888  888  888    888 888  888 888  888 88888888       888    888 88888888 888  Y88888 888  ") 
			print ("        888   Y88b  Y8b.     Y88b 888  Y88b  d88P Y88..88P Y88b 888 Y8b.           Y88b  d88P Y8b.     888   Y8888 888  ") 
			print ("        888    Y88b  'Y8888   'Y88888   'Y8888P'   'Y88P'  'Y88888  'Y8888         'Y8888P88  'Y8888   888    Y888 888  ") 
			print ("                                  888                                                                                   ") 
			print ("                             Y8b d88P                                                                                   ")     
			print ("                              'Y88P'                                                                                    ")  

			fi=[]
			# letter/number/symbol lists
			l=[]
			#lower case letters
			ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
			#number
			nu=['1','2','3','4','5','6','7','8','9','0']
			#most used symbols
			ms=['!','@','#','$','%','&']
			#lowly used symbols
			ls=['*','^','(',')','-','+','=',',','.','/',':',';','>','<','~']
			#upper case letters
			ul=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("                 How many characters should be in your wordlist? (3/4/5/6/7/8) ")
			o4=int(input("                    >   "))
			print (" ")
			print ("                 Do you want to add lower case letters? (y/n)")
			o5=str(input("                    >   "))
			print (" ")
			print ("                 Do you want to add upper case letters? (y/n)")
			o6=str(input("                    >   "))
			print (" ")
			print ("                 Do you want to add numbers? (y/n)")
			o7=str(input("                    >   "))
			print (" ")
			print ("                 Do you want to add common symbols? (y/n)")
			o8=str(input("                    >   "))
			print (" ")
			print ("                 Do you want to add not frequently used symbols? (y/n)")
			o9=str(input("                    >   "))
			print (" ")
			print (" ")
			#generating one character list
			if o5=="y" or o5=="Y":
				l=l+ll
			if o6=="y" or o6=="Y":
				l=l+ul
			if o7=="y" or o7=="Y":
				l=l+nu
			if o8=="y" or o8=="Y":
				l=l+ms
			if o9=="y" or o9=="Y":
				l=l+ls
			if o4==3:
				for i1 in l:
					for i2 in l:
						for i3 in l:
							f=i1+i2+i3
							fi.append(f)
			elif o4==4:
				for i1 in l:
					for i2 in l:
						for i3 in l:
							for i4 in l:
								f=i1+i2+i3+i4
								fi.append(f)
			elif o4==5:
				for i1 in l:
					for i2 in l:
						for i3 in l:
							for i4 in l:
								for i5 in l:
									f=i1+i2+i3+i4+i5
									fi.append(f)
			elif o5==6:
				for i1 in l:
					for i2 in l:
						for i3 in l:
							for i4 in l:
								for i5 in l:
									for i6 in l:
										f=i1+i2+i3+i4+i5+i6
										fi.append(f)
			elif o5==7:
				for i1 in l:
					for i2 in l:
						for i3 in l:
							for i4 in l:
								for i5 in l:
									for i6 in l:
										for i7 in l:
											f=i1+i2+i3+i4+i5+i6+i7
											fi.append(f)
			elif o5==8:
				for i1 in l:
					for i2 in l:
						for i3 in l:
							for i4 in l:
								for i5 in l:
									for i6 in l:
										for i7 in l:
											for i8 in l:
												f=i1+i2+i3+i4+i5+i6+i7+i8
												fi.append(f)

		#wizard mode
		elif o0==3:
			print ("   ")
			print ("   ")
			print ("   ")
			print ("                                 ,,                                   ,,                                       ,,           ")
			print ("         `7MMF'     A     `7MF'  db                                 `7MM      `7MMM.     ,MMF'               `7MM              ")
			print ("           `MA     ,MA     ,V                                         MM        MMMb    dPMM                   MM              ")
			print ("            VM:   ,VVM:   ,V   `7MM  M\"\"\"MMV  ,6\"Yb.  `7Mb,od8   ,M\"\"bMM        M YM   ,M MM   ,pW\"Wq.    ,M\"\"bMM   .gP\"Ya     ")
			print ("             MM.  M' MM.  M'     MM  '  AMV  8)   MM    MM' \"' ,AP    MM        M  Mb  M' MM  6W'   `Wb ,AP    MM  ,M'   Yb    ")
			print ("             `MM A'  `MM A'      MM    AMV    ,pm9MM    MM     8MI    MM        M  YM.P'  MM  8M     M8 8MI    MM  8M\"\"\"\"\"\"    ")
			print ("              :MM;    :MM;       MM   AMV  , 8M   MM    MM     `Mb    MM        M  `YM'   MM  YA.   ,A9 `Mb    MM  YM.    ,    ")
			print ("               VF      VF      .JMML.AMMmmmM `Moo9^Yo..JMML.    `Wbmd\"MML.    .JML. `'  .JMML. `Ybmd9'   `Wbmd\"MML. `Mbmmd'    ")
			print ("   ")
			print ("   ")

			# lists
			#data list
			a=['master','fuck','huner','my','hello','sex','sexy','secret','princess','love','password']
			#final list
			fi=['password','123456789','987654321']
			#prifixes list
			pf=['123','abc','ABC','Abc','qwerty','1111','1234','12345','123456','0123','#']
			#suffixes list
			sf=['','.net','.com','.me','@gmail.com','rock','rox','.lk']
			#breakings list
			br=['','.',',','@','$','!','&','*','+','/']
			print (" ")
			print (" ")
			#input area

			print ("                 Make sure the words you enter are all lowercase.")
			print (" ")

			#Names
			print("                 Enter his/her first name ")
			n1=str(input("                    >   "))
			a.append(n1)

			print("                 Enter his/her middle name ")
			n2=str(input("                    >   "))
			a.append(n2)
			
			print ("                 Enter his/her last name ")
			n3=str(input("                    >   "))
			a.append(n3)
			
			n4=""				
			n4=print ("                 Enter his/her nick name  ")
			while n4!="0":
				n4=str(input("                    >   "))
				a.append(n4)
				if n4=="0":
					del a[-1]
			print (" ")

			#other names
			q=""
			print ("                 Is there any other signeficant names? ")
			print ("                 If there no any other names, just type 0")
			while q!="0":
				q=str(input("                    >   "))
				a.append(q)
				if q=="0":
					del a[-1]
			print (" ")

			#birth year calculation crisis
			print ("                 Enter His/Her Birth YEAR ")
			by=str(input("                    >   "))
			a.append(by)
			byc=len(by)
			if byc==4:
				bx=by[2:4]
				a.append(bx)
			elif byc>=5 or byc<=1:
				print (" ")
				print ("                  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|     Aww.......!     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| ")
				print ("                  You must've made a mistake while typing birth year. ")
				print ("                  Birth year that you have entered is seems to be incorrect. ")
				print ("                  If it's not correct, we can't assure you about the results of this custom wordlist.")
				print ("                  To make this more efficient, please double check the data before you enter.")
				print ("                  Enter 0 to rollback.")
				print (" ")
				e=str(input("                    >   "))
				if e=="0":
					print ("                 Enter His/Her Birth YEAR  ")
					del a[-1]
					by=str(input("                    >   "))
					a.append(by)
					byc=len(by)
					if byc==4:
						bx=by[2:4]
						a.append(bx)
				else :
					print ("                  Unexpected answer..!")
			print (" ")

			#birth month
			print ("                 Enter His/Her Birth MONTH ")
			bm=str(input("                    >   "))
			a.append(bm)
			print (" ")

			#birth date
			print ("                 Enter His/Her Birth DATE ")
			bd=str(input("                    >   "))
			a.append(bd)
			print (" ")

			# phone number
			print ("                 Enter His/Her Mobile Phone Numbers (with 10 numbers eg: 0714567890).")
			print ("                 If you don't know another mobile phone number, just enter 0")
			pn="1"
			while pn!="0":
				print ("                 Enter A Mobile Phone Number")
				pn=str(input("                    >   "))
				pc=len(pn)
				if pc==10:
					ph=pn[-3]+pn[-2]+pn[-1]
					pnn=(pn[1:])
					fi.append(pnn)
					a.append(ph)
					fi.append(pn)
				elif pc==9:
					ph=pn[-3]+pn[-2]+pn[-1]
					a.append(ph)
					fi.append(pn)
				elif pc==12:
					ph=pn[-3]+pn[-2]+pn[-1]
					pn=pn.replace("+94", "0")
					pnn=(pn[1:])
					fi.append(pnn)
					a.append(ph)
					fi.append(pn)
				elif pc==1:
					pn==0
				else:
					print (                 "There must've been an error while you enter mobile phone number.")
					print (                 "Check the number again and re enter it.")
			print (" ")

			# nic
			print ("                 Enter His/Her NIC number (if you don't know it, just enter 0)   ")
			nic=str(input("                    >   "))
			if nic[-1]=="v":
				nic=nic.replace("v", "")
			elif nic[-1]=="V":
				nic=nic.replace("V", "")
			ic=str(nic)
			fi.append(ic)
			fi.append(nic)
			print (" ")

			# other words
			print ("                 Is there any other words/phrases/numbers him/her is fond with?")
			print ("                 Names of His/Her school or college. His/Her Exam index number.")
			print ("                 His/Her vehical number/ home town.")
			print ("                 Or passwords He/She used earlier according to your knowledge.")
			print ("                 Or you think he/she would use it as or in his/her password?")
			print ("                 If there are any enter them. If there are not, enter 0")
			print (" ")
			ot=1
			while ot!="0":
				ot=str(input("                    >   "))
				a.append(ot)
				if len(ot)>3:
					fi.append(ot)
				elif ot=="0":
					del a[-1]
			print (" ")
			print (" ")

			#clearing console
			sleep(0.1)
			clear()

			c=len(a)
			# combining words 
			#selecting advanceness
			print (" ")
			print ("                Now you need to choose how advanced wordlist you want.")
			print ("                That depends on how advanced his/her password would be.")
			print ("                Is he/she a pro-techie? Or a random guy? Or a muggle?")
			print ("                There are 6 types of wordlists this script could generate. Choose Wisely.")
			print (" ")
			print (" ")
			print ("                Level 1 - no any type of word combination")
			print ("                Level 2 - simple two words combined")
			print ("                Level 3 - common prefixes + two words + common suffixes")
			print ("                Level 4 - simple three words combination")
			print ("                Level 5 - common prefixes + three words combination + common suffixes")
			print ("                Level 6 - simple four words combination")
			print ("                Level 7 - common prefixes + four words combination + common suffixes")
			print ("                Level 8 - [DEFAULT] you can make a custom template - for highly advanced passwords")
			print ("                How advanced wordlist do you need ? (1/2/3/4/5/6) ")
			print (" ")
			lv=int(input("                   >   "))
			#level 1 - one word
			if lv==1:
				for hi in range (0,c):
					f=a[hi]
					fi.append(f)
			#level 2 - two words
			elif lv==2:
				for hi in range (0, c):
					for ih in range (0, c):
						f=a[hi]+a[ih]
						fi.append(f)
			#level 3 - two words
			elif lv==3:
				for hi in range (0, c):
					for ih in range (0, c):
						f=a[hi]+a[ih]
					for i in pf:
						f=i+f
						for u in sf:
							f=f+u
							fi.append(f)
			#level 4 - three words
			elif lv==4:
				for hi in range (0, c):
					for ih in range (0, c):
						for hh in range (0, c):
							gg=a[hi]+a[ih]+a[hh]
							fi.append(gg)
							go=a[hi]+a[ih]
							fi.append(go)
			#level 5 - three words
			elif lv==5:
				for hi in range (0, c):
					for ih in range (0, c):
						for hh in range (0, c):
							gg=a[hi]+a[ih]+a[hh]
							fi.append(gg)
							go=a[hi]+a[ih]
							fi.append(go)
							for u in sf:
								f1=gg+u
								f2=go+u
								fi.append(f1)
								fi.append(f2)
							for i in pf:
								gg=i+gg
								go=i+go
								fi.append(gg)
								fi.append(go)
								for u in sf:
									gg=gg+u
									go=go+u
									fi.append(gg)
									fi.append(go)
			#level 6 - four words
			elif lv==6:
				for hi in range (0, c):
					for ih in range (0, c):
						for hh in range (0, c):
							for ii in range (0, c):
								f=a[hi]+a[ih]+a[hh]+a[ii]
								fi.append(f)
								gg=a[hi]+a[ih]+a[hh]
								fi.append(gg)
								go=a[hi]+a[ih]
								fi.append(go)
			#level 7 - four words
			elif lv==7:
				for hi in range (0, c):
					for ih in range (0, c):
						for hh in range (0, c):
							for ii in range (0, c):
								f=a[hi]+a[ih]+a[hh]+a[ii]
								fi.append(f)
								gg=a[hi]+a[ih]+a[hh]
								fi.append(gg)
								go=a[hi]+a[ih]
								fi.append(go)
								for u in sf:
									f1=f+u
									fi.append(f1)
									f2=gg+u
									fi.append(f2)
									f3=go+u
									fi.append(f3)
								for i in pf:
									f=i+f
									gg=i+gg
									go=i+go
									fi.append(f)
									fi.append(gg)
									fi.append(go)
									for u in sf:
										f=f+u
										gg=gg+u
										go=go+u
										fi.append(f)
										fi.append(gg)
										fi.append(go)

			#clearing console
			sleep(0.1)
			clear()

			# outputs 
			c=len(a)
			print (" ")
			print (" ")
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
			print ("             |     Your Custom Wordlist Is Created     |           ")
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
			print (" ")
			print (" Data items are :  ")
			print (a)

			print (" ")
			print (" Item count : ", c)
			print (" ")
			print (" ")

		else :
			print (" Unexpected answer...!")




		#wordlist output
		print (" Do you want to see your custom wordlist?")
		print (" ")
		pp=str(input("    >   "))
		if pp=="y" or pp=="Y":
			#wordlist display
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
			print ("                   |   Here's Your Wordlist   |                    ")
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
			print (" ")

			# display final words
			for items in fi:
				print ("               |  ", items, "    ")

			print (" ")
			print ("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

		print (" ")
		print (" ")

		# export to a text
		print (" Do you want to export this wordlist to a file? (y/n) : ")
		e=str(input("    >  "))
		if e=="y" or e=="yes" or e=="Y" or e=="Yes" or e=="YES":
			f = open('custom_wordlist.txt', 'w')
			for items in fi:
				simplejson.dump(items, f)
			f.close()
			print (" ")
			print (" ")

		elif e=="n" or e=="no" or e=="N" or e=="NO":
			print (" ")
			print (" ")

		else :
			print (" ")
			print (" ")
			print ("Unexpected answer...!")
			print (" ")
			print (" ")
		print (" ")
		print (" ")


	elif xx==2:
		#how to use - instructions
		print ("Still in development")

	elif xx==3:
		#license
		print ("Still in development")

	elif xx==4:
		#about us
		print ("Still in development")

	elif xx==5:
		#donations
		print ("Still in development")

	elif xx==6:
		#bug report -feedback
		print ("Still in development")

	else :
		print ("Unexpected answer......")

#clearing interpriter console
sleep(0.1)
clear()
