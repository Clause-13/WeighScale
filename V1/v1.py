import serial

weighScalePort = serial.Serial(port = "COM100", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
scannerPort = serial.Serial(port = "COM200", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while(1):

    # Wait until there is data waiting in the serial buffer
    if(weighScalePort.in_waiting > 0):
        lo = 200
        high = 600
        weighScaleOutput = weighScalePort.readline().decode('Ascii')
        print(type(weighScaleOutput))
        try: 
            weighScaleInt= int(weighScaleOutput)
            if weighScaleInt >= 200 and weighScaleInt <= 600: 
                print("{}kg".format(weighScaleInt))
                if(scannerPort.in_waiting > 0):
                    scannerPortOutput = scannerPort.readline().decode('Ascii')
                    print(scannerPortOutput)
            elif weighScaleInt < 200:
                print("Your weight is {}kg which is too low!".format(weighScaleInt))
            elif weighScaleInt: 
                print("Your weight is {}kg which is too high!".format(weighScaleInt))
        except ValueError: 
            print("{} is not a number".format(weighScaleOutput))
        # print(weighScaleOutput)
        # print("Next output!")
        # if serialString > 
        # serialPort.write(b"Next! \r\n")


