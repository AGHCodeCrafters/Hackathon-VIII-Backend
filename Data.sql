USE Magazyn;

INSERT INTO employees(name, bezoski) VALUES('Bartosz', 0), ('Kamil', 0), ('Dariusz', 0), ('Jakub', 0);

INSERT INTO tasks(item_id, employee_id, destination_location, type, status, bezoski_value) VALUES 
(1, 1, 'A-1', 'get', 'IN_PROGRESS', 57),
(2, 1, 'B-2', 'get', 'IN_PROGRESS', 95),
(3, 1, 'C-3', 'get', 'IN_PROGRESS', 120),
(4, 1, 'D-4', 'get', 'IN_PROGRESS', 48),
(5, 1, 'A-5', 'put', 'IN_PROGRESS', 284),
(6, 1, 'B-6', 'put', 'IN_PROGRESS', 193),
(7, 1, 'C-7', 'put', 'IN_PROGRESS', 36),
(8, 1, 'D-8', 'put', 'IN_PROGRESS', 48),
(6, 1, 'F-10', 'put', 'IN_PROGRESS', 42),
(8, 1, 'F-8', 'put', 'IN_PROGRESS', 78),
(4, 2, 'A-9', 'put', 'IN_PROGRESS', 32),
(3, 2, 'C-4', 'put', 'IN_PROGRESS', 53),
(7, 2, 'E-7', 'put', 'IN_PROGRESS', 68),
(6, 2, 'F-9', 'put', 'IN_PROGRESS', 42),
(8, 2, 'A-1', 'put', 'IN_PROGRESS', 87),
(4, 2, 'D-4', 'put', 'IN_PROGRESS', 32),
(1, 2, 'F-6', 'put', 'IN_PROGRESS', 47),
(4, 2, 'C-7', 'put', 'IN_PROGRESS', 43),
(3, 2, 'A-9', 'put', 'IN_PROGRESS', 47),
(4, 2, 'B-10', 'put', 'IN_PROGRESS', 20)

INSERT INTO items(code, location) VALUES
('100', 'A-1'),
('200', 'B-2'),
('300', 'C-3'),
('400', 'D-4'),
('500', 'A-5'),
('600', 'B-6'),
('700', 'C-7'),
('800', 'D-8')

SELECT * FROM tasks
SELECT * FROM employees

UPDATE employees SET bezoski = 0
UPDATE tasks SET status = 'IN_PROGRESS'