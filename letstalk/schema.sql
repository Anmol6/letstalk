CREATE DATABASE lData;
 
CREATE TABLE User(
userId INT NOT NULL AUTO_INCREMENT,
userName VARCHAR(100) NOT NULL,
password VARCHAR(40) NOT NULL,
PRIMARY KEY(userId)
 );

USE `lData`$$
CREATE PROCEDURE `spCreateUser` (
IN p_Username varchar(50),
IN p_Password varchar(50)
)
BEGIN

if ( select exists (select 1 from User where Username = p_username) ) THEN

    select 'Username Exists !!';

ELSE

insert into tblUser
(
    Username,
    Password
)
values
(
    p_Username,
    p_Password
);

END IF;

END$$

DELIMITER ;
