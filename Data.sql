USE Magazyn;

INSERT INTO employees(name, bezoski) VALUES('Bartosz', 0), ('Kamil', 0), ('Dariusz', 0), ('Jakub', 0);

INSERT INTO tasks(item_id, employee_id, destination_location, type, status, bezoski_value) VALUES 
(1, 1, 'A-1', 'get', 'IN_PROGRESS', 1),
(2, 1, 'B-2', 'get', 'IN_PROGRESS', 2),
(3, 1, 'C-3', 'get', 'IN_PROGRESS', 3),
(4, 1, 'D-4', 'get', 'IN_PROGRESS', 2),
(5, 1, 'A-5', 'put', 'IN_PROGRESS', 3),
(6, 1, 'B-6', 'put', 'IN_PROGRESS', 2),
(7, 1, 'C-7', 'put', 'IN_PROGRESS', 1),
(8, 1, 'D-8', 'put', 'IN_PROGRESS', 4)

INSERT INTO items(code, location) VALUES
('100', 'A-1'),
('200', 'B-2'),
('300', 'C-3'),
('400', 'D-4'),
('500', 'A-5'),
('600', 'B-6'),
('700', 'C-7'),
('800', 'D-8')