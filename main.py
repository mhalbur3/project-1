import sys
import re
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from logic import manageVotes
from gui import Ui_MainWindow

class Vote(QMainWindow, Ui_MainWindow):
    """The GUI class that controls the votes."""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.vote_manager = manageVotes(
            candidates=["John", "Jane"],
            votes_filename="votes.csv",
            voter_ids_filename="voterIDs.csv"
        )
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
    def submitWindow(self) -> None:
        """Submit window and displays updated results. Error messages for invalid IDs or repetition"""
        self.textResults.clear()
        voterID = self.inputID.text().strip()
        chosenCanidate = None

        if not self.validateID(voterID):
            self.showMessage("Invalid ID. Use your 1-10 character ID", "red")
            return
        if self.vote_manager.hasVoted(voterID):
            self.showMessage("You have already voted", "red")
            return

        if self.radioJohn.isChecked():
            chosenCanidate = "John"
        elif self.radioJane.isChecked():
            chosenCanidate = "Jane"

        if not chosenCanidate:
            QMessageBox.warning(self, "Invalid", "Please select a candidate...")
            return

        try:
            self.vote_manager.voteChoose(chosenCanidate, voterID)
            self.vote_manager.saveVotesToCSV()
            self.showMessage(
                f"Successful vote\nResults:\n{self.vote_manager.getResults()}",
                "green"
            )
            self.radioJohn.setChecked(False)
            self.radioJane.setChecked(False)
            self.inputID.clear()
        except Exception as e:
            print(f"Error: {str(e)}")
            QMessageBox.critical(self, "Error", f"{str(e)}")
    def voteWindow(self) -> None:
        """Shows the vote menu."""
        self.frameMainMenu.hide()
        self.frameVoteMenu.show()
    def validateID(self, voter_id: str) -> bool:
        """Validates the voter ID format."""
        return bool(re.fullmatch(r'\w{1,10}', voter_id))
    def showMessage(self, message: str, color: str) -> None:
        """Displays a colored message in the result box."""
        self.textResults.setStyleSheet(f"color: {color};")
        self.textResults.setText(message)

if __name__ == "__main__":
    mainWindow = QApplication(sys.argv)
    window = Vote()
    window.show()
    sys.exit(mainWindow.exec())
