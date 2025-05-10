import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from logic import manageVotes
from gui import Ui_MainWindow

class Vote(QMainWindow, Ui_MainWindow):
    """The GUI class that controls the votes."""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.vote_manager = manageVotes(["John", "Jane"])
        self.frameMainMenu.show()
        self.frameVoteMenu.hide()
        self.buttonVote.clicked.connect(self.voteWindow)
        self.buttonExit.clicked.connect(self.close)
        self.buttonBack.clicked.connect(self.mainWindow)
        self.buttonSubmitVote.clicked.connect(self.submitWindow)
    def mainWindow(self) -> None:
        """Shows the main window."""
        self.frameVoteMenu.hide()
        self.frameMainMenu.show()
    def voteWindow(self) -> None:
        """Shows the vote menu."""
        self.frameMainMenu.hide()
        self.frameVoteMenu.show()
    def submitWindow(self) -> None:
        """Submit window and displays updated results."""
        self.textResults.clear()
        selected_candidate = (
            "John" if self.radioJohn.isChecked()
            else "Jane" if self.radioJane.isChecked()
            else None
        )
        if not selected_candidate:
            QMessageBox.warning(self, "Error", "Please select a candidate...")
            return
        try:
            self.vote_manager.voteChoose(selected_candidate)
            self.textResults.setText(
                f"Thank you for your vote!\n"
                f"Results:\n{self.vote_manager.getResults()}"
            )
            self.radioJohn.setChecked(False)
            self.radioJane.setChecked(False)
        except Exception as e:
            QMessageBox.critical(self, "An error", f"has occurred: {str(e)}")

if __name__ == "__main__":
    mainWindow = QApplication(sys.argv)
    window = Vote()
    window.show()
    sys.exit(mainWindow.exec())
