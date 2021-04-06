use 4d;


CREATE TABLE IF NOT EXISTS user (
id INT NOT NULL AUTO_INCREMENT primary key,
user_name VARCHAR(32) NOT NULL
) ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS echo (
id INT NOT NULL AUTO_INCREMENT primary key,
user_id INT(16) NOT NULL,
longitude DOUBLE(12, 8) NOT NULL,
latigude DOUBLE(12, 8) NOT NULL,
altitude DOUBLE(12, 8) NOT NULL,
echo_space POINT,
echo_time Date NOT NULL,
echo_audio_id  INT(16) NOT NULL,
echo_audio BLOB NOT NULL,
INDEX echo_place (longitude, latigude, altitude)
) ENGINE=INNODB;