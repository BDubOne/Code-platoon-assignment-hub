SELECT count(*), 
blogusers.first_name, 
blogusers.last_name 
FROM blogusers 
JOIN posts ON posts.user_id = blogusers.id
GROUP BY blogusers.last_name, 
blogusers.first_name 
ORDER BY count(*) DESC
LIMIT 1;