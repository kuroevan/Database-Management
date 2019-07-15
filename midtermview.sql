CREATE VIEW V_REDROOSTER
As select tournaments.TourneyID, tournaments.TourneyLocation
from tournaments 
where tournaments.TourneyID in 
	( 	select tourneymatches.TourneyID
		from tourneymatches
		where tourneymatches.TourneyID = 1 OR tourneymatches.TourneyID = 8 OR tourneymatches.TourneyID = 15 )