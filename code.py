import serial
import subprocess

serial_port = 'COM2'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        # Replace the path with the actual path to your script
        script_path = r"C:\Users\Shambhu J\Desktop\VIT\Embedded Systems\Project\Embedded Review\tab_change.ahk"
        subprocess.Popen(script_path, shell=True)
