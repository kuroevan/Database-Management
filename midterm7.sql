select players.PlayerFirstName, players.PlayerLastName, (score.PlayerScore) as PlayerMaxScore, avg(score.PlayerScore) as PlayerMeanScore, max(score.PlayerScore) - avg(score.PlayerScore) AS DisplayScore
from score inner join players on players.PlayerID = score.PlayerID
group by score.PlayerID
having DisplayScore > 10