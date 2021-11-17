from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from altyazicevirici_ui import Ui_MainWindow

from translate import Translator
import os

class app(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        #signal-slot bağlantıları
        self.FileInputButton.clicked.connect(self.onInputFileButtonClicked)
        self.Translate.clicked.connect(self.onTranslateButtonClicked)

    def onInputFileButtonClicked(self):
        filename, filter = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select A File',
        )
        self.FileInput.setText(filename)
        self.FileInputButton.setText("Change")
    
    def onTranslateButtonClicked(self):
        global filePath
        global mainLang
        global targetLang
        filePath = self.FileInput.text().strip(" ")
        mainLang = self.MainLangInput.text().strip(" ")
        targetLang = self.TargetLangInput.text().strip(" ")
        if len(filePath) == 0:
            self.FileInput.setText("Please select a file")
            QMessageBox.warning(self, "Warning", "Please select a file")
            self.FileInput.setText("")

        elif len(mainLang) == 0:
            self.MainLangInput.setText("Please select a main language")
            QMessageBox.warning(self, "Warning", "Please select a main language")
            self.MainLangInput.setText("")
        
        elif len(targetLang) == 0:
            self.TargetLangInput.setText("Please select a target language")
            QMessageBox.warning(self, "Warning", "Please select a target language")
            self.TargetLangInput.setText("")
        
        else:
            try:
                self.translate(filePath)
                QMessageBox.information(self, "Information", "Translate Successful")
                QMessageBox.information(self, "Information", "File saved in "+file_dir)
                self.FileInput.setText("")
                self.MainLangInput.setText("")
                self.TargetLangInput.setText("")
            except:
                QMessageBox.warning(self, "Warning", "Translate Failed") 
    
    def translate(self,file_path):
        try:        
            global file_dir
            global file_ext
            with open(file_path,"r",encoding="utf-8") as f:
                file = f.read()
                translator= Translator(from_lang=mainLang,to_lang=targetLang)
                translation = translator.translate(file)
                
                file_dir = os.path.dirname(file_path)
                file_ext = os.path.basename(file_path)
                file_name = file_ext.split(".")[0]
                file_ext = file_ext.split(".")[1]
                
                
                
                with open(file_dir+"/"+file_name+"_"+targetLang+"."+file_ext,"w",encoding="utf-8") as nf:
                    nf.write(translation)
                    nf.close()
                
                f.close()
        except:
            QMessageBox.warning(self, "Warning", "Translate Failed")

uygulama = QApplication([])
pencere = app()
pencere.show()
uygulama.exec_()