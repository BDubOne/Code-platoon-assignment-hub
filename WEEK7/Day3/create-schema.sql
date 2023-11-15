
DROP TABLE IF EXISTS user_accounts CASCADE;
CREATE TABLE user_accounts(
    id SERIAL PRIMARY KEY,
    username VARCHAR,
    password VARCHAR,
    last_login_date TIMESTAMPTZ
);
DROP TABLE IF EXISTS user_profiles CASCADE;
CREATE TABLE user_profiles(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES user_accounts(id),
    profile_photo VARCHAR,
    about_me TEXT,
    personal_quote VARCHAR
);
DROP TABLE IF EXISTS posts CASCADE;
CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    content VARCHAR,
    profile_id INT REFERENCES user_profiles(id)
);
DROP TABLE IF EXISTS comments CASCADE;
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    content TEXT,
    profile_id INT REFERENCES user_profiles(id),
    post_id INTEGER REFERENCES posts(id)
);

DROP TABLE IF EXISTS reaction_types CASCADE;
CREATE TABLE reaction_types(
    id SERIAL PRIMARY KEY,
    type VARCHAR
);

DROP TABLE IF EXISTS post_reactions CASCADE;
CREATE TABLE post_reactions(
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id),
    reaction_id INTEGER REFERENCES reaction_types(id),
    profile_id INT REFERENCES user_profiles(id),
    UNIQUE (profile_id, post_id)
);


-- Generating random data for user_accounts table
INSERT INTO user_accounts (username, password, last_login_date)
VALUES
    ('user1', 'password1', '2023-11-15 08:00:00'),
    ('user2', 'password2', '2023-11-15 09:30:00'),
    ('user3', 'password3', '2023-11-15 10:45:00'),
    ('user4', 'password4', '2023-11-15 11:15:00'),
    ('user5', 'password5', '2023-11-15 12:30:00'),
    ('user6', 'password6', '2023-11-15 14:00:00');
  -- add more users as needed;

-- Generating random data for user_profiles table
INSERT INTO user_profiles (user_id, profile_photo, about_me, personal_quote)
VALUES
  (1, 'profile1.jpg', 'I love coding!', 'Live life to the fullest.'),
  (2, 'profile2.jpg', 'Foodie and traveler.', 'Stay positive.');
  -- add more profiles as needed;

-- Generating random data for posts table
INSERT INTO posts (content, profile_id)
VALUES
  ('This is my first post!', 1),
  ('Feeling excited about the weekend!', 2);
  -- add more posts as needed;

-- Generating random data for reaction_types table
INSERT INTO reaction_types (type)
VALUES
  ('LIKE'),
  ('LOVE'),
  ('WOW');
  -- add more reaction types as needed;

-- Generating random data for post_reactions table
INSERT INTO post_reactions (post_id, reaction_id, profile_id)
VALUES
  (1, 1, 2), -- User 2 likes Post 1
  (2, 2, 1); -- User 1 loves Post 2
  -- add more reactions as needed;