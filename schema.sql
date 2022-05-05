DROP TABLE IF EXISTS moods_diet_sleep;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS diet;
DROP TABLE IF EXISTS moods;

CREATE TABLE users (
user_id SERIAL PRIMARY KEY,
username VARCHAR(255),
email VARCHAR(255),
password_hash VARCHAR(255)
);


CREATE TABLE moods_diet_sleep (
id INTEGER REFERENCES users(user_id),
name VARCHAR(255),
mood_rating INTEGER,
diet_rating INTEGER,
sleep_rating INTEGER, 
created_on TIMESTAMP NOT NULL DEFAULT NOW()
);



CREATE TABLE diet (
id INTEGER REFERENCES users(user_id),
diet_rating INTEGER,
food_items VARCHAR(255),
created_on TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE moods (
id INTEGER REFERENCES users(user_id),
mood_rating INTEGER,
emotions VARCHAR(255),
created_on TIMESTAMP NOT NULL DEFAULT NOW()
);


-- test seed


INSERT INTO users (email, username, password_hash) VALUES ('bob@example.com', 'BobExample', '$2b$12$TpvX8HcLDBfx.LOaNefsI.hBFars/nSddrxqcYDxb5VDQfughklBa');
INSERT INTO users (email, username, password_hash) VALUES ('sally@example.com', 'SallyExample', '$2b$12$d8iYmpmksEHmPqnCVDxGC.ZDID3KkS6jR8uH.fHewhOYm7UXJaJv6');
INSERT INTO users (email, username, password_hash) VALUES ('sarah@example.com', 'SarahS', '$2b$12$.Nom1w23KL6FV4oDbLNiYebldiJrH4PC3OiNLNt2mhj0jKKYymdh6' );
INSERT INTO users (email, username, password_hash) VALUES ('jenny@example.com', 'JennyJ', '$2b$12$G1jYAe3jBCJyQQ74HnvL0enP6KkWRfMUZRoLRpBbPLwlmN.qKru6a');
