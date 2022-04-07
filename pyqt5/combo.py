#LEARN PYQT5 
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

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

        #create an combo box
        my_combo = qtw.QComboBox(self,
            editable=True, 
            insertPolicy=qtw.QComboBox.InsertAtTop)
        #add items to the combo box
        my_combo.addItem("Pepperoni","Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Chilli", qtw.QWidget)
        my_combo.addItem("Bacon")
        my_combo.addItem("Avo")
        my_combo.addItems(["Peppers","Feta","Spinage"])
        my_combo.insertItem(2,"Third thing")
        my_combo.insertItems(3,["Fourth thing","Fifth thing"])
        #insert combo bx on screen 
        self.layout().addWidget(my_combo)

        #creat a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        #show the app
        self.show()

        def press_it():
            #add name to label
            my_label.setText(f'You picked {my_combo.currentText()}!') #currentText reference the first, Currentdata reference the sencond, Currentindex refernce the index number of the item 

            




app = qtw.QApplication([])
mw = MainWindow()

#run the app
app.exec_()