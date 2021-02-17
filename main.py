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
        self.UpdateButton.clicked.connect(self.browse_folder)
        

    def browse_folder(self):
        global frame_count
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        frame_count += 1
        self.frame.setObjectName('frame%d' % frame_count)
        self.verticalLayout_5.addWidget(self.frame)
        
        # directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'choose folder')

        # if directory:
        #     for file_name in os.listdir(directory):
        #         if file_name[-3:] == 'mkv':
        #             print(file_name)
        pass

class FileFrame(QtWidgets.QFrame, frame_design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        print('added')

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AudioRecordApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()