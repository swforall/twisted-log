/* Create table for logging */

create table if not exists Log (time REAL, hostname VARCHAR, pid INT, pname VARCHAR, exc_type VARCHAR, filename VARCHAR, line INT);