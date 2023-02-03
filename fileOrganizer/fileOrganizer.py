#Author: Paweł Paciorkowski
import os
import shutil
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QCheckBox



class FileOrganizer(QMainWindow): #Inheritance
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
     # Set window title
        self.setWindowTitle("Organizator Twoich plików - Paweł Paciorkowski")
    
        # Create file browser button
        browse_btn = QtWidgets.QPushButton("Wybierz co chcesz uporządkować", self)
        browse_btn.clicked.connect(self.browse_folder)

        # Create checkboxes for file types to be organized
        images_chk = QCheckBox("Zdjęcia", self)
        videos_chk = QCheckBox("Filmy", self)
        documents_chk = QCheckBox("Dokumanty", self)
        images_chk.setChecked(True)
        videos_chk.setChecked(True)
        documents_chk.setChecked(True)
    
    # Add the button to the window layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(browse_btn)
        layout.addWidget(images_chk)
        layout.addWidget(videos_chk)
        layout.addWidget(documents_chk)
        widget = QtWidgets.QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def browse_folder(self):
        # Show file browser and select directory to organize
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Wybież folder")
        self.organize_files(directory)


    def organize_files(self, directory):
        # Check if directory is valid
        if not os.path.exists(directory):
            QtWidgets.QMessageBox.critical(self, "Błąd", "Wybrano nieprawidłowy folder. Proszę wybrać prawidłowy folder.")
            return
        
        # Get a list of all files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        # Create subdirectories for different file types (e.g. images, videos, documents)
        subdirectories = {"Zdjęcia": [".jpeg", ".jpg", ".png", ".gif"],
                        "Filmy": [".mp4", ".mkv", ".avi", ".mov"],
                        "Dokumenty": [".docx", ".pdf", ".txt"]}
        for subdir, extensions in subdirectories.items():
            subdir_path = os.path.join(directory, subdir)
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)

        # Move each file to its corresponding subdirectory based on its file type
        for file in files:
            file_path = os.path.join(directory, file)
            for subdir, extensions in subdirectories.items():
                if file.endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(directory, subdir, file))
                    break


    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = FileOrganizer()
    window.show()
    app.exec()

