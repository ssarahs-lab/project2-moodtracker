DROP TABLE IF EXISTS moods_diet_sleep;
DROP TABLE IF EXISTS user_profiles;
DROP TABLE IF EXISTS diet;
DROP TABLE IF EXISTS moods;


CREATE TABLE user_profiles (
user_id SERIAL PRIMARY KEY,
username VARCHAR(255),
email VARCHAR(255),
password_hash VARCHAR(255)
)

CREATE TABLE moods_diet_sleep (
id SERIAL PRIMARY KEY,
mood_rating INTEGER,
sleep_rating INTEGER,
diet_rating INTEGER
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
INSERT into moods_diet_sleep (id, mood_rating, sleep_rating, diet_rating) VALUES(1,5, 6, 4);