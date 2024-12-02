import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QSpinBox, QCheckBox, QPushButton, QTextEdit
)

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 300)

        # Central Widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout
        layout = QVBoxLayout()

        # Length
        self.length_label = QLabel("Password Length:")
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(4, 64)
        self.length_spinbox.setValue(12)

        # Options
        self.uppercase_checkbox = QCheckBox("Include Uppercase Letters")
        self.uppercase_checkbox.setChecked(True)
        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.numbers_checkbox.setChecked(True)
        self.special_checkbox = QCheckBox("Include Special Characters")
        self.special_checkbox.setChecked(True)

        # Generate Button
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        # Output
        self.output_label = QLabel("Generated Password:")
        self.output_text = QLineEdit()
        self.output_text.setReadOnly(True)

        # Add widgets to layout
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_spinbox)
        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.numbers_checkbox)
        layout.addWidget(self.special_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)

        self.central_widget.setLayout(layout)

    def generate_password(self):
        length = self.length_spinbox.value()
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_numbers = self.numbers_checkbox.isChecked()
        use_special = self.special_checkbox.isChecked()

        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.output_text.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())

