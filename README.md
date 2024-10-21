# Arduino Sensor Reader
This project reads data from an Arduino connected via a serial port, logs it, and exports the data to an Excel file (arduino_data.xlsx) using Python. It demonstrates how to interface with an Arduino using the pySerial library, process the data, and store it in a structured format like Excel for further analysis.
## Features
* Reads sensor or other data from the Arduino in real-time.
* 1000 data points with timestamps.
* Exports the collected data to an Excel file (arduino_data.xlsx).
* Easy-to-use Python script with configurable serial port settings.
## Requirements
* Python 3.x
* Arduino with sensor or data source
* pySerial Library : To communicate with the Arduino via serial
* xlsxwriter Library : To create and write to Excel files
## Setup and Usage
* Connect the Arduino: Ensure your Arduino is connected to your computer via USB, and upload the appropriate code to it so it sends data over the serial connection.

* Configure the Serial Port: Update the Python script with the correct COM port for your Arduino (in this case, COM3) and set the baud rate (9600 by default).
* Run the Python Script
* Output: The script will continuously read data from the Arduino and display it in the console. After collecting data, it will save it into an Excel file (arduino_data.xlsx) with columns for Actual and Measured values.
## Customization
* Adjust Data Points: The script is currently set to read 1003 data points. You can modify the loop to collect more or fewer data points as needed.
* Modify Actual Values: If you want to change the "Actual" column value from 30 to something else, you can easily update this part of the script.
