select players.PlayerFirstName, players.PlayerLastName ,max(score.PlayerScore)
from score inner join players on players.PlayerID = score.PlayerID
group by score.PlayerID
