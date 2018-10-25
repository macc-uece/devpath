CREATE DATABASE devpath;
CREATE USER devpath;
GRANT ALL ON DATABASE devpath to "devpath";
ALTER USER devpath PASSWORD '123456';
ALTER USER devpath CREATEDB;

-- Use this commands if you need to restart the database
CREATE DATABASE devpath;
GRANT ALL ON DATABASE devpath to "devpath";