import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu, QAction, QVBoxLayout
import random


class MotivationalPuppet(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Add puppet image label
        self.label = QLabel(self)
        pixmap = QPixmap('darkrai.png')  # image for the widget
        if pixmap.isNull():
            print("Error loading image")

        # Resizing the image
        pixmap = pixmap.scaledToWidth(200)
        self.label.setPixmap(pixmap)
        self.label.setContentsMargins(0, 0, 0, 0)  # Remove padding around the image

        self.notification_label = QLabel("", self)
        self.notification_label.setAlignment(Qt.AlignCenter)
        self.notification_label.setStyleSheet(
            "background-color: rgba(255, 255, 255, 50); color: blue; font-size: 16px; font-weight: bold; font-family: Arial;")

        # Add a button to start the quote change
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_quote_timer)

        # Setting up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.notification_label)  # Notification label added first
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

        self.resize(250, 250)  # size to fit the resized image and notification label

        # center position
        x_pos = (self.width() - pixmap.width()) // 2
        y_pos = (self.height() - pixmap.height()) // 2

        self.label.setGeometry(x_pos, y_pos, pixmap.width(), pixmap.height())
        self.notification_label.setGeometry(0, 0, self.width(), 20)  # Positioning notification label at the top
        self.start_button.setGeometry(0, self.height() - 30, self.width(), 30)

        # Staring the QTimer for quote updates
        self.quote_timer = QTimer(self)
        self.quote_timer.timeout.connect(self.show_quote)

    def show_quote(self):
        quotes = [
            "You've got this!",
            "Stay motivated!",
            "Keep going!",
            "You're awesome!"
        ]
        quote = random.choice(quotes)
        self.notification_label.setText(quote)

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
