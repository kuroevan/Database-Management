select tournaments.TourneyID, tournaments.TourneyLocation
from tournaments 
where tournaments.TourneyID not in (Select tourneymatches.TourneyID from tourneymatches group by tourneymatches.TourneyID)