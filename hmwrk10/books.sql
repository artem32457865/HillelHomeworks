CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER,
    price REAL
);

INSERT INTO books (title, author, publication_year, price)
VALUES
    ('Кобзар', 'Тарас Шевченко', 1840, 350.50),
    ('1984', 'George Orwell', 1949, 420.00),
    ('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 1997, 550.75),
    ('Місто', 'Валер''ян Підмогильний', 1928, 310.00);

UPDATE books
SET price = 600.00
WHERE id = 3;

DELETE FROM books
WHERE id = 2;