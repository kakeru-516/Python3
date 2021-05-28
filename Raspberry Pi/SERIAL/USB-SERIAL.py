import serial
import sys

ser = serial.Serial('/dev/ttyACM0', 115200)
print("OK")
while(1):
  try:
    val = input()
    ser.write(val.encode())
    val = (ser.readline()).decode()
    print(val)
  except KeyboardInterrupt:
    ser.close()
    sys.exit
