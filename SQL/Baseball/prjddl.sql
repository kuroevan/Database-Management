CREATE DATABASE BaseballTest;

use BaseballTest;

CREATE TABLE Baseball (
Team nvarchar (25) NULL ,
Player nvarchar (25) NULL ,
Salary int NOT NULL ,
Position text (25) NULL 
);

select *
from baseball