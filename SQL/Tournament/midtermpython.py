import mysql.connector

cnx = mysql.connector.connect(user='root', password='*******',host='127.0.0.1',database='tourney')

cursor = cnx.cursor()

query = (" select tournaments.TourneyLocation from tournaments inner join tourneymatches on tournaments.TourneyID = tourneymatches.TourneyID group by tournaments.TourneyID ")

cursor.execute(query)

for (TourneyLocation) in cursor:
    print(TourneyLocation)

cursor.close()
cnx.close()
