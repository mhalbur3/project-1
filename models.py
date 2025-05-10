from dataclasses import dataclass
@dataclass

class Candidate:
    name: str
    votes: int = 0
    def addVote(self):
        """Increments the vote count for this candidate."""
        self.votes += 1
    def returnVote(self):
        """Returns the vote count."""
        return self.votes
