CREATE DATABASE Tourney;

use Tourney;

CREATE TABLE Players (
	TeamID int NOT NULL DEFAULT 0 ,
    PlayerID int NOT NULL DEFAULT 0 ,
	PlayerFirstName nvarchar (30) NULL , 
    PlayerLastName nvarchar (30) NULL 
);

CREATE TABLE Address (
    PlayerID int NOT NULL DEFAULT 0 ,
    PlayerAddress nvarchar (30) NULL ,
    PlayerCity nvarchar (30) NULL ,
    PlayerState nvarchar (2) NULL ,
    PlayerZip int DEFAULT 00000 
);

CREATE TABLE Score (
	GameID int NOT NULL ,
    PlayerID int NOT NULL ,
    PlayerScore int DEFAULT 0 
);

CREATE TABLE Teams (
	TeamID int NOT NULL ,
	TeamName nvarchar (25) NULL ,
    CoachFirstName nvarchar (30) NULL ,
	CoachLastName nvarchar (30) NULL 
);

CREATE TABLE Tournaments (
	TourneyID int NOT NULL ,
    TourneyDate nvarchar (10) NULL ,
	TourneyLocation nvarchar (30) NULL
);

CREATE TABLE TourneyMatches (
	GameID int NOT NULL ,
    TourneyID int NOT NULL ,
	HomeTeam nvarchar (25) NULL ,
    AwayTeam nvarchar (25) NULL ,
    WinningTeam nvarchar (25) NULL 
);

/* Use SQL Data Import Wizard to load data to tourney DB */

/* Primary Key Declaration*/

ALTER TABLE Players ADD 
	CONSTRAINT Players_PK PRIMARY KEY   
	(
		PlayerID
	)  ;
    
ALTER TABLE Address ADD 
	CONSTRAINT Address_PK PRIMARY KEY   
	(
		PlayerAddress,
        PlayerID
	)  ;

ALTER TABLE Score ADD 
	CONSTRAINT Score_PK PRIMARY KEY   
	(
		GameID,
        PlayerID
	)  ;

ALTER TABLE Teams ADD 
	CONSTRAINT Teams_PK PRIMARY KEY   
	(
		TeamID
	)  ;

ALTER TABLE Tournaments ADD 
	CONSTRAINT Tournaments_PK PRIMARY KEY   
	(
		TourneyID
	)  ;

ALTER TABLE TourneyMatches ADD 
	CONSTRAINT TourneyMatches_PK PRIMARY KEY   
	(
		GameID,
        TourneyID
	)  ;

/* Foreign Key Declaration*/

ALTER TABLE Players ADD 
	CONSTRAINT Players_FK00 FOREIGN KEY 
	(
		TeamID
	) REFERENCES Teams (
		TeamID
	);

ALTER TABLE Address ADD 
	CONSTRAINT Address_FK00 FOREIGN KEY 
	(
		PlayerID
	) REFERENCES Players (
		PlayerID
	);

ALTER TABLE Score ADD 
	CONSTRAINT Score_FK00 FOREIGN KEY 
	(
		PlayerID
	) REFERENCES Players (
		PlayerID
	);

ALTER TABLE TourneyMatches ADD 
	CONSTRAINT TourneyMatches_FK00 FOREIGN KEY 
	(
		TourneyID
	) REFERENCES Tournaments (
		TourneyID
	);

