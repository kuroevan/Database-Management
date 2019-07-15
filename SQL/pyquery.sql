select tournaments.TourneyLocation
from tournaments inner join tourneymatches on tournaments.TourneyID = tourneymatches.TourneyID
group by tournaments.TourneyID