import sys
import json
from pathlib import Path
from bale_api import BaleClient
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QPushButton,
    QMessageBox,
    QInputDialog,
    QLabel,
)


ACTIVITIES_FILE = "activities.json"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.client = BaleClient()

        self.setWindowTitle("My Reporter")
        self.resize(500, 400)

        self.activities = []

        self.setup_ui()
        self.load_activities()

        self.setStyleSheet(
            """
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }

            QPushButton {
                background-color: #333333;
                border: 1px solid #555;
                padding: 6px;
            }

            QListWidget {
                background-color: #252525;
            }
            """
        )

    def setup_ui(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)

        buttons_layout = QHBoxLayout()

        self.send_btn = QPushButton("ارسال")
        self.add_btn = QPushButton("افزودن")
        self.edit_btn = QPushButton("ویرایش")
        self.delete_btn = QPushButton("حذف")

        buttons_layout.addWidget(self.send_btn)
        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.edit_btn)
        buttons_layout.addWidget(self.delete_btn)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.send_btn.clicked.connect(self.send_selected)
        self.add_btn.clicked.connect(self.add_activity)
        self.edit_btn.clicked.connect(self.edit_activity)
        self.delete_btn.clicked.connect(self.delete_activity)

    def load_activities(self):
        file_path = Path(ACTIVITIES_FILE)

        if not file_path.exists():
            self.activities = []
            self.save_activities()
            return

        with open(file_path, "r", encoding="utf-8") as f:
            self.activities = json.load(f)

        self.refresh_list()

    def save_activities(self):
        with open(ACTIVITIES_FILE, "w", encoding="utf-8") as f:
            json.dump(self.activities, f, ensure_ascii=False, indent=4)

    def refresh_list(self):
        self.list_widget.clear()

        for activity in self.activities:
            self.list_widget.addItem(activity)

    def add_activity(self):
        text, ok = QInputDialog.getText(self, "افزودن فعالیت", "متن فعالیت:")

        if ok and text.strip():
            self.activities.append(text.strip())
            self.save_activities()
            self.refresh_list()

    def edit_activity(self):
        row = self.list_widget.currentRow()

        if row < 0:
            return

        current_text = self.activities[row]

        text, ok = QInputDialog.getText(
            self, "ویرایش فعالیت", "متن جدید:", text=current_text
        )

        if ok and text.strip():
            self.activities[row] = text.strip()
            self.save_activities()
            self.refresh_list()

    def delete_activity(self):
        row = self.list_widget.currentRow()

        if row < 0:
            return

        reply = QMessageBox.question(self, "حذف", "آیا مطمئن هستید؟")

        if reply == QMessageBox.Yes:
            del self.activities[row]
            self.save_activities()
            self.refresh_list()

    def send_selected(self):
        item = self.list_widget.currentItem()

        if item is None:
            QMessageBox.warning(self, "خطا", "یک فعالیت انتخاب کنید.")
            return

        text = item.text()

        success, result = self.client.send_message(text)

        if success:
            self.status_label.setText(f"✅ ارسال شد: {text}")
        else:
            self.status_label.setText(f"❌ خطا در ارسال")

            QMessageBox.critical(self, "Error", str(result))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
