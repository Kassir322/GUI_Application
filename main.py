import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий


from PyQt5 import QtWidgets

import main_window_design as design # Это наш конвертированный файл дизайна
import file_frame as frame_design

class AudioRecordApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directoryButton.clicked.connect(self.choose_directory)
        self.deleteButton.clicked.connect(self.delete_checked)
        self.directory = 'D:/python/GUI_Application/audio'
        self.update_frame()

    def choose_directory(self):
        dialog = QtWidgets.QFileDialog(self)
        self.directory = dialog.getExistingDirectory(self, 'Выберите папку', options=dialog.DontUseNativeDialog)
        self.update_frame()

    def print_dir(self):
        print(self.directory)

    def clear_scroll_area(self):
        while self.verticalLayout_5.count() > 0:
                item = self.verticalLayout_5.takeAt(0)
                check = item.widget()
                if check:
                    check.deleteLater()
    
    def update_frame(self):
        self.clear_scroll_area()

        if self.directory:
            for file_name in os.listdir(self.directory):
                if file_name[-3:] == 'm4a':
                    self.frame = FileFrame()
                    self.frame.set_caption(file_name)
                    self.verticalLayout_5.addWidget(self.frame)

    def delete_checked(self):
        # print(self.scrollAreaWidgetContents_2.findChildren(QtWidgets.QFrame))
        for elem in self.scrollAreaWidgetContents_2.findChildren(QtWidgets.QFrame):
            if elem.objectName() == 'frame':
                elem.try_to_delete_frames(self.directory)

class FileFrame(QtWidgets.QFrame, frame_design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setObjectName('frame')
        # print(self.objectName()) 

    def set_caption(self, info: str):
        self.lineEdit.setText(info)
        # print(self.lineEdit.text())

    def try_to_delete_frames(self, directory):
        if self.radioButton.isChecked():
            self.deleteLater()
            # os.remove('%s\\%s' % (directory, self.lineEdit.text()))
        pass

def main():
    global window
    app = QtWidgets.QApplication(sys.argv)
    window = AudioRecordApp()
    window.show()
    app.exec_()

window = None

if __name__ == '__main__':
    main()