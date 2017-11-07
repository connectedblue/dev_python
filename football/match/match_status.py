

			
		
# Exception classes to catch the match status

class MatchStatus(Exception):
	status = None
	def __init__(self):
		self.status = self.__class__.status

class MatchNotStarted(MatchStatus):
	status = "Match not started"

class MatchInProgress(MatchStatus):
	status = "Match under way"

class MatchFinished(MatchStatus):
	status = "Match finished"



