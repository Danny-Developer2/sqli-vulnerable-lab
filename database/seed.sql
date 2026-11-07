-- SQLi Vulnerable Lab - datos de ejemplo ficticios.
-- Las contraseñas están en texto plano SOLO para el laboratorio.

USE sqli_lab;

INSERT INTO roles (name, description) VALUES
  ('admin',   'Administrador del laboratorio'),
  ('user',    'Usuario estándar'),
  ('auditor', 'Auditor de actividad');

INSERT INTO users (username, password, email, role) VALUES
  ('admin',   'Password123!', 'admin@lab.local',   'admin'),
  ('jdoe',    'Password123!', 'jdoe@lab.local',    'user'),
  ('asmith',  'Password123!', 'asmith@lab.local',  'user'),
  ('mbrown',  'Password123!', 'mbrown@lab.local',  'auditor'),
  ('lgarcia', 'Password123!', 'lgarcia@lab.local', 'user'),
  ('kwilson', 'Password123!', 'kwilson@lab.local', 'user'),
  ('nperez',  'Password123!', 'nperez@lab.local',  'user'),
  ('slee',    'Password123!', 'slee@lab.local',    'user');

INSERT INTO products (name, price, stock) VALUES
  ('Laptop Educativa 14',  899.99, 25),
  ('Monitor 24 Pulgadas',  179.50, 40),
  ('Teclado Mecánico',      69.99, 60),
  ('Ratón Inalámbrico',    29.99, 80),
  ('Webcam HD 1080p',       49.90, 35),
  ('Disco SSD 1TB',         99.00, 20);

INSERT INTO customers (name, email, phone, city) VALUES
  ('Cliente Ficticio Uno',   'uno@clientes.local',   '+34 000 000 001', 'Madrid'),
  ('Cliente Ficticio Dos',   'dos@clientes.local',   '+34 000 000 002', 'Barcelona'),
  ('Cliente Ficticio Tres',  'tres@clientes.local',  '+34 000 000 003', 'Valencia'),
  ('Cliente Ficticio Cuatro','cuatro@clientes.local','+34 000 000 004', 'Sevilla'),
  ('Cliente Ficticio Cinco', 'cinco@clientes.local', '+34 000 000 005', 'Bilbao'),
  ('Cliente Ficticio Seis',  'seis@clientes.local',  '+34 000 000 006', 'A Coruña'),
  ('Cliente Ficticio Siete', 'siete@clientes.local', '+34 000 000 007', 'Granada');

INSERT INTO activity_logs (user_id, action) VALUES
  ((SELECT id FROM users WHERE username = 'admin'),   'login_success'),
  ((SELECT id FROM users WHERE username = 'jdoe'),    'login_success'),
  ((SELECT id FROM users WHERE username = 'asmith'),  'view_dashboard'),
  ((SELECT id FROM users WHERE username = 'mbrown'),  'export_logs'),
  ((SELECT id FROM users WHERE username = 'lgarcia'), 'login_failed'),
  ((SELECT id FROM users WHERE username = 'kwilson'), 'login_success'),
  ((SELECT id FROM users WHERE username = 'nperez'),  'view_products'),
  ((SELECT id FROM users WHERE username = 'slee'),    'login_failed');
