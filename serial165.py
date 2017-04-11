##This is a serial interpreter script - used to establish communication
##between the DPSS Laser and the third party Machine

##Ver 1.57 (Final)

import serial, re, time  ##Import serial, string and time packages

ser = serial.Serial(port = '/dev/ttyUSB0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = None) # Define serial port for Machine
ser2 = serial.Serial(port = '/dev/ttyUSB1', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = None) # Define serial port for Laser


print("connected to: " + ser.portstr)
print("connected to: " + ser2.portstr)

count =1

while True:
	line = ser.read()                 ##Reads command from Machine
	time.sleep(0.02)              ##Waits 0.02s - to ensure command is received
	bytesToRead = ser.inWaiting()   ##Number of characters in queue to be read
	line += ser.read(bytesToRead)
	print (str(count) + str(': ') + line)   ##Prints to terminal what the script is receiving
	count = count+1


##Script 'interprets' the commands and forwards to laser/machine as per specifications

	if line == "?C1;" or line == "?c1;":
		ser2.write("?C1\r\n")
		line2 = ser2.readline()	##line2 = ser2.read(7)
##		if line2 != None and re.match('\d.\d\d\D\r\n', line2):
		line3 = line2.replace("\r\n",";")
		ser.write(line3)

	elif line == "?C1S;" or line == "?c1s;":
		ser2.write("?CS1\r\n")
		line2 = ser2.readline()	##line2 = ser2.read(7)
##		if line2 != None and re.match('\d.\d\d\D\r\n', line2):
		line3 = line2.replace("\r\n",";")
		ser.write(line3)

	elif line == "?G;" or line == "?g;":
		ser2.write("?G\r\n")
		line2 = ser2.readline()	##line2 = ser2.read(3)
		line3 = line2.replace("\r\n",";")
		ser.write(line3)

	elif line == "?Q;" or line == "?q;":
		ser2.write("?Q\r\n")
		line2 = ser2.readline()
		list1 = list(line2)
		list1.remove('\r')
		list1.remove('\n')
		list1[2] = '000'
		line2 = "".join(list1)
		line2 += ';'
		ser.write(line2)

	elif line == "?STB;" or line == "?stb;":
		ser.write("10.00A;")
##		ser.write('\r\n')

	elif line == "?SUP;" or line == "?sup;":
		ser.write("1;")
##		ser.write('\r\n')

	elif line == "?T1;" or line == "?t1;":
		ser2.write("?T4\r\n")
		line2 = ser2.readline()
		fline = line2.replace('\xb0', "")
		fline2 = fline.replace('\r\n',";")
		ser.write(fline2)

	elif line == "?T3;" or line == "?t3;":
		ser.write("2000;")
##		ser.write('\r\n')

	elif line == "?X61;" or line == "?x61;":
		ser2.write("?HOURS\r\n")
		line2 = ser2.readline()
		fline = line2.replace("\r\n",";")
		fline2 = fline.replace(" ","")
		fline3 = fline2.replace("o","")
		fline4  = fline3.replace("u","")
##		print fline4
		ser.write(fline4)

	elif line == "D0;" or line == "d0;":
		ser2.write("LASER=0\r\n")
		line2 = ser2.readline()	##line2 = ser2.read(4)
		if line2 == "OK\r\n":
			ser.write(";")

	elif line == "D1;" or line == "d1;":
		ser2.write("LASER=1\r\n")
		line2 = ser2.readline()  ##line2 = ser2.read(4)
		if line2 == "OK\r\n":
			ser.write(";")

	elif line != None and re.match('\D\d:\d\d\d\d;', line):
		ser.write(';')

	else:
		pass
		
ser.close()        ##Close port
