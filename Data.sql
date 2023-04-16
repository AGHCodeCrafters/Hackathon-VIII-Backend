USE Magazyn;

INSERT INTO employees(name, bezoski) VALUES('Bartosz', 0), ('Kamil', 0), ('Dariusz', 0), ('Jakub', 0);

INSERT INTO tasks(item_id, employee_id, destination_location, type, status) VALUES 
(123, 1, 'A-1', 'get', 'IN_PROGRESS'),
(345, 1, 'B-2', 'get', 'IN_PROGRESS'),
(678, 1, 'C-3', 'get', 'IN_PROGRESS'),
(910, 1, 'D-4', 'get', 'IN_PROGRESS'),
(111, 1, 'A-5', 'put', 'IN_PROGRESS'),
(131, 1, 'B-6', 'put', 'IN_PROGRESS'),
(151, 1, 'C-7', 'put', 'IN_PROGRESS'),
(171, 1, 'D-8', 'put', 'IN_PROGRESS')