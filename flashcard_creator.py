import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
current_subject=None
display_card_data=[]
display_card_color=[]
order=[]
import os
def concat(lst):
    full_sep = '|;!!;|'
    text=''
    for i in lst:
        text+=i+full_sep
    return text
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,creat=False):
        if creat:
            all_file=os.listdir()
            file_name=self.nameofsubject.text()+'100120.txt'
            if file_name not in all_file:
                a=open(file_name,'w+')
                a.close()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.creatnewsubject = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.creatnewsubject.setGeometry(QtCore.QRect(260, 190, 222, 48))
        self.creatnewsubject.setObjectName("creatnewsubject")
        self.viewexistingsubject = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.viewexistingsubject.setGeometry(QtCore.QRect(260, 250, 222, 48))
        self.viewexistingsubject.setObjectName("viewexistingsubject")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.creatnewsubject.clicked.connect(lambda:self.new_subject())
        self.viewexistingsubject.clicked.connect(lambda:self.existing())
    def existing(self):
        global display_card_data
        global display_card_color
        global order
        display_card_data=[]
        display_card_color=[]
        order=[]
        allfiles=os.listdir()
        subjects=[]
        for i in allfiles:
            if i.endswith('100120.txt'):
                subjects.append(i)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.subject_exist = QtWidgets.QComboBox(self.centralwidget)
        self.subject_exist.setGeometry(QtCore.QRect(290, 130, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.subject_exist.setFont(font)
        self.subject_exist.setObjectName("subject_exist")
        for i in range(len(subjects)):
            self.subject_exist.addItem("")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(360, 210, 101, 41))
        self.go.setObjectName("go")
        self.back2 = QtWidgets.QPushButton(self.centralwidget)
        self.back2.setGeometry(QtCore.QRect(352, 270, 121, 41))
        self.back2.setObjectName("back2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.existing_retranslateUi(MainWindow,subjects)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.back2.clicked.connect(lambda:self.setupUi(MainWindow))
        self.go.clicked.connect(lambda:self.see_flashcard())
    def see_flashcard(self,forward=True,show_next=False):
        global current_subject
        global order
        global display_card_data
        global display_card_color
        if  forward or len(order)==0:############if forward
            color_sep = '|:!!:|'
            full_sep = '|;!!;|'
            if forward:
                target_file=open(self.subject_exist.currentText()+'100120.txt','r')
            else:
                target_file = open(current_subject + '100120.txt', 'r')
            all_data_str=target_file.read()
            all_data=all_data_str.split(full_sep)
            text_data=[]
            color_data=[]
            for i in all_data:
                j=i.split(color_sep)
                if len(j)==2:
                    text_data.append(j[0])
                    color_data.append(j[1])
            if len(text_data)==0:
                text_data=['No Flashcard to show\n press add flashcard to creat one']
                color_data=['white']
            display_card_color=color_data
            display_card_data=text_data
            order = list(range(len(display_card_data)))
            random.shuffle(order)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addflashcard = QtWidgets.QPushButton(self.centralwidget)
        self.addflashcard.setGeometry(QtCore.QRect(320, 480, 151, 41))
        self.addflashcard.setObjectName("addflashcard")
        self.flashcard_display = QtWidgets.QLabel(self.centralwidget)
        self.flashcard_display.setGeometry(QtCore.QRect(160, 100, 471, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flashcard_display.setFont(font)
        self.flashcard_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        if show_next:
            if display_card_color[order[0]].lower()=='white':
                self.flashcard_display.setStyleSheet("background-color: rgb(250, 250, 250);")
            elif display_card_color[order[0]].lower()=='red':
                self.flashcard_display.setStyleSheet("background-color: rgb(250, 0, 0);")
            elif display_card_color[order[0]].lower()=='blue':
                self.flashcard_display.setStyleSheet("background-color: rgb(0, 0, 250);")
            else:
                self.flashcard_display.setStyleSheet("background-color: rgb(0, 250, 0);")
        else:
            self.flashcard_display.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.flashcard_display.setScaledContents(False)
        self.flashcard_display.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.flashcard_display.setWordWrap(False)
        self.flashcard_display.setObjectName("flashcard_display")
        self.show_next_card = QtWidgets.QPushButton(self.centralwidget)
        self.show_next_card.setGeometry(QtCore.QRect(320, 430, 151, 41))
        self.show_next_card.setObjectName("show_next_card")
        self.subject_name = QtWidgets.QLabel(self.centralwidget)
        self.subject_name.setGeometry(QtCore.QRect(164, 10, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.subject_name.setFont(font)
        self.subject_name.setObjectName("subject_name")
        self.back3 = QtWidgets.QPushButton(self.centralwidget)
        self.back3.setGeometry(QtCore.QRect(10, 0, 121, 41))
        self.back3.setObjectName("back3")##
        self.delete_card = QtWidgets.QPushButton(self.centralwidget)
        self.delete_card.setGeometry(QtCore.QRect(670, 0, 121, 41))
        self.delete_card.setObjectName("delete_card")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.see_flashcard_retranslateUi(MainWindow,forward,show_next)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addflashcard.clicked.connect(lambda:self.creatflashcard())
        self.back3.clicked.connect(lambda:self.existing())
        self.show_next_card.clicked.connect(lambda:self.see_flashcard(forward=False,show_next=True))
        self.delete_card.clicked.connect(lambda:self.delete_flash())
    def delete_flash(self,have_to_delete=False):
        global current_subject
        full_sep = '|;!!;|'
        target_file = open(current_subject + '100120.txt', 'r')
        all_data_str=target_file.read()
        text_with_col=all_data_str.split(full_sep)
        if have_to_delete:
            inx=self.all_flash_cards_to_delete.currentIndex()
            text_with_col.pop(inx)
            text=concat(text_with_col)
            file=open(current_subject+'100120.txt','w')
            file.write(text)
            file.close()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.all_flash_cards_to_delete = QtWidgets.QComboBox(self.centralwidget)
        self.all_flash_cards_to_delete.setGeometry(QtCore.QRect(270, 170, 251, 31))
        self.all_flash_cards_to_delete.setObjectName("all_flash_cards_to_delete")
        for i in range(len(text_with_col)):
            self.all_flash_cards_to_delete.addItem("")
        self.back5 = QtWidgets.QPushButton(self.centralwidget)
        self.back5.setGeometry(QtCore.QRect(350, 250, 93, 28))
        self.back5.setObjectName("back5")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(350, 210, 93, 28))
        self.delete_button.setObjectName("delete_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.delete_flash_retranslateUi(MainWindow,text_with_col)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.delete_button.clicked.connect(lambda:self.delete_flash(True))
        self.back5.clicked.connect(lambda: self.see_flashcard(False))
    def creatflashcard(self,have_to_creat=False):
        global current_subject
        if have_to_creat:
            if self.flashcard_text.toPlainText().count('\n')+1>15:
                msg=QMessageBox()
                msg.setWindowTitle('Number of lines exceed the limit')
                msg.setText("you can write maximum of 15 lines")
                msg.setIcon(QMessageBox.Critical)
                x=msg.exec_()
            else:
                color_sep='|:!!:|'
                full_sep='|;!!;|'
                file_to_write_in=current_subject+'100120.txt'
                file=open(file_to_write_in,'r')
                past=file.read()
                file.close()
                text=self.flashcard_text.toPlainText()
                text_col=self.bg_color.currentText()
                text=text+color_sep+text_col+full_sep
                file=open(file_to_write_in,'w')
                wri=past+text
                file.write(wri)
                file.close()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flashcard_text = QtWidgets.QTextEdit(self.centralwidget)
        self.flashcard_text.setGeometry(QtCore.QRect(240, 150, 361, 221))
        self.flashcard_text.setObjectName("flashcard_text")
        self.bg_color = QtWidgets.QComboBox(self.centralwidget)
        self.bg_color.setGeometry(QtCore.QRect(330, 390, 171, 31))
        self.bg_color.setObjectName("bg_color")
        self.bg_color.addItem("")
        self.bg_color.addItem("")
        self.bg_color.addItem("")
        self.bg_color.addItem("")
        self.creat_the_flashcard = QtWidgets.QPushButton(self.centralwidget)
        self.creat_the_flashcard.setGeometry(QtCore.QRect(360, 430, 121, 41))
        self.creat_the_flashcard.setObjectName("creat_the_flashcard")
        self.back4 = QtWidgets.QPushButton(self.centralwidget)
        self.back4.setGeometry(QtCore.QRect(360, 480, 121, 41))
        self.back4.setObjectName("back4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.creatflashcardretranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.creat_the_flashcard.clicked.connect(lambda:self.creatflashcard(True))
        self.back4.clicked.connect(lambda:self.see_flashcard(False))
    def new_subject(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameofsubject = QtWidgets.QLineEdit(self.centralwidget)
        self.nameofsubject.setGeometry(QtCore.QRect(270, 170, 261, 41))
        self.nameofsubject.setObjectName("nameofsubject")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 170, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.creatsubject = QtWidgets.QPushButton(self.centralwidget)
        self.creatsubject.setGeometry(QtCore.QRect(340, 260, 121, 51))
        self.creatsubject.setObjectName("creatsubject")
        self.back1 = QtWidgets.QPushButton(self.centralwidget)
        self.back1.setGeometry(QtCore.QRect(340, 320, 121, 51))
        self.back1.setObjectName("back1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.new_subject_retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.creatsubject.clicked.connect(lambda:self.setupUi(MainWindow,True))
        self.back1.clicked.connect(lambda:self.setupUi(MainWindow))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.creatnewsubject.setText(_translate("MainWindow", "Create New Subject"))
        self.viewexistingsubject.setText(_translate("MainWindow", "View Existing Subject Note"))

    def see_flashcard_retranslateUi(self, MainWindow,forward=True,show_next=False):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addflashcard.setText(_translate("MainWindow", "Add Flashcard"))
        if show_next:
            global display_card_data
            global order
            if len(order)!=0:
                self.flashcard_display.setText(_translate("MainWindow", display_card_data[order[0]]))
                order=order[1:]
            else:
                self.flashcard_display.setText(_translate("MainWindow", "Press next to start again"))
        else:
            self.flashcard_display.setText(_translate("MainWindow", "Press next to start"))
        self.show_next_card.setText(_translate("MainWindow", "Next"))
        if forward:
            self.subject_name.setText(_translate("MainWindow", "Chapter:-"+self.subject_exist.currentText()))
            globals()['current_subject'] = self.subject_exist.currentText()
        else:
            global current_subject
            self.subject_name.setText(_translate("MainWindow", "Chapter:-" + current_subject))
        self.back3.setText(_translate("MainWindow", "Back"))
        self.delete_card.setText(_translate("MainWindow", "Delete"))

    def delete_flash_retranslateUi(self, MainWindow,lst_to_del):
        color_sep = '|:!!:|'
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        start = 0
        for i in lst_to_del:
            self.all_flash_cards_to_delete.setItemText(start, _translate("MainWindow", i.split(color_sep)[0]))
            start += 1
        self.back5.setText(_translate("MainWindow", "Back"))
        self.delete_button.setText(_translate("MainWindow", "delete"))
    def new_subject_retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","MainWindow"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.creatsubject.setText(_translate("MainWindow", "Create"))
        self.back1.setText(_translate("MainWindow",'back'))
    def existing_retranslateUi(self, MainWindow,sub):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        start=0
        for i in sub:
            self.subject_exist.setItemText(start, _translate("MainWindow", i[:-10]))
            start+=1
        self.go.setText(_translate("MainWindow", "GO"))
        self.back2.setText(_translate("MainWindow", "back"))

    def creatflashcardretranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.flashcard_text.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.bg_color.setItemText(0, _translate("MainWindow", "White"))
        self.bg_color.setItemText(1, _translate("MainWindow", "Red"))
        self.bg_color.setItemText(2, _translate("MainWindow", "Blue"))
        self.bg_color.setItemText(3, _translate("MainWindow", "Green"))
        self.creat_the_flashcard.setText(_translate("MainWindow", "Create"))
        self.back4.setText(_translate("MainWindow", "Back"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
