CREATE DATABASE devpath;
CREATE USER devpath;
GRANT ALL ON DATABASE devpath to "devpath";
ALTER USER devpath PASSWORD 'development';
ALTER USER devpath CREATEDB;