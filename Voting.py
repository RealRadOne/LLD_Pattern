class Vote:
    def __init__(self,ID:int,VID:int):
        self._ID = ID
        self._VID = VID
        self._Party = None

    @property
    def Party(self):
        return self._Party

    @Party.setter
    def Party(self,party:str):
        self._Party = party

class Voter:
    def __init__(self,VID:int):
        self._VID = VID 
        self._Name = None 
        self._Province = None 

    @property
    def VID(self):
        return self._VID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self,name:str):
        self._Name = name

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self,province:str):
        self._Province = province

class VotingMachine:
    def __init__(self):
        self._Votes = {}
        self._Voters = {}

    def register_user(self,name:str,province:str):
        #For simplicity Voter number for now is just serial
        voter = Voter(len(self._Voters)+1)
        voter.Name = name 
        voter.Province = province
        self._Voters[voter.VID] = voter 
        return voter.VID
        

    def collect_vote(self,VID:int,party:str):
        if not isinstance (VID,int):
            raise TypeError
        if not isinstance(party,str):
            raise TypeError
        if VID in self._Votes:
            raise "You have already voted!"
        vote = Vote(len(self._Votes)+1,VID)
        vote.Party = party
        self._Votes[VID] = party 

    def declare_winner(self):
        vote_counter = {}
        if len(self._Votes)==0:
            raise "Voting hs not yet begun"
        for info in self._Votes:
            vote_counter[info]+=1
        majority_vote = 0
        majority_party = ''
        for party in vote_counter:
            if vote_counter[party]>majority_vote:
                majority_party = party
                majority_vote = vote_counter[party]
        print(f'The winning party is {majority_party} with votes {majority_vote}')

if __name__ == "__main__":
    machine = VotingMachine()
    bhartiID = machine.register_user('Bharti','Begusarai')
    sushmaID = machine.register_user('Sushma','Motihari')
    machine.collect_vote(bhartiID,party='BJP')
    machine.collect_vote(bhartiID,party='RJD')




