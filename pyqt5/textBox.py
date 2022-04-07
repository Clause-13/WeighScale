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
        my_label = qtw.QLabel("Type something into the box below")
        
        #change the font size of label
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        #create an text box
        my_text = qtw.QTextEdit(self,
            # plainText='This is real Text!',
            # html = "<h1>Hello in h1</h1>",
            acceptRichText=True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Enter Text!",
            readOnly=False,
            )
        #put spinbox on the screen
        self.layout().addWidget(my_text)

        #creat a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        #show the app
        self.show()

        def press_it():
            #add name to label
            my_label.setText(f'You typed {my_text.toPlainText()}!')
            my_text.setPlainText("You Pressed the button!")
            




app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()