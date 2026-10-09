CREATE DATABASE IF NOT EXISTS portal;
USE portal;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL,
  role VARCHAR(20) NOT NULL,
  flag VARCHAR(200)
);

INSERT INTO users (username, password, role, flag) VALUES
('admin', 'admin123', 'admin', 'NOVATECH{S3_ADMIN_DB_FLAG}'),
('employee', 'welcome1', 'user', NULL);