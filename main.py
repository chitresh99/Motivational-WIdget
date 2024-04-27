import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu, QAction, QVBoxLayout
import os
import random


class MotivationalPuppet(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # List of image paths
        self.image_dir = "images"
        self.image_names = os.listdir(self.image_dir)
        self.image_paths = [os.path.join(self.image_dir, name) for name in self.image_names]
        self.current_image_index = 0

        # Add puppet image label
        self.label = QLabel(self)
        self.load_image()  # Load initial image

        self.notification_label = QLabel("", self)
        self.notification_label.setAlignment(Qt.AlignCenter)
        self.notification_label.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50); color: blue; font-size: 16px; font-weight: bold; font-family: "
            "Arial;")

        # Button to change quotes
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_quote_timer)

        # Button to change the avatar
        self.change_avatar_button = QPushButton("Change Avatar", self)
        self.change_avatar_button.clicked.connect(self.change_avatar)

        # layout
        layout = QVBoxLayout(self)  # Use the QWidget as the parent
        layout.addWidget(self.notification_label)  # Notification label added first
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.change_avatar_button)

        # Staring timer for quote updates
        self.quote_timer = QTimer(self)
        self.quote_timer.timeout.connect(self.show_quote)

    def load_image(self):
        # Load image based on current index
        pixmap = QPixmap(self.image_paths[self.current_image_index])
        if pixmap.isNull():
            print("Error loading image")
            return

        # Resizing the image
        pixmap = pixmap.scaledToWidth(200)
        self.label.setPixmap(pixmap)

        # Removing padding around the image

        self.label.setContentsMargins(0, 0, 0, 0)

    def show_quote(self):
        quotes = [
            "You've got this!",
            "Stay motivated!",
            "Keep going!",
            "You're awesome!"
        ]
        quote = random.choice(quotes)
        self.notification_label.setText(quote)

    def change_avatar(self):
        # Incrementing the index and cycle back to 0 if it exceeds the number of images
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_image()

    def start_quote_timer(self):
        self.quote_timer.start(1000)  # timer for quote

    def stop_quote_timer(self):
        self.quote_timer.stop()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.drag_pos)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)
        menu.exec_(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    puppet = MotivationalPuppet()
    puppet.show()
    sys.exit(app.exec_())
