# Created by: Trey Ball

from PyQt5 import QtWidgets, QtCore, QtGui
from BioBuddy import Ui_MainWindow
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from THP import read_bme280  # Assuming this function returns temperature, humidity, and pressure
import sys
from plants import Pansy, PeaceLily, Fern, Pothos
from moisture import read_moisture, setup_sensor
import RPi.GPIO as GPIO
import json    ### these two needed for notes
import os   ### /saving notes




class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        self.init_update_process()
        self.load_notes_from_file() # LOADS ANY NOTES SAVED AT START
        self.pansy = Pansy()
        self.peaceLily = PeaceLily()
        self.fern = Fern()
        self.pothos = Pothos()
        self.buttonFern.clicked.connect(lambda: self.display_plant(self.fern))      # THESE CONNECT BUTTONS TO PLANT CLASSES
        self.buttonPansy.clicked.connect(lambda: self.display_plant(self.pansy))
        self.buttonPeaceLily.clicked.connect(lambda: self.display_plant(self.peaceLily))
        self.buttonPothos.clicked.connect(lambda: self.display_plant(self.pothos))
        self.calendarWidget.selectionChanged.connect(self.calendar_date_changed)                                  #  CALANDAR BUTTONS
        self.saveNotesButton.clicked.connect(self.save_notes)
        for pin in [22, 23, 24, 25]:  # Pins for sensors 1 through 4
            GPIO.setup(pin, GPIO.IN)
        self.notesByDate = {}  # stores notes for calandar dates
        self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())     ## sets calandar to current date justa convenience and something cool i saw in qt5 docs
        self.init_plant_dropdowns() # inits the ID drop menus for plant-sensor correlation
        

        
#################################################################### CALANDAR AND NOTES FUNCS ###########################################################
    def calendar_date_changed(self):    ## this tracks if a new date is selected on the calandar to display current date and notes for that day
        selectedDate = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")  # Format date as string in correct format
        notes = self.notesByDate.get(selectedDate, "")  # get notes for the selected date
        self.notesTextEdit.setPlainText(notes)  # Update the text box with the retrieved notes
        selectedDate = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")    ## had to add these to show current selected date -
        self.selectedDateLabel.setText(f"Selected Date: {selectedDate}")         # since qt5 sucks and doesn't support this by default

    def save_notes(self):
        selectedDate = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")  # Format date as string in correct format
        notes = self.notesTextEdit.toPlainText()  # get the notes/text from the user input and store it as notes
        self.notesByDate[selectedDate] = notes  # Save or update the notes for the selected date
        self.save_notes_to_file()  # allows note to be saved as a file 

    def save_notes_to_file(self):
        with open('notes_data.json', 'w') as file:    # w means write
            json.dump(self.notesByDate, file)

    def load_notes_from_file(self):
        try:
            with open('notes_data.json', 'r') as file:    # r means read
                self.notesByDate = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.notesByDate = {}  # Init to an empty dictionary if no file found (i hate this error)





#############################################################  MOISTURE MONITOR #####################################################
    def read_moisture_sensor(self, pin):
        return GPIO.input(pin)

    def display_plant(self, plant):
        # Get plant details
        details = plant.get_details()
        self.current_max_temp = details['max_temp']   ## importing these to use set PB constraints
        self.current_max_humidity = details['max_humidity']  ####
        ######Update the UI labels######
        self.plantname_label.setText(details['name'])
        self.labelImage.setPixmap(QtGui.QPixmap(details['imagePath']))
        self.labelDescription.setText(details['description'])
        self.tempPB_MM.setText(f"   {details['min_temp']}°C - {details['max_temp']}°C  ")
        self.HumidPB_MM.setText(f"   {details['min_humidity']}% - {details['max_humidity']}%  ")

    def init_update_process(self):
        # timer to update sensor data
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_sensor_data)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

    def update_moisture_display(self, sensor_number):
        pin_mapping = {1: 22, 2: 23, 3: 24, 4: 25}    # Mapping sensor numbers to GPIO pins
        sensor_status = self.read_moisture_sensor(pin_mapping[sensor_number])
        image_path = "moist.png" if sensor_status == 0 else "unmoist.png"
        # Find the correct QLabel object based on sensor_number
        sensor_label = getattr(self, f'sensor{sensor_number}Mstatus')
        sensor_label.setPixmap(QtGui.QPixmap(image_path))   # sets image of init plant to its image
        # Get the frame object for the current sensor
        frame = getattr(self, f'frameMS{sensor_number}')
        # Determine the border color based on the sensor status
        border_color = "rgb(65, 212, 149)" if sensor_status == 0 else "red"  # 0 is moist, 1 is unmoist
        frame.setStyleSheet(f"""
            QFrame {{
            background-color: rgb(249, 253, 242);
            border: 2px solid {border_color};
            }}
        """)

    def update_sensor_data(self):
        # Read temperature and humidity from BME280
        temperature, humidity, pressure, = read_bme280()
        
        # Update temperature PB data
        self.update_temperature_progress(temperature)
        # Update humidity PB data
        self.update_humidity_progress(humidity)  
        # Updates pressure PB data
        self.update_pressure_progress(pressure)
        #update moisture sensors
        for sensor_number in range(1, 5):  #  sensors 1 to 4
            self.update_moisture_display(sensor_number)

    ########## DROP DOWN MENUS IN MM ##################################

    def init_plant_dropdowns(self):
        plant_names = ['Pansy', 'Peace Lily', 'Fern', 'Pothos']  # Plant names
        # scans the sensors
        for i in range(1, 5):
            comboBox = getattr(self, f'comboBoxSensor{i}')
            comboBox.addItems(plant_names)
            comboBox.currentIndexChanged.connect(lambda index, cb=comboBox: self.update_plant_label(cb))

    def update_plant_label(self, comboBox):
        # find sensor this comboBox corresponds to
        sensor_number = int(comboBox.objectName()[-1])  # comboxboxes named 1-4 so just uses range to chose instance of it
        selected_plant = comboBox.currentText()
        # Update corresponding label
        label = getattr(self, f'labelSensor{sensor_number}')
        label.setText(selected_plant)
            

    ################################################################## PROGRESS BARS ##################################################################

    def update_temperature_progress(self, temperature):
        max_temp = getattr(self, 'current_max_temp', 50)  # Use stored max or default
        temp_percent = (temperature / max_temp) * 100  # Convert to percentage
        color = "rgba(255, 0, 0, 255)" if temperature > max_temp else "rgba(85, 170, 255, 255)"  ## CHANGES PB to RED if max temp exceeded
        self.progressBarValue(min(temp_percent, 100), self.circularProgressTEMP, color)
        self.labelPercentage.setText(f"{temperature:.2f}°C")

    def update_humidity_progress(self, humidity):
        max_humidity = getattr(self, 'current_max_humidity', 60)  # again max or default
        humid_percent = (humidity / max_humidity) * 100
        color = "rgba(255, 0, 0, 255)" if humidity > max_humidity else "rgba(0, 255, 34, 255)"
        self.progressBarValue(min(humid_percent, 100), self.circularProgressHUMID, color)
        self.labelPercentage_2.setText(f"{humidity:.2f}%")

    def update_pressure_progress(self, pressure):
        max_pressure = 1080 
        pressure_percent = (pressure / max_pressure) * 100  # Convert to percentage
        self.progressBarValue(min(pressure_percent, 100), self.circularProgressPRES, "rgba(255, 184, 60, 255)")
        self.labelPercentage_3.setText(f"{pressure:.2f} hPa")

    def progressBarValue(self, value, progressBar, color):  ## manipulating gradiendts to give cirular PB effect
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        progress = value / 100
        stop_1 = str(1.0 - progress)
        stop_2 = str(1.0 - progress + 0.001 if progress > 0 else 0)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)
        progressBar.setStyleSheet(newStylesheet)

##################################################################################################################################################


# runs main UI, just some mombo jumbo required for QT5
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())