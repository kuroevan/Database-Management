select distinct(PlayerFirstName), players.PlayerLastName, score.PlayerScore
from players inner join score on players.PlayerID = score.PlayerID
order by score.PlayerScore desc limit 10