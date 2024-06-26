import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt

class AboutPage(QWidget):
    returnToIndexSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(top_layout)

        self.index_button = QPushButton("☰")
        self.index_button.setStyleSheet("""
                                        QPushButton {
                                            font-size: 25px;
                                            background-color: rgba(0, 0, 0, 0);
                                            color: #2DD096;
                                            padding: 2px 25px;
                                            border-radius: 5px;
                                        }
                                        
                                        QPushButton:hover {
                                            background-color: rgba(255, 255, 255, 0.1);
                                        }
                                        
                                        QPushButton:pressed {
                                            background-color: rgba(255, 255, 255, 0.2);
                                        }
            """
        )
        self.index_button.clicked.connect(self.emit_return_to_index_signal)
        layout.addWidget(self.index_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        top_layout.addWidget(self.index_button)
        top_layout.addSpacing(30)

        help_label = QLabel("ABOUT")
        help_label.setStyleSheet("font-size: 40px; letter-spacing: 10px; font-weight: bold;")
        top_layout.addWidget(help_label)

        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("border: none; background-color: #0c1221;")
        layout.addWidget(scroll_area)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(inner_widget)
        scroll_area.setWidgetResizable(True)

        self.add_paragraph("Welcome to XSSify, an educational application designed to teach users about Cross-Site Scripting (XSS) attacks. XSSify is created with the goal of raising awareness about the potential risks and vulnerabilities associated with XSS attacks and empowering users to protect themselves and their applications against such threats.", inner_layout)

        self.add_heading("Our Mission", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            At XSSify, our mission is to educate individuals and organizations about XSS attacks and provide them with the knowledge and tools necessary to prevent and mitigate these threats. We believe that by understanding how XSS attacks work and adopting best practices for web security, users can safeguard their data and protect against potential exploitation.
        """, inner_layout)

        self.add_heading("Get Involved", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            Join us in our mission to promote web security and combat XSS attacks. Whether you're a beginner looking to learn or an expert willing to contribute, there are many ways to get involved with XSSify: <br><br> <b><em>Spread the Word</em></b>: Share XSSify with your friends, colleagues, and networks to help raise awareness about XSS attacks and the importance of web security. <br><br>
            <b><em>Contribute Content</em></b>: Are you knowledgeable about XSS attacks or web security? Consider contributing tutorials, quizzes, or case studies to help enrich the learning experience for our users. <br><br>
            <b><em>Report Vulnerabilities</em></b>: If you discover XSS vulnerabilities in websites or applications, report them responsibly to the respective organizations and help make the web a safer place for everyone.
        """, inner_layout)

        self.add_heading("Stay Secure, Stay Informed", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            Thank you for choosing XSSify as your trusted resource for learning about XSS attacks and web security. Together, let's make the internet a safer place for everyone.
        """, inner_layout)

        self.add_heading("Contact Us", inner_layout, font_size=30, alignment=Qt.AlignmentFlag.AlignCenter)
        self.add_paragraph("""
            Have questions, feedback, or suggestions for XSSify? We'd love to hear from you! Get in touch with us via email at <em>contact@xssify.com</em>
        """, inner_layout)

    def add_heading(self, text, parent_layout, font_size, alignment):
        heading_label = QLabel(text)
        heading_label.setStyleSheet(f"font-size: {font_size}px; text-decoration: underline; letter-spacing: 2px; font-weight: bold; color: #2DD096;")
        parent_layout.addWidget(heading_label, alignment=alignment)

    def add_paragraph(self, text, parent_layout):
        paragraph_label = QLabel(text)
        paragraph_label.setStyleSheet("font-size: 25px; text-align: justify; padding: 10px 60px 60px 60px; letter-spacing: 2px;")
        paragraph_label.setWordWrap(True)

        paragraph_label.setTextFormat(Qt.TextFormat.RichText)
        paragraph_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        for word in ["XSSify"]:
            text = text.replace(word, f"<em>{word}</em>")

        paragraph_label.setText(text)

        parent_layout.addWidget(paragraph_label, alignment=Qt.AlignmentFlag.AlignTop)

    def emit_return_to_index_signal(self):
        self.returnToIndexSignal.emit()