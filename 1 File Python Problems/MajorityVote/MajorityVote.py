"""
Basic Problem Summary:
    Given a list of votes 

    Example Input: ["A","B","A"]
    Example Output: "A"

    Example Input: ["A","A","A","B","C","A"]
    Example Output: "A"

    Example Input: ["A","B","B","A","C","C"]
    Example Output: None
"""
import collections

def MajorityVote(votes: list):
    countedVotes = collections.Counter(votes)
    countedVotesList = list(countedVotes.values())
    if countedVotesList[0] == countedVotesList[1] :
        return None
    return list(countedVotes.keys())[0]

if __name__ == "__main__":
    print(MajorityVote(["A","B","A"]))
    print(MajorityVote(["A","A","A","B","C","A"]))
    print(MajorityVote(["A","B","B","A","C","C"]))
