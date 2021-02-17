import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий


from PyQt5 import QtWidgets

import main_window_design as design # Это наш конвертированный файл дизайна
import file_frame as frame_design

frame_count = 0

class AudioRecordApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.UpdateButton.clicked.connect(self.update_frame)
        

    def update_frame(self):
        global frame_count
        frame_count = 0

        while self.verticalLayout_5.count() > 0:
            item = self.verticalLayout_5.takeAt(0)
            check = item.widget()
            if check:
                check.deleteLater()

        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'choose folder')

        if directory:
            for file_name in os.listdir(directory):
                if file_name[-3:] == 'm4a':
                    # print(file_name)
                    self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
                    self.frame = FileFrame()
                    # frame_count += 1
                    # self.frame.setObjectName('frame%d' % frame_count)
                    self.verticalLayout_5.addWidget(self.frame)
        pass

class FileFrame(QtWidgets.QFrame, frame_design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global frame_count
        frame_count += 1
        self.setObjectName('frame%d' % frame_count)
        print(self.objectName()) 

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AudioRecordApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()