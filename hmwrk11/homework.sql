SELECT name, breed, weight
FROM Dogs;
SELECT *
FROM Dogs
WHERE weight > 25;
SELECT name, email
FROM Owners
WHERE city = 'Kyiv';
SELECT name, birth_year
FROM Dogs
WHERE breed = 'mixed';
SELECT reason, visit_date, price
FROM Visits
ORDER BY price DESC
LIMIT 5;