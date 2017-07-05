# roles/database/files/dump.sql
CREATE TABLE IF NOT EXISTS demo1 (
  message varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO demo1 (message) VALUES('Hello World!');
