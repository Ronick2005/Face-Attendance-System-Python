import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
from datetime import date
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import mysql.connector
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QApplication, QWidget, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import webbrowser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

"""class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)

        self.movie = QMovie("C:\\Users\\Ronick\\Desktop\\Python project development\\Project final\\loader.gif")
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)
        
        self.startAnimation()
        #timer.singleShot(3000, self.stopAnimation)
        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()"""

class Ui_Link(object):
    def setupUi(self, Link):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        Link.setObjectName("Link")
        Link.resize(1500, 800)
        Link.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(Link)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 50, 931, 81))
        font = QtGui.QFont()
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 270, 571, 84))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(790, 295, 400, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 530, 150, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.link)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 530, 150, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 20px; color:white;")
        self.label.setFont(QFont('Eras Bold ITC', 26))
        self.label_2.setFont(QFont('HP Simplified', 22))
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.lineEdit.setFont(QFont('HP Simplified', 13))
        self.lineEdit.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        Link.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Link)
        self.statusbar.setObjectName("statusbar")
        Link.setStatusBar(self.statusbar)

        self.retranslateUi(Link)
        QtCore.QMetaObject.connectSlotsByName(Link)
        #Link.showMaximized()

    def retranslateUi(self, Link):
        _translate = QtCore.QCoreApplication.translate
        Link.setWindowTitle(_translate("Link", "Link"))
        self.label.setText(_translate("Link", "Go to Meeting(Online)"))
        self.label_2.setText(_translate("Link", "Enter your meeting id"))
        self.pushButton.setText(_translate("Link", "Go"))
        self.pushButton_2.setText(_translate("Link", "Don\'t Go"))
    
    def link(self):
        meetid = self.lineEdit.text()
        weblink = "https://meet.google.com/" + str(meetid)
        webbrowser.open(weblink)

class Ui_user(object):
    def __init__(self, dat1, dat2, dat3, dat4):
        self.dat1 = dat1
        self.dat2 = dat2
        self.dat3 = dat3
        self.dat4 = dat4

    def window10(self):
        self.window10 = QtWidgets.QMainWindow()
        self.ui = Ui_Attendance()
        self.ui.setupUi(self.window10)
        self.window10.show()
    def window9(self):
        self.window9 = QtWidgets.QMainWindow()
        self.ui = Ui_Stureg()
        self.ui.setupUi(self.window9)
        self.window9.show()
    def window7(self):
        self.window7 = QtWidgets.QMainWindow()
        self.ui = Ui_Link()
        self.ui.setupUi(self.window7)
        self.window7.show()
    def setupUi(self, user):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        #user.resize(572, 359)
        user.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(user)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 50, 931, 81))
        font = QtGui.QFont()
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 250, 831, 52))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 350, 831, 52))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 450, 831, 52))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 550, 831, 52))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1000, 250, 831, 52))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1000, 350, 831, 52))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 450, 831, 52))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1000, 550, 831, 52))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 710, 205, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.window7)
        self.pushButton.setFont(QFont('Times', 15))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 710, 250, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.window9)
        self.pushButton_2.setFont(QFont('Times', 15))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1170, 710, 215, 54))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.window10)
        self.pushButton_3.setFont(QFont('Times', 15))
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_3.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        user.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(user)
        self.statusbar.setObjectName("statusbar")
        user.setStatusBar(self.statusbar)
        currentTime = datetime.datetime.now()
        currentTime.hour
        if currentTime.hour < 12:
            t = 'Good Morning'
        elif 12 <= currentTime.hour < 18:
            t = 'Good Afternoon'
        else:
            t = 'Good Evening'
        time = t + " User"
        self.label.setText(time)
        self.retranslateUi(user)
        QtCore.QMetaObject.connectSlotsByName(user)
        self.label.setFont(QFont('Eras Bold ITC', 26))
        self.label_2.setFont(QFont('HP Simplified', 22))
        self.label_3.setFont(QFont('HP Simplified', 22))
        self.label_4.setFont(QFont('HP Simplified', 22))
        self.label_5.setFont(QFont('HP Simplified', 22))
        self.label_6.setFont(QFont('HP Simplified', 22))
        self.label_7.setFont(QFont('HP Simplified', 22))
        self.label_8.setFont(QFont('HP Simplified', 22))
        self.label_9.setFont(QFont('HP Simplified', 22))
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.label_3.setStyleSheet("color:white;")
        self.label_4.setStyleSheet("color:white;")
        self.label_5.setStyleSheet("color:white;")
        self.label_6.setStyleSheet("color:white;")
        self.label_7.setStyleSheet("color:white;")
        self.label_8.setStyleSheet("color:white;")
        self.label_9.setStyleSheet("color:white;")
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.pushButton_3.setFont(QFont('HP Simplified', 15))
        user.showMaximized()

    def retranslateUi(self, user):
        _translate = QtCore.QCoreApplication.translate
        user.setWindowTitle(_translate("user", "User"))
        self.label_2.setText(_translate("user", "Your Name"))
        self.label_3.setText(_translate("user", "Your Email ID"))
        self.label_4.setText(_translate("user", "Your Class"))
        self.label_5.setText(_translate("user", "Your Subject"))
        self.label_6.setText(_translate("user", self.dat1))
        self.label_7.setText(_translate("user", self.dat2))
        self.label_8.setText(_translate("user", self.dat3))
        self.label_9.setText(_translate("user", self.dat4))
        self.pushButton.setText(_translate("user", "Go to GMeet"))
        self.pushButton_2.setText(_translate("user", "Add new Student"))
        self.pushButton_3.setText(_translate("user", "Attendance"))

class Ui_Mainreg2(object):
    def window8(self):
        self.window8 = QtWidgets.QMainWindow()
        self.ui = Ui_Stureg()
        self.ui.setupUi(self.window8)
        self.window8.show()
    def setupUi(self, Mainreg2):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        Mainreg2.setObjectName("Mainreg2")
        #Mainreg2.resize(650, 420)
        Mainreg2.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(Mainreg2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 50, 831, 61))
        font = QtGui.QFont()
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 200, 831, 52))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 300, 801, 50))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 400, 851, 50))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 500, 851, 50))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1060, 200, 400, 41))
        self.lineEdit.setObjectName("lineEdit")          
        self.lineEdit.setFont(font)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1060, 300, 400, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")          
        self.lineEdit_2.setFont(font)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1060, 400, 400, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")          
        self.lineEdit_3.setFont(font)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1060, 500, 400, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")           
        self.lineEdit_4.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 860, 115, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 860, 115, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 600, 821, 60))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 700, 401, 51))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1060, 600, 400, 41))
        self.comboBox.setObjectName("comboBox")            
        self.comboBox.setFont(font)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1060, 700, 400, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")          
        self.lineEdit_5.setFont(font)
        Mainreg2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mainreg2)
        self.statusbar.setObjectName("statusbar")
        Mainreg2.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.insert_data)
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.retranslateUi(Mainreg2)
        QtCore.QMetaObject.connectSlotsByName(Mainreg2)
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.label.setFont(QFont('HP Simplified', 22))
        self.label_2.setFont(QFont('Eras Bold ITC', 26))
        self.label_3.setFont(QFont('HP Simplified', 22))
        self.label_4.setFont(QFont('HP Simplified', 22))
        self.label_5.setFont(QFont('HP Simplified', 22))
        self.label_6.setFont(QFont('HP Simplified', 22))
        self.label_7.setFont(QFont('HP Simplified', 22))
        self.lineEdit.setFont(QFont('HP Simplified', 13))
        self.lineEdit_2.setFont(QFont('HP Simplified', 13))
        self.lineEdit_3.setFont(QFont('HP Simplified', 13))
        self.lineEdit_4.setFont(QFont('HP Simplified', 13))
        self.lineEdit_5.setFont(QFont('HP Simplified', 13))
        self.comboBox.setFont(QFont('HP Simplified', 13))
        self.lineEdit.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_2.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_3.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_4.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_5.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.comboBox.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.label_3.setStyleSheet("color:white;")
        self.label_4.setStyleSheet("color:white;")
        self.label_5.setStyleSheet("color:white;")
        self.label_6.setStyleSheet("color:white;")
        self.label_7.setStyleSheet("color:white;")
        Mainreg2.showMaximized()

    def retranslateUi(self, Mainreg2):
        _translate = QtCore.QCoreApplication.translate
        Mainreg2.setWindowTitle(_translate("Mainreg2", "Sign up"))
        self.label_2.setText(_translate("Mainreg2", "School Admin Registration"))
        self.label.setText(_translate("Mainreg2", "Enter your name"))
        self.label_3.setText(_translate("Mainreg2", "Your mail id"))
        self.label_4.setText(_translate("Mainreg2", "Username"))
        self.label_5.setText(_translate("Mainreg2", "Password"))
        self.pushButton.setText(_translate("Mainreg2", "OK"))
        self.pushButton_2.setText(_translate("Mainreg2", "Cancel"))
        self.label_6.setText(_translate("Mainreg2", "Select your grade"))
        self.label_7.setText(_translate("Mainreg2", "Subject"))
        self.comboBox.setItemText(0, _translate("Mainreg2", "LKG"))
        self.comboBox.setItemText(1, _translate("Mainreg2", "UKG"))
        self.comboBox.setItemText(2, _translate("Mainreg2", "Grade 1"))
        self.comboBox.setItemText(3, _translate("Mainreg2", "Grade 2"))
        self.comboBox.setItemText(4, _translate("Mainreg2", "Grade 3"))
        self.comboBox.setItemText(5, _translate("Mainreg2", "Grade 4"))
        self.comboBox.setItemText(6, _translate("Mainreg2", "Grade 5"))
        self.comboBox.setItemText(7, _translate("Mainreg2", "Grade 6"))
        self.comboBox.setItemText(8, _translate("Mainreg2", "Grade 7"))
        self.comboBox.setItemText(9, _translate("Mainreg2", "Grade 8"))
        self.comboBox.setItemText(10, _translate("Mainreg2", "Grade 9"))
        self.comboBox.setItemText(11, _translate("Mainreg2", "Grade 10"))
        self.comboBox.setItemText(12, _translate("Mainreg2", "Grade 11"))
        self.comboBox.setItemText(13, _translate("Mainreg2", "Grade 12"))

    
    def insert_data(self):
        #self.loading_screen = LoadingScreen()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        def check(email):
            if(re.match(regex, email)):
                print("")

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Incorrect Email Address")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    quit()
        try:
            mydb = mysql.connector.connect(host="192.168.68.100", user="root", password="sqlro0614", database="attendance")
            mycursor = mydb.cursor()

            Name = self.lineEdit.text()
            Email = self.lineEdit_2.text()
            check(Email)
            Username = self.lineEdit_3.text()
            Password = self.lineEdit_4.text()
            Class = self.comboBox.currentText()
            Subject = self.lineEdit_5.text()
            query = "INSERT INTO user(Name, Emailid, Username, Password, Class, Subject) VALUES(%s, %s, %s, %s, %s, %s)"
            value = (Name, Email, Username, Password, Class, Subject)
            mycursor.execute(query, value)
            mydb.commit()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Successfully Registered")
            msgBox.setWindowTitle("Successful")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.window8()
                Name = self.lineEdit.text()
                Email = self.lineEdit_2.text()
                Username = self.lineEdit_3.text()
                Password = self.lineEdit_4.text()
                Class = self.comboBox.currentText()
                Subject = self.lineEdit_5.text()
                sender_email = "mydoc.faceattendance@gmail.com"
                receiver_email = Email
                password = "mydocface_2021"

                message = MIMEMultipart("alternative")
                message["Subject"] = "Successful"
                message["From"] = sender_email
                message["To"] = receiver_email

                html = """\
                <html>
                <body>
                    <h2>Message from MyDOC</h2>
                    <h3>Hello User</h3>
                    <p>
                        Account created successfully for <u>{name}</u> {thumb}
                        <br>Thank you for registering with MyDOC @ Face Attendance System</br>
                        <br><br>Your details</br></br>
                        <br>Name: <i>{name}</i></br>
                        <br>Email: <i>{mail}</i></br>
                        <br>Username: <i>{usrname}</i></br>
                        <br>Grade: <i>{grade}</i></br>
                        <br>Subject: <i>{sub}</i></br>
                        <br><br>Hope you have good time ahead !</br></br>
                        <br><br>Regards from <i>Ronick Aakshath</i> developer of MyDOC @ Face Attendance System {wave}</br></br>
                    </p>
                </body>
                </html>
                """.format(name = Name, thumb = "\U0001F44D", wave = "\U0001F44B", mail = Email, usrname = Username, grade = Class, sub = Subject)

                part2 = MIMEText(html, "html")

                message.attach(part2)


                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )

                """from stureg import Ui_Stureg
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Stureg()
                self.ui.setupUi(self.window)
                self.window.show()"""
            elif returnValue == QMessageBox.Cancel:
                quit()
        except mysql.connector.Error:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("2003: Server Not Found")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                quit()

class Ui_Offreg(object):
    def window8(self):
        self.window8 = QtWidgets.QMainWindow()
        self.ui = Ui_Stureg()
        self.ui.setupUi(self.window8)
        self.window8.show()
    def window6(self):
        self.window6 = QtWidgets.QMainWindow()
        self.ui = Ui_Stureg()
        self.ui.setupUi(self.window6)
        self.window6.show()
    def setupUi(self, Offreg):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        Offreg.setObjectName("Offreg")
        #Offreg.resize(650, 420)
        Offreg.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(Offreg)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 50, 831, 61))
        font = QtGui.QFont()
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 200, 831, 52))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 300, 801, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 400, 851, 50))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 500, 851, 50))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 600, 821, 60))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1060, 200, 400, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1060, 300, 400, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1060, 400, 400, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1060, 500, 400, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 860, 115, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 860, 115, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.insert_data)
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1060, 605, 400, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        Offreg.setCentralWidget(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.statusbar = QtWidgets.QStatusBar(Offreg)
        self.statusbar.setObjectName("statusbar")
        Offreg.setStatusBar(self.statusbar)
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.label.setFont(QFont('Eras Bold ITC', 26))
        self.label_2.setFont(QFont('HP Simplified', 22))
        self.label_3.setFont(QFont('HP Simplified', 22))
        self.label_4.setFont(QFont('HP Simplified', 22))
        self.label_5.setFont(QFont('HP Simplified', 22))
        self.label_6.setFont(QFont('HP Simplified', 22))
        self.lineEdit.setFont(QFont('HP Simplified', 13))
        self.lineEdit_2.setFont(QFont('HP Simplified', 13))
        self.lineEdit_3.setFont(QFont('HP Simplified', 13))
        self.lineEdit_4.setFont(QFont('HP Simplified', 13))
        self.comboBox.setFont(QFont('HP Simplified', 13))
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.label_3.setStyleSheet("color:white;")
        self.label_4.setStyleSheet("color:white;")
        self.label_5.setStyleSheet("color:white;")
        self.label_6.setStyleSheet("color:white;")
        self.lineEdit.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_2.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_3.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.lineEdit_4.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.comboBox.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")


        self.retranslateUi(Offreg)
        QtCore.QMetaObject.connectSlotsByName(Offreg)
        Offreg.showMaximized()

    def retranslateUi(self, Offreg):
        _translate = QtCore.QCoreApplication.translate
        Offreg.setWindowTitle(_translate("Offreg", "Offreg"))
        self.label.setText(_translate("Offreg", "Office Admin Registration"))
        self.label_2.setText(_translate("Offreg", "Name of Admin"))
        self.label_3.setText(_translate("Offreg", "Username"))
        self.label_4.setText(_translate("Offreg", "Email ID"))
        self.label_5.setText(_translate("Offreg", "Password"))
        self.label_6.setText(_translate("Offreg", "Type of organisation"))
        self.pushButton.setText(_translate("Offreg", "OK"))
        self.pushButton_2.setText(_translate("Offreg", "Cancel"))
        self.comboBox.setItemText(0, _translate("Offreg", "IT Company"))
        self.comboBox.setItemText(1, _translate("Offreg", "Software Company"))
        self.comboBox.setItemText(2, _translate("Offreg", "Manufacturing"))
        self.comboBox.setItemText(3, _translate("Offreg", "Small Scale Business"))
        self.comboBox.setItemText(4, _translate("Offreg", "School/Tutorials(Offline classes)"))
        self.comboBox.setItemText(5, _translate("Offreg", "College(Offline classes)"))
        self.comboBox.setItemText(6, _translate("Offreg", "Any Company(not in list)"))

    def insert_data(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        def check(email):
            if(re.match(regex, email)):
                print("")

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Incorrect Email Address")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    quit()
        try:
            mydb = mysql.connector.connect(host="192.168.68.100", user="root", password="sqlro0614", database="attendance")
            mycursor = mydb.cursor()

            Name = self.lineEdit.text()
            Email = self.lineEdit_3.text()
            check(Email)
            Username = self.lineEdit_2.text()
            Password = self.lineEdit_4.text()
            Org = self.comboBox.currentText()
            query = "INSERT INTO user2(Name, Emailid, Username, Password, Organisation) VALUES(%s, %s, %s, %s, %s)"
            value = (Name, Email, Username, Password, Org)
            mycursor.execute(query, value)
            mydb.commit()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Successfully Registered")
            msgBox.setWindowTitle("Successful")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.window8()
                Name = self.lineEdit.text()
                Email = self.lineEdit_3.text()
                Username = self.lineEdit_2.text()
                Password = self.lineEdit_4.text()
                Org = self.comboBox.currentText()
                sender_email = "mydoc.faceattendance@gmail.com"
                receiver_email = Email
                password = "mydocface_2021"

                message = MIMEMultipart("alternative")
                message["Subject"] = "Successful"
                message["From"] = sender_email
                message["To"] = receiver_email

                html = """\
                <html>
                <body>
                    <h2>Message from MyDOC</h2>
                    <h3>Hello User</h3>
                    <p>
                        Account created successfully for <u>{name}</u> {thumb}
                        <br>Thank you for registering with MyDOC @ Face Attendance System</br>
                        <br><br>Your details</br></br>
                        <br>Name: <i>{name}</i></br>
                        <br>Email: <i>{mail}</i></br>
                        <br>Username: <i>{usrname}</i></br>
                        <br>Organisation: <i>{org}</i></br>
                        <br><br>Hope you have good time ahead !</br></br>
                        <br><br>Regards from <i>Ronick Aakshath</i> developer of MyDOC @ Face Attendance System {wave}</br></br>
                    </p>
                </body>
                </html>
                """.format(name = Name, thumb = "\U0001F44D", wave = "\U0001F44B", mail = Email, usrname = Username, org = Org)

                part2 = MIMEText(html, "html")

                message.attach(part2)


                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )

                """from stureg import Ui_Stureg
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Stureg()
                self.ui.setupUi(self.window)
                self.window.show()"""
            elif returnValue == QMessageBox.Cancel:
                quit()
        except mysql.connector.Error:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("2003: Server Not Found")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                quit()

class Ui_Dialog(object):
    def window2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Mainreg2()
        self.ui.setupUi(self.window)
        self.window.show()
    def window5(self):
        self.window5 = QtWidgets.QMainWindow()
        self.ui = Ui_Offreg()
        self.ui.setupUi(self.window5)
        self.window5.show()
    def setupUi(self, Dialog):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 500)
        Dialog.setWindowIcon(QtGui.QIcon(self.iconName))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 300, 700, 64))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.window5)
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 150, 700, 64))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.window2)
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 791, 70))
        font = QtGui.QFont()
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setFont(QFont('Eras Bold ITC', 22))
        self.pushButton.setFont(QFont('HP Simplified', 18))
        self.pushButton_2.setFont(QFont('HP Simplified', 18))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Organisation"))
        self.pushButton.setText(_translate("Dialog", "Office/Institutions(Offline)"))
        self.pushButton_2.setText(_translate("Dialog", "Eductional Institutions(Online Classes only)"))
        self.label.setText(_translate("Dialog", "What type of organisation?"))

class Ui_Stureg(object):
    def setupUi(self, Stureg):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        Stureg.setObjectName("Stureg")
        Stureg.resize(1500, 800)
        Stureg.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(Stureg)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 50, 731, 81))
        font = QtGui.QFont()
        #font.setPointSize(26)
        #self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 270, 571, 84))
        #font = QtGui.QFont()
        #font.setPointSize(22)
        #self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(760, 300, 400, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QFont('HP Simplified', 13))
        self.lineEdit.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        #font = self.lineEdit.font()
        #font.setPointSize(13)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 370, 571, 84))
        #font = QtGui.QFont()
        #font.setPointSize(22)
        #self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 400, 75, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open)
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 530, 150, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 530, 150, 54))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_3.setFont(QFont('HP Simplified', 15))
        Stureg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Stureg)
        self.statusbar.setObjectName("statusbar")
        Stureg.setStatusBar(self.statusbar)
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.pushButton_3.setFont(QFont('HP Simplified', 15))
        self.label.setFont(QFont('Eras Bold ITC', 26))
        self.label_2.setFont(QFont('HP Simplified', 22))
        self.label_3.setFont(QFont('HP Simplified', 22))
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.label_3.setStyleSheet("color:white;")

        self.retranslateUi(Stureg)
        QtCore.QMetaObject.connectSlotsByName(Stureg)

    def retranslateUi(self, Stureg):
        _translate = QtCore.QCoreApplication.translate
        Stureg.setWindowTitle(_translate("Stureg", "Face Registeration"))
        self.label.setText(_translate("Stureg", "Registering Student Faces"))
        self.label_2.setText(_translate("Stureg", "Enter their Name"))
        self.label_3.setText(_translate("Stureg", "Student\'s face"))
        self.pushButton.setText(_translate("Stureg", "Add"))
        self.pushButton_2.setText(_translate("Stureg", "OK"))
        self.pushButton_3.setText(_translate("Stureg", "Cancel"))

    def open(self):
        from tkinter import filedialog
        filename = self.lineEdit.text()
        filetype = (('JPG files', '*.jpg'), ('All files', '*.*'))
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        pth = str(desktop) + "\\Face Attendance\\Imgdata\\ImagesAttendance"
        imgfile = filedialog.asksaveasfilename(initialdir = pth, defaultextension = '.jpg', initialfile = filename, filetypes = filetype)

class Ui_Attendance(object):
    def setupUi(self, Attendance):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        Attendance.setObjectName("Attendance")
        Attendance.resize(1500, 800)
        Attendance.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(Attendance)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(555, 50, 931, 81))
        font = QtGui.QFont()
        #font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 270, 571, 84))
        #font = QtGui.QFont()
        #font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(770, 295, 400, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        #font = self.lineEdit.font()
        #font.setPointSize(13)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 530, 250, 54))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.att)
        self.pushButton.setFont(QFont('HP Simplified', 15))
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        Attendance.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Attendance)
        self.statusbar.setObjectName("statusbar")
        Attendance.setStatusBar(self.statusbar)
        self.lineEdit.setFont(QFont('HP Simplified', 13))
        self.label.setFont(QFont('Eras Bold ITC', 26))
        self.label_2.setFont(QFont('HP Simplified', 22))
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.retranslateUi(Attendance)
        QtCore.QMetaObject.connectSlotsByName(Attendance)

    def retranslateUi(self, Attendance):
        _translate = QtCore.QCoreApplication.translate
        Attendance.setWindowTitle(_translate("Attendance", "Attendance"))
        self.label.setText(_translate("Attendance", "Attendance"))
        self.label_2.setText(_translate("Attendance", "Enter attendance file name"))
        self.pushButton.setText(_translate("Attendance", "Take Attendance"))
    
    def att(self):
        flname = self.lineEdit.text()
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        pth = str(desktop) + "\\Face Attendance\\Imgdata\\"
        flnm = str(flname) + str(date.today())
        fnm = flnm + ".csv"
        fln = pth + fnm
        fl = open(fln, 'w+')
        fl.writelines(f"Name, Time")
        fl.close()
        path = str(desktop) + "\\Face Attendance\\Imgdata\\ImagesAttendance"
        images = []
        classNames = []
        mylist = os.listdir(path)
        #print(mylist)
        for cl in mylist:
            curimg = cv2.imread(f'{path}/{cl}')
            images.append(curimg)
            classNames.append(os.path.splitext(cl)[0])
        #print(classNames)

        def findencod(images):
            encodelist = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodelist.append(encode)
            return encodelist

        def markattendance(name):
            from datetime import datetime
            from datetime import date
            today = date.today()
            with open(fln, 'r+') as f:
                mydatalist = f.readlines()
                namelist = []
                for line in mydatalist:
                    entry = line.split(',')
                    namelist.append(entry[0])
                if name not in namelist:
                    now = datetime.now()
                    dtstr = now.strftime('%I:%M:%S %p')
                    f.writelines(f'\n{name}, {dtstr}')
                
        encodelistknown = findencod(images)
        print("Encoding Complete")

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)
            imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

            faccurframe = face_recognition.face_locations(imgs)
            encodecurframe = face_recognition.face_encodings(imgs, faccurframe)

            for encodeface, facloc in zip(encodecurframe, faccurframe):
                matches = face_recognition.compare_faces(encodelistknown, encodeface)
                facedis = face_recognition.face_distance(encodelistknown, encodeface)
                #print(facedis)
                matchindex = np.argmin(facedis)

                if matches[matchindex]:
                    name = classNames[matchindex].capitalize()
                    #print(name)
                    y1, x2, y2, x1 = facloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markattendance(name)


            cv2.imshow("Capturing...(Press q to quit)", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

class Ui_MainWindow(object):
    def window3(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_user()
        self.ui.setupUi(self.window3)
        self.window3.show()
    def window4(self):
        self.window4 = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window4)
        self.window4.show()
    def setupUi(self, MainWindow):
        desktop = os.path.join(os.path.join(os.environ["ProgramFiles(x86)"]))
        pth = str(desktop) + "\\Face Attendance System\\fac2.ico"
        self.iconName = pth
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(600, 300)
        MainWindow.setWindowIcon(QtGui.QIcon(self.iconName))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 50, 931, 81))
        #self.label.setAlignment(QtCore.Qt.AlignRight)
        font = QtGui.QFont()
        self.label.setStyleSheet("color:white;")
        #font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 280, 721, 66))
        self.label_2.setStyleSheet("color:white;")
        #self.label_2.setAlignment(QtCore.Qt.AlignRight)
        #font = QtGui.QFont()
        #font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 430, 721, 66))
        self.label_3.setStyleSheet("color:white;")
        #self.label_3.setAlignment(QtCore.Qt.AlignRight)
        #font = QtGui.QFont()
        #font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1000, 300, 400, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        #font = self.lineEdit.font()
        #font.setPointSize(13)             
        self.lineEdit.setFont(font)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1000, 440, 400, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        #font = self.lineEdit_2.font()
        #font.setPointSize(13)             
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setStyleSheet("border-style: solid; border-color: rgb(102, 157, 246); border-radius : 5px; border-width: 3px; background-color : rgba(255,255,255,10%); color: white;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 710, 125, 54))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.setGeometry(200, 150, 150, 40)
        self.pushButton.setFont(QFont('HP Simplified', 16))
        self.pushButton.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 710, 145, 54))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        #self.pushButton_2.setGeometry(200, 150, 150, 40)
        self.pushButton_2.setFont(QFont('HP Simplified', 15))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1070, 710, 125, 54))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: rgb(27, 102, 202); border-radius : 25px; color:white;")
        #self.pushButton_3.setGeometry(200, 150, 150, 40)
        self.pushButton_3.setFont(QFont('HP Simplified', 16))
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.window4)
        self.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.showMaximized()
        self.label.setFont(QFont('Eras Bold ITC', 26))
        self.label_2.setFont(QFont('HP Simplified', 22))
        self.label_3.setFont(QFont('HP Simplified', 22))
        self.lineEdit.setFont(QFont('HP Simplified', 13))
        self.lineEdit_2.setFont(QFont('HP Simplified', 13))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Attendance System"))
        self.label.setText(_translate("MainWindow", "Face Attendance System"))
        self.label_2.setText(_translate("MainWindow", "Enter Username"))
        self.label_3.setText(_translate("MainWindow", "Enter Password"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.pushButton_2.setText(_translate("MainWindow", "New User"))
        self.pushButton_3.setText(_translate("MainWindow", "Cancel"))

    def login(self):
        #self.loading_screen = LoadingScreen()
        try:
            Username = self.lineEdit.text()
            Password = self.lineEdit_2.text()
            mydb = mysql.connector.connect(host="192.168.68.100", user="root", password="sqlro0614", database="attendance")
            mycursor = mydb.cursor()
            query = "SELECT * FROM user WHERE Username = %s and Password = %s"
            mycursor.execute(query, [(Username), (Password)])
            result = mycursor.fetchall()
            query2 = "SELECT * FROM user2 WHERE Username = %s and Password = %s"
            mycursor.execute(query2, [(Username), (Password)])
            result2 = mycursor.fetchall()
            if result:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Successfully Logged in")
                msgBox.setWindowTitle("Successful")
                msgBox.setStandardButtons(QMessageBox.Ok)

                for data in result:
                    self.window3 = QtWidgets.QMainWindow()
                    self.dat1 = data[0]
                    self.dat2 = data[1]
                    self.dat3 = data[4]
                    self.dat4 = data[5]
                    self.ui = Ui_user(self.dat1, self.dat2, self.dat3, self.dat4)
                    self.ui.setupUi(self.window3)
                    #print("Name:",data[0])
                    #print("Email ID:",data[1])
                    #print("Username:",data[2])
                    #print("Password:",data[3])
                    #print("Class:",data[4])
                    #print("Subject:",data[5])
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    self.window3.show()
            else:
                if result2:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("Successfully Logged in")
                    msgBox.setWindowTitle("Successful")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    for data in result2:
                        self.window3 = QtWidgets.QMainWindow()
                        self.dat1 = data[0]
                        self.dat2 = data[1]
                        self.dat3 = "NIL"
                        self.dat4 = data[4]
                        self.ui = Ui_user(self.dat1, self.dat2, self.dat3, self.dat4)
                        self.ui.setupUi(self.window3)
                        #print("Name:",data[0])
                        #print("Email ID:",data[2])
                        #print("Username:",data[1])
                        #print("Password:",data[3])
                        #print("Organisation:",data[4])
                    returnValue = msgBox.exec()
                    if returnValue == QMessageBox.Ok:
                        self.window3.show()

                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Incorrect Username or Password")
                    msgBox.setWindowTitle("Warning")
                    msgBox.setStandardButtons(QMessageBox.Ok)


                    returnValue = msgBox.exec()
                    if returnValue == QMessageBox.Ok:
                        quit()
                
        except mysql.connector.Error:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("2003: Server Not Found")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                quit()
stylesheet = """
    QMainWindow {
        background-image: url(C:/Program Files (x86)/Face Attendance System/background.png); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
            
if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(stylesheet) 
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()