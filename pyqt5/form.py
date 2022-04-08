#LEARN PYQT5 
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg
from numpy import maximum, minimum

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!!")

        #set  vertical layout
        # self.setLayout(qtw.QVBoxLayout())
        # set form layout
        form_layout= qtw.QFormLayout()
        self.setLayout(form_layout)

        # add our widgets
        label_one = qtw.QLabel("This is a cool label row")
        label_one.setFont(qtg.QFont("Helvetica", 18))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # add rows to app 
        form_layout.addRow(label_one)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("Last Name", l_name)
        form_layout.addRow(qtw.QPushButton("Press Me!", clicked = lambda:press_it()))

        #show the app
        self.show()

        def press_it():
            #add name to label
            label_one.setText(f'You clicked the button, {f_name.text()} {l_name.text()}!') #currentText reference the first, Currentdata reference the sencond, Currentindex refernce the index number of the item 

            




app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()