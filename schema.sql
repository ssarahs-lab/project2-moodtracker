DROP TABLE IF EXISTS moods_diet_sleep;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS diet;
DROP TABLE IF EXISTS moods;




CREATE TABLE moods_diet_sleep (
id SERIAL PRIMARY KEY,
name VARCHAR(255),
mood_rating INTEGER,
diet_rating INTEGER,
sleep_rating INTEGER, 
created_on TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE users (
user_id SERIAL PRIMARY KEY,
username VARCHAR(255),
email VARCHAR(255),
password_hash VARCHAR(255)
);

CREATE TABLE diet (
id SERIAL PRIMARY KEY,
diet_rating INTEGER,
food_items VARCHAR(255)
);

CREATE TABLE moods (
id SERIAL PRIMARY KEY,
mood_rating INTEGER,
emotions VARCHAR(255)
);


-- test seed
INSERT INTO moods_diet_sleep (name, mood_rating, sleep_rating, diet_rating) VALUES('Sarah',5, 6, 4);


INSERT INTO users (email, username, password_hash) VALUES ('bob@example.com', 'BobExample', '$2b$12$TpvX8HcLDBfx.LOaNefsI.hBFars/nSddrxqcYDxb5VDQfughklBa');
INSERT INTO users (email, username, password_hash) VALUES ('sally@example.com', 'SallyExample', '$2b$12$d8iYmpmksEHmPqnCVDxGC.ZDID3KkS6jR8uH.fHewhOYm7UXJaJv6');
INSERT INTO users (email, username, password_hash) VALUES ('sarah@example.com', 'SarahS', '$2b$12$.Nom1w23KL6FV4oDbLNiYebldiJrH4PC3OiNLNt2mhj0jKKYymdh6' );
INSERT INTO users (email, username, password_hash) VALUES ('jenny@example.com', 'JennyJ', '$2b$12$G1jYAe3jBCJyQQ74HnvL0enP6KkWRfMUZRoLRpBbPLwlmN.qKru6a');
