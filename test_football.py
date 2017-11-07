

from football import Match, Team

t1=Team("Rovers")
t2=Team("Fulham")

m = Match(t1,t2)

m.match_status()
m.score()
m.goal_scored_by(t1)
m.start()
m.goal_scored_by(t1)
m.goal_scored_by(t1)
m.match_status()
m.score()
m.stop()
m.match_status()
m.score()

m.goal_scored_by(t1)
