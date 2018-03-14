# Industrial-Laser-Interpreter
A script to establish RS-232 Serial communication between a Raspberry Pi 3 and an industrial laser device.

## Brief Summary
The machine sends commands to the interpreter. The interpreter reads these commands, massages them into a form that can be read by the Laser
before transmitting them to the laser. Similarly, the interpreter also receives commands and status updates from the laser, massages them into
a form that can be read by the machine before transmitting them to the machine. Communication between the interpreter and the machine/laser 
is done using RS-232. The program itself is running on a Raspberry Pi 3. It has been configured to execute at boot, without the need for any
external peripherals. The script - 'serial165.py' has been written entirely in Python. 
