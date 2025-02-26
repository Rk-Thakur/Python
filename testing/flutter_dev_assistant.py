# import sys
# import subprocess
# import requests
# import json
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog
# )
# from PyQt6.QtCore import Qt, QThread, pyqtSignal


# class FlutterCommandThread(QThread):
#     output_signal = pyqtSignal(str)

#     def __init__(self, command):
#         super().__init__()
#         self.command = command

#     def run(self):
#         process = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         output, error = process.communicate()
#         self.output_signal.emit(output if output else error)


# class FlutterDevAssistant(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()

#         # Project Creation
#         self.project_label = QLabel("Project Name:")
#         self.project_input = QLineEdit()
#         self.project_btn = QPushButton("Create Flutter Project")
#         self.project_btn.clicked.connect(self.create_flutter_project)

#         # # Command Execution
#         # self.command_label = QLabel("Run Flutter Command:")
#         # self.command_input = QLineEdit()
#         # self.command_input.setPlaceholderText("Example: flutter pub get")
#         # self.command_btn = QPushButton("Run Command")
#         # self.command_btn.clicked.connect(self.run_flutter_command)

#         # Package Manager
#         self.package_label = QLabel("Search Flutter Package:")
#         self.package_input = QLineEdit()
#         self.package_btn = QPushButton("Get Package Info")
#         self.package_btn.clicked.connect(self.get_package_info)

#         # JSON to Dart Model
#         self.json_label = QLabel("Paste JSON to Convert:")
#         self.json_input = QTextEdit()
#         self.json_btn = QPushButton("Convert to Dart Model")
#         self.json_btn.clicked.connect(self.convert_json_to_dart)

#         # Output Box
#         self.output_box = QTextEdit()
#         self.output_box.setReadOnly(True)

#         # Add Widgets to Layout
#         layout.addWidget(self.project_label)
#         layout.addWidget(self.project_input)
#         layout.addWidget(self.project_btn)

#         # layout.addWidget(self.command_label)
#         # layout.addWidget(self.command_input)
#         # layout.addWidget(self.command_btn)

#         layout.addWidget(self.package_label)
#         layout.addWidget(self.package_input)
#         layout.addWidget(self.package_btn)

#         layout.addWidget(self.json_label)
#         layout.addWidget(self.json_input)
#         layout.addWidget(self.json_btn)

#         layout.addWidget(QLabel("Output:"))
#         layout.addWidget(self.output_box)

#         self.setLayout(layout)
#         self.setWindowTitle("Flutter Dev Assistant")
#         self.resize(600, 500)

#     def create_flutter_project(self):
#         project_name = self.project_input.text().strip()
#         if not project_name:
#             self.output_box.append("❌ Please enter a project name.")
#             return

#         directory = QFileDialog.getExistingDirectory(self, "Select Directory")
#         if not directory:
#             return

#         command = f"flutter create {directory}/{project_name}"
#         self.run_command_in_thread(command)

#     # def run_flutter_command(self):
#     #     command = self.command_input.text().strip()
#     #     if not command:
#     #         self.output_box.append("❌ Please enter a Flutter command.")
#     #         return

#     #     self.run_command_in_thread(command)

#     def get_package_info(self):
#         package_name = self.package_input.text().strip()
#         if not package_name:
#             self.output_box.append("❌ Please enter a package name.")
#             return

#         url = f"https://pub.dev/api/packages/{package_name}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             version = data.get("latest", {}).get("version", "Unknown")
#             self.output_box.append(f"✅ {package_name} latest version: {version}")
#         else:
#             self.output_box.append(f"❌ Package '{package_name}' not found.")

#     def convert_json_to_dart(self):
#         json_data = self.json_input.toPlainText().strip()
#         try:
#             parsed = json.loads(json_data)
#             dart_model = "class MyModel {\n"
#             for key, value in parsed.items():
#                 dart_model += f"  final {type(value).__name__} {key};\n"
#             dart_model += "  MyModel({required this." + ", required this.".join(parsed.keys()) + "});\n"
#             dart_model += "}"
#             self.output_box.append(f"✅ Generated Dart Model:\n{dart_model}")
#         except json.JSONDecodeError:
#             self.output_box.append("❌ Invalid JSON format.")

#     def run_command_in_thread(self, command):
#         self.output_box.append(f"🔄 Running: {command}")
#         self.thread = FlutterCommandThread(command)
#         self.thread.output_signal.connect(self.update_output)
#         self.thread.start()

#     def update_output(self, output):
#         self.output_box.append(f"✅ Output:\n{output}")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FlutterDevAssistant()
#     window.show()
#     sys.exit(app.exec())


import sys
import subprocess
import requests
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLineEdit, QTextEdit, QLabel, QFileDialog, QGroupBox, QSizePolicy
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon, QColor, QTextCharFormat

# Custom color palette
COLORS = {
    "background": "#2D2D2D",
    "foreground": "#DCDCDC",
    "primary": "#42A5F5",
    "secondary": "#66BB6A",
    "error": "#EF5350",
    "success": "#66BB6A",
    "warning": "#FFCA28"
}

class FlutterCommandThread(QThread):
    output_signal = pyqtSignal(str, str)  # message, color

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        process = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        if error:
            self.output_signal.emit(error, COLORS["error"])
        else:
            self.output_signal.emit(output, COLORS["success"])

class FlutterDevAssistant(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_styles()
        self.init_ui()

    def setup_styles(self):
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {COLORS["background"]};
                color: {COLORS["foreground"]};
            }}
            QPushButton {{
                background-color: {COLORS["primary"]};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {COLORS["secondary"]};
            }}
            QLineEdit, QTextEdit {{
                background-color: #373737;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 6px;
            }}
            QGroupBox {{
                border: 1px solid #555;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 10px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
                color: {COLORS["primary"]};
            }}
        """)

    def create_group_box(self, title, widgets):
        group = QGroupBox(title)
        layout = QVBoxLayout()
        for widget in widgets:
            if isinstance(widget, QWidget):
                layout.addWidget(widget)
            else:
                layout.addLayout(widget)
        group.setLayout(layout)
        return group

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Project Creation Section
        self.project_input = QLineEdit()
        self.project_input.setPlaceholderText("Enter project name...")
        browse_btn = QPushButton("Browse...")
        browse_btn.setIcon(QIcon.fromTheme("folder"))
        browse_btn.clicked.connect(self.select_directory)
        project_btn = QPushButton("Create Flutter Project")
        project_btn.setIcon(QIcon.fromTheme("document-new"))
        project_btn.clicked.connect(self.create_flutter_project)
        
        project_layout = QHBoxLayout()
        project_layout.addWidget(self.project_input)
        project_layout.addWidget(browse_btn)
        project_group = self.create_group_box("Project Setup", [
            QLabel("Project Name:"),
            project_layout,
            project_btn
        ])

        # Package Search Section
        self.package_input = QLineEdit()
        self.package_input.setPlaceholderText("Enter package name...")
        package_btn = QPushButton("Search Package")
        package_btn.setIcon(QIcon.fromTheme("search"))
        package_btn.clicked.connect(self.get_package_info)
        package_group = self.create_group_box("Package Manager", [
            self.package_input,
            package_btn
        ])

        # JSON to Dart Section
        self.json_input = QTextEdit()
        self.json_input.setPlaceholderText("Paste your JSON here...")
        json_btn = QPushButton("Convert to Dart Model")
        json_btn.setIcon(QIcon.fromTheme("text-x-generic"))
        json_btn.clicked.connect(self.convert_json_to_dart)
        json_group = self.create_group_box("JSON Converter", [
            self.json_input,
            json_btn
        ])

        # Output Section
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setFont(QFont("Monospace", 10))
        clear_btn = QPushButton("Clear Output")
        clear_btn.setIcon(QIcon.fromTheme("edit-clear"))
        clear_btn.clicked.connect(lambda: self.output_box.clear())
        output_group = self.create_group_box("Output", [
            self.output_box,
            clear_btn
        ])

        # Assemble main layout
        main_layout.addWidget(project_group)
        main_layout.addWidget(package_group)
        main_layout.addWidget(json_group)
        main_layout.addWidget(output_group)

        self.setLayout(main_layout)
        self.setWindowTitle("Flutter Dev Assistant")
        self.setWindowIcon(QIcon.fromTheme("applications-development"))
        self.resize(800, 700)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.project_input.setText(directory)

    def create_flutter_project(self):
        project_name = self.project_input.text().strip()
        if not project_name:
            self.append_output("Please enter a project name.", COLORS["error"])
            return

        command = f"flutter create {project_name}"
        self.run_command_in_thread(command)

    def get_package_info(self):
        package_name = self.package_input.text().strip()
        if not package_name:
            self.append_output("Please enter a package name.", COLORS["error"])
            return

        url = f"https://pub.dev/api/packages/{package_name}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                version = data.get("latest", {}).get("version", "Unknown")
                self.append_output(f"{package_name} latest version: {version}", COLORS["success"])
            else:
                self.append_output(f"Package '{package_name}' not found.", COLORS["error"])
        except Exception as e:
            self.append_output(f"Error: {str(e)}", COLORS["error"])

    def convert_json_to_dart(self):
        json_data = self.json_input.toPlainText().strip()
        try:
            parsed = json.loads(json_data)
            class_name = "MyModel"
            dart_model = f"class {class_name} {{\n"
            constructor_params = []
            for key, value in parsed.items():
                dart_type = self._map_json_type(value)
                dart_model += f"  final {dart_type} {key};\n"
                constructor_params.append(f"required this.{key}")
            dart_model += f"\n  {class_name}({{"
            dart_model += ", ".join(constructor_params)
            dart_model += "});\n}"
            self.append_output(f"Generated Dart Model:\n{dart_model}", COLORS["success"])
        except json.JSONDecodeError:
            self.append_output("Invalid JSON format.", COLORS["error"])

    def _map_json_type(self, value):
        if isinstance(value, bool):
            return "bool"
        elif isinstance(value, int):
            return "int"
        elif isinstance(value, float):
            return "double"
        elif isinstance(value, dict):
            return "Map<String, dynamic>"
        elif isinstance(value, list):
            return "List<dynamic>"
        return "String"

    def run_command_in_thread(self, command):
        self.append_output(f"Running: {command}", COLORS["primary"])
        self.thread = FlutterCommandThread(command)
        self.thread.output_signal.connect(self.append_output)
        self.thread.start()

    def append_output(self, message, color=None):
        if color:
            self.output_box.setTextColor(QColor(color))
        self.output_box.append(message)
        self.output_box.setTextColor(QColor(COLORS["foreground"]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlutterDevAssistant()
    window.show()
    sys.exit(app.exec())