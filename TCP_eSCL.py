import socket, time

DriveIP = "10.10.10.10"  # Drive IP can be configured

# header and end required for each eSCL message
header = bytes([0x00, 0x07])
end = bytes([0xD])

TCP_PORT = 7776

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish a TCP connection to the motor drive
sock.connect(('10.10.10.10', 7776))  # Match to your drive


# This function encodes the message attaches header and adds carriage return to
# the end. It also recieves the drive response and prints it.
def command(Message):
    encodeMessage = Message.encode()
    toSend = header + encodeMessage + end
    sock.send(toSend)
    recMessage = sock.recv(1024).decode()
    print(recMessage[2:])


# Drives should jog for 5 seconds in each direction
command('AX') # Reset Alarm
command('ME') # Enable Motor
command('DI1')
time.sleep(.1)
command('JS1')
time.sleep(.1)
command('CJ')
time.sleep(5)
command('SJ')
time.sleep(.1)
command('DI-1')
time.sleep(.1)
command('CJ')
time.sleep(5)
command('SJ')

# Close the socket when done
sock.close()
