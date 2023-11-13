
DROP TABLE  IF EXISTS blogUsers CASCADE;
CREATE TABLE blogUsers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR NOT NULL
);

DROP TABLE IF EXISTS posts CASCADE;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES blogUsers(id),
    title VARCHAR NOT NULL,
    text TEXT
);

DROP TABLE IF EXISTS comments CASCADE;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    text TEXT,
    user_id INTEGER REFERENCES blogUsers(id),
    post_id INTEGER REFERENCES posts(id),
    parent_comment_id INTEGER REFERENCES comments(id)
    CHECK (--optional
    (post_id IS NOT NULL AND parent_comment_id IS NULL) OR
    (post_id IS NULL AND parent_comment_id IS NOT NULL)
    )
);
    








