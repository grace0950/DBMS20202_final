CREATE TABLE movie(
	movie_name VARCHAR,
	movie_day VARCHAR NOT NULL,
	theater VARCHAR NOT NULL,
	t_location VARCHAR  NOT NULL,
	movie_time VARCHAR NOT NULL,
	PRIMARY KEY(movie_name,theater,movie_day,movie_time)
);
CREATE TABLE acts(
	m_name VARCHAR NOT NULL,
	actor_name VARCHAR NOT NULL,
	PRIMARY KEY(m_name,actor_name)
);
CREATE TABLE actor(
	actor_name VARCHAR,
	actor_id VARCHAR NOT NULL,
	sex VARCHAR NOT NULL,
	PRIMARY KEY(actor_id)
);
CREATE TABLE movie_type(
	movie_name VARCHAR NOT NULL,
	type_name VARCHAR NOT NULL,
	url VARCHAR NOT NUll,
	info VARCHAR NOT NULL,
	PRIMARY KEY(movie_name)
);
CREATE TABLE seat(
	m_name VARCHAR NOT NULL,
	t_name VARCHAR NOT NULL,
	day VARCHAR NOT NULL,
	s_time VARCHAR NOT NULL,
	s_column VARCHAR NOT NULL,
	s_row VARCHAR NOT NULL,
	has_someone bool NOT NULL,
	PRIMARY KEY(m_name,t_name,day,s_time,s_column,s_row)    
);
CREATE TABLE customer(
	c_name VARCHAR NOT NULL,
	c_phone VARCHAR NOT NULL,
	c_id VARCHAR NOT NULL,
	c_list int NOT NULL,
	m_name VARCHAR NOT NULL,
	m_theater VARCHAR NOT NULL,
	m_day VARCHAR NOT NULL,
	m_time VARCHAR NOT NULL,
	m_row VARCHAR NOT NULL,
	m_column VARCHAR NOT NULL,
	PRIMARY KEY(c_list)
);

## 0627-0704 ##
COPY acts FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0627-0704csvs/acts_data0627-0704.csv' DELIMITER ',' CSV;
COPY actor FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0627-0704csvs/actor_data0627-0704.csv' DELIMITER ',' CSV;
COPY movie FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0627-0704csvs/display_data0627-0704.csv' DELIMITER ',' CSV;
COPY movie_type FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0627-0704csvs/type_data0627-0704.csv' DELIMITER ',' CSV;
COPY seat FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0627-0704csvs/seat_data0627-0704.csv' DELIMITER ',' CSV;

## 0620-0627 ##
COPY acts FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0620-0627csvs/acts_data0620-0627.csv' DELIMITER ',' CSV;
COPY actor FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0620-0627csvs/actor_data0620-0627.csv' DELIMITER ',' CSV;
COPY movie FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0620-0627csvs/display_data0620-0627.csv' DELIMITER ',' CSV;
COPY movie_type FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0620-0627csvs/type_data0620-0627.csv' DELIMITER ',' CSV;
COPY seat FROM '/home/absnormal/大學/DBMS_2020/DBMS_Project1/0620-0627csvs/seat_data0620-0627.csv' DELIMITER ',' CSV;

DROP TABLE actor CASCADE;
DROP TABLE acts CASCADE;
DROP TABLE movie CASCADE;
DROP TABLE movie_type CASCADE;
DROP TABLE seat CASCADE;
DROP TABLE customer CASCADE;
