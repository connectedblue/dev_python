

# decorator class to perform validation on a team name
# The team names passed as arguments are checked that they are the
# right class.
# Optionally, if the is_playing flag is set on the decorator
# then a further check is made to ensure that the team is actually
# playing in gthe match

class validate_team(object):

    def __init__(self, is_playing=False):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.is_playing = is_playing

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        def wrapped_f(wrapped_self, *args, **kwargs):
               # check that the arg is of the correct type Team
               for arg in args:
                     if type(arg).__name__ != 'Team':
                           raise Exception("Team needs to be type Team")

                     # if the decorator sets the is_playing flag then check
                     # that the arg is either the home or away team	
                     if(self.is_playing):
                           if wrapped_self.home_team.name!=arg.name  and wrapped_self.away_team.name!=arg.name:
                                    raise Exception("Team is not playing!")

               f(wrapped_self, *args, **kwargs)
       	return wrapped_f


