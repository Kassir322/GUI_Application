import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий


from PyQt5 import QtWidgets

import main_window_design as design # Это наш конвертированный файл дизайна
import file_frame as frame_design

# GLOBAL variables
frame_count = 0 # счетчик добавленных файлов
frame_array = [] # массив, содержащий в себе экземпляры класса FileFrame
directory = False

def print_frame_array():
    global frame_array
    global directory

    for j in range(2): # без двойного прохода почему-то не удаляются сразу 
        for i in frame_array: # все элементы
            i.try_to_delete()


class AudioRecordApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.UpdateButton.clicked.connect(update_frame)
        self.DeleteButton.clicked.connect(print_frame_array)

class FileFrame(QtWidgets.QFrame, frame_design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global frame_count
        frame_count += 1
        self.setObjectName('frame%d' % frame_count)
        # print(self.objectName()) 

    def set_caption(self, info: str):
        self.lineEdit.setText(info)
        # print(self.lineEdit.text())

    def try_to_delete(self):
        if self.radioButton.isChecked():
            self.deleteLater()
            os.remove('%s\\%s' % (directory, self.lineEdit.text()))
            frame_array.remove(self)
        pass


def update_frame():
    global window
    global frame_count
    global frame_array
    frame_count = 0

    while window.verticalLayout_5.count() > 0:
        item = window.verticalLayout_5.takeAt(0)
        check = item.widget()
        if check:
            check.deleteLater()

    global directory
    directory = False
    directory = QtWidgets.QFileDialog.getExistingDirectory(window, 'choose folder')

    if directory:
        for file_name in os.listdir(directory):
            if file_name[-3:] == 'm4a':
                window.frame = FileFrame()
                window.frame.set_caption(file_name)
                # ТУТ ДОБАВЛЯТЬ В МАССИВ window.frame
                frame_array.append(window.frame)
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