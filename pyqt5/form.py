#LEARN PYQT5 
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg
from numpy import maximum, minimum

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!!")

        #set  vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #create a label
        my_label = qtw.QLabel("Pick something from the list")
        
        #change the font size of label
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        #create an spin box
        my_spin = qtw.QSpinBox(self,
            value=10,
            maximum=200, 
            minimum=0,
            singleStep=5)
        #put spinbox on the screen
        self.layout().addWidget(my_spin)

        #creat a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        #show the app
        self.show()

        def press_it():
            #add name to label
            my_label.setText(f'You picked {my_spin.value()}!') #currentText reference the first, Currentdata reference the sencond, Currentindex refernce the index number of the item 

            




app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()