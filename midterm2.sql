Select players.PlayerFirstName, players.PlayerLastName, address.PlayerAddress, address.PlayerCity, 
	address.PlayerState, address.PlayerZip
from Players inner join address on players.PlayerID = address.PlayerID
group by address.PlayerZip