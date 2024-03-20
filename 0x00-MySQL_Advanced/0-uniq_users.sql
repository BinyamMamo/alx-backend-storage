-- Generate a list of unique users
CREATE TABLE IF NOT EXISTS `users` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT FULL UNIQUE,
    name VARCHAR(255)
);
