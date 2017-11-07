from .validate_team import validate_team


from .match_status import MatchStatus, MatchNotStarted, MatchInProgress, MatchFinished


from ..team import Team

class Match:

	# home and away teams must be passed when Match object is instantiated
	# They must be of type Team

	@validate_team(is_playing=False)
	def __init__(self, home_team, away_team):

		self.home_team = Team()
		self.away_team = Team()
		self._set_team(home_team)
		self._set_team(away_team, home=False)

		self.home_goals = 0
		self.away_goals = 0

		self.match_started=False
		self.match_finished=False

	# Match must be started by calling this method before any
	# goals can be scored
	def start(self):
		try:
			self._get_match_status()

		except MatchNotStarted:
			self.match_started = True
			print("Match started")

		except MatchStatus as match:
			print("Can't start: {status}".format(status=match.status))

			
	# After calling this method, no more goals can be scored
	def stop(self):
		try:
			self._get_match_status()

		except MatchInProgress:
			self.match_finished = True
			print("Match ended")

		except MatchStatus as match:
			print("Can't stop: {status}".format(status=match.status))
			
			
	def match_status(self):
		try:
			self._get_match_status()

		except MatchStatus as match:
			print(match.status)



	# call whenever a team playing scores a goal
	@validate_team(is_playing=True)
	def goal_scored_by(self, team):
		try:
			self._get_match_status()

		except MatchInProgress:

			if self.home_team.name==team.name:
				self.home_goals+=1
			elif self.away_team.name==team.name:
				self.away_goals+=1
		
		except MatchStatus as match:
			print("Can't score goals: {status}".format(status=match.status))


	def score(self):
		try:
			self._get_match_status()

		except MatchNotStarted:
			print("{home_team} v {away_team}".format(**self._score_info()))

		except MatchInProgress:
			print("{home_team} {home_goals} - {away_goals} {away_team} - Latest score".format(**self._score_info()))

		except MatchFinished:
			print("{home_team} {home_goals} - {away_goals} {away_team} - FT".format(**self._score_info()))




	# All the functions below are utility functions
	# for the class and shouldn't be called directly 
	# by the users of the class

	@validate_team(is_playing=False)
	def _set_team(self, team, home=True):
		if home:
			self.home_team = team
		else:
			self.away_team = team


	# Helper function to throw an exception
	# denoting the state of the match
	def _get_match_status(self):
		if not self.match_started:
			raise MatchNotStarted
		elif not self.match_finished:
			raise MatchInProgress
		else:
			raise MatchFinished

			
	def _score_info(self):
		return {'home_team': self.home_team.name,
			'away_team': self.away_team.name,
			'home_goals': self.home_goals,
			'away_goals': self.away_goals}

			
		
