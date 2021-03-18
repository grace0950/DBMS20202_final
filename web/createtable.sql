CREATE TABLE movie(
	movie_name VARCHAR,
	movie_day VARCHAR NOT NULL,
	theater VARCHAR NOT NULL,
	t_location VARCHAR  NOT NULL,
	movie_time VARCHAR,
	PRIMARY KEY(movie_name,theater,movie_day,movie_time)
);
CREATE TABLE actor(
	actor_name VARCHAR,
	actor_id VARCHAR NOT NULL,
	sex VARCHAR not NULL,
	PRIMARY KEY(actor_id)
);

CREATE TABLE movie_type(
	movie_name VARCHAR NOT NULL,
	type_name VARCHAR NOT NULL,
	url VARCHAR NOT NUll,
	PRIMARY KEY(movie_name)
);

CREATE TABLE seat(
	t_name VARCHAR NOT NULL,
	s_row VARCHAR NOT NULL,
	s_column VARCHAR NOT NULL,
	has_someone bool NOT NULL,
	day VARCHAR NOT NULL,
	s_time VARCHAR NOT NULL,
	PRIMARY KEY(t_name,s_row,s_column)
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

