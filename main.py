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
        self.UpdateButton.clicked.connect(update_frame)

class FileFrame(QtWidgets.QFrame, frame_design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global frame_count
        frame_count += 1
        self.setObjectName('frame%d' % frame_count)
        print(self.objectName()) 

    def set_caption(self, info: str):
        self.lineEdit.setText(info)
        print(self.lineEdit.text())

def update_frame():
    global window
    print()
    global frame_count
    frame_count = 0

    while window.verticalLayout_5.count() > 0:
        item = window.verticalLayout_5.takeAt(0)
        check = item.widget()
        if check:
            check.deleteLater()

    directory = QtWidgets.QFileDialog.getExistingDirectory(window, 'choose folder')

    if directory:
        for file_name in os.listdir(directory):
            if file_name[-3:] == 'm4a':
                # print(file_name)
                window.frame = QtWidgets.QFrame(window.scrollAreaWidgetContents_2)
                window.frame = FileFrame()
                window.frame.set_caption(file_name)
                # frame_count += 1
                # window.frame.setObjectName('frame%d' % frame_count)
                window.verticalLayout_5.addWidget(window.frame)

def main():
    global window
    app = QtWidgets.QApplication(sys.argv)
    window = AudioRecordApp()
    window.show()
    app.exec_()

window = None

if __name__ == '__main__':
    main()