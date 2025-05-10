import csv
import os
from typing import Dict, List

class Candidate:
    """Represents a candidate in the election."""
    def __init__(self, name: str) -> None:
        self.name = name
        self.votes = 0
    def increaseVote(self) -> None:
        """Increment the vote count for this candidate."""
        self.votes += 1
    def __str__(self) -> str:
        return self.name
    def returnVote(self) -> int:
        """Returns the vote count."""
        return self.votes

class manageVotes:
    """Manages the voting process, voter ID validation, and tracks the candidate."""
    def __init__(self, candidates: List[str], votes_filename: str, voter_ids_filename: str) -> None:
        self.candidates = {name: Candidate(name) for name in candidates}
        self.voteFile = votes_filename
        self.voterIDFile = voter_ids_filename
        self.voterIDs = self.loadID()
        self.loadVotesFromCSV()  # Load vote data from CSV when initializing
    def saveID(self, voter_id: str, chosenCandidate: str) -> None:
        """Saves the ID and the chosen candidate."""
        with open(self.voterIDFile, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, chosenCandidate])
    def loadID(self) -> set:
        """Loads saved voter IDs from the CSV."""
        if not os.path.exists(self.voterIDFile):
            return set()
        with open(self.voterIDFile, mode='r', newline='') as file:
            return {row[0] for row in csv.reader(file) if row}
    def loadVotesFromCSV(self) -> None:
        """Loads the vote counts from the CSV file and updates candidate votes."""
        if os.path.exists(self.voteFile):
            with open(self.voteFile, mode='r', newline='') as file:
                reader = csv.reader(file)
                for nameCanidate, vote_count in reader:
                    if nameCanidate in self.candidates:
                        self.candidates[nameCanidate].votes = int(vote_count)
    def hasVoted(self, voter_id: str) -> bool:
        """Check if a voter has already voted."""
        return voter_id in self.voterIDs
    def voteChoose(self, selected_candidate: str, voter_id: str) -> None:
        """Saves the vote selection and the voter ID."""

        if voter_id in self.voterIDs:
            raise Exception(f"{voter_id} has already voted")

        self.saveID(voter_id, selected_candidate)
        self.voterIDs.add(voter_id)
        candidate = self.candidates.get(selected_candidate)

        if not candidate:
            raise Exception(f"Invalid candidate selected: {selected_candidate}")
        candidate.increaseVote()
    def getResults(self) -> str:
        """Return formatted vote results."""
        return '\n'.join(
            f"{candidate.name}: {candidate.returnVote()} vote(s)" for candidate in self.candidates.values())
    def saveVotesToCSV(self) -> None:
        """Save vote counts to a CSV file."""
        try:
            with open(self.voteFile, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "votes"])
                for candidate in self.candidates.values():
                    writer.writerow([candidate.name, candidate.returnVote()])
        except IOError as e:
            raise RuntimeError(f"Error: Failed to save votes {e}")
