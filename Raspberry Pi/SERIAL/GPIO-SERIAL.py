import serial

ser = serial.Serial('/dev/serial0', 115200)
print("OK")
while(1):
  val = input()
  ser.write(val.encode('utf-8'))
  val = (ser.readline()).decode('utf-8')
  print(val)

