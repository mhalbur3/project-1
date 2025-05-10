from models import Candidate
from storage import LoadToCSV, saveToCSV

class manageVotes:
    """Manages the voting logic and candidates."""
    def __init__(self, candidate_names: list[str], storage_path: str = "votes.csv") -> None:
        """Makes the candidates and loads the vote data."""
        self._saveCSV = storage_path
        self._candidates: dict[str, Candidate] = {name: Candidate(name) for name in candidate_names}
        self.loadVote()
    def voteChoose(self, canidateChoice: str) -> None:
        """Gives the vote to the canidate."""
        if canidateChoice in self._candidates:
            self._candidates[canidateChoice].add_vote()
            self.saveVote()
        else:
            raise ValueError(f"Candidate '{canidateChoice}' does not exist.")
    def getResults(self) -> str:
        """Obtains the vote results."""
        return "\n".join(
            f"{candidate.name}: {candidate.votes} votes" for candidate in self._candidates.values()
        )
    def loadVote(self) -> None:
        """Loads votes from the CSV."""
        try:
            loadingVotes = LoadToCSV(self._saveCSV)
            for name, votes in loadingVotes.items():
                if name in self._candidates:
                    self._candidates[name].votes = votes
        except Exception:
            pass

    def saveVote(self) -> None:
        """Saves votes to the CSV."""
        info = {name: candidate.votes for name, candidate in self._candidates.items()}
        saveToCSV(self._saveCSV, info)
