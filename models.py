from dataclasses import dataclass
@dataclass

class Candidate:
    """The voting candidates."""
    name: str
    votes: int = 0
    def add_vote(self) -> None:
        """Increases the candidate's vote count."""
        self.votes += 1
