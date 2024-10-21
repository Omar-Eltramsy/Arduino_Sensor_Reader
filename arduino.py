#!/usr/
import serial.tools.list_ports
import xlsxwriter
import time

serial_port = 'COM3'
baud_rate = 9600
serial_object = serial.Serial(serial_port, baud_rate)
data = []


for _ in range(1003):
    if serial_object.in_waiting:  # Check if data is available
        packet = serial_object.readline()
        val = packet.decode('utf-8').strip('\n').strip('\r') 
        data.append(val) 
        print(val)
    else:
        print("No data available at the moment")
    time.sleep(1)  

# Close the serial connection after use
serial_object.close()

# Create an Excel file and write data
workbook = xlsxwriter.Workbook('arduino_data.xlsx')  # Create a new Excel file
worksheet = workbook.add_worksheet()

# Write header
worksheet.write('A1', 'Actual')
worksheet.write('B1', 'Measured')

# Write data to the Excel file
for row_num, measured_value in enumerate(data, start=1):  # Start at row 1
    worksheet.write(row_num, 0, 50)  # Writing "Actual" value (assuming it's always 30)
    worksheet.write(row_num, 1, measured_value)  # Writing "Measured" value from serial

# Save and close the workbook
workbook.close()

print("Data has been successfully written to arduino_data.xlsx")
