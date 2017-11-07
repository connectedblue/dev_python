
from six import string_types

class Team(object):

	def __init__(self, team_name=None):
		if(team_name is not None and  not isinstance(team_name, string_types)):
			raise Exception("Team name must be a string")

		self.name=team_name

