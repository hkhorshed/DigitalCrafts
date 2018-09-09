CREATE TABLE restaurant2 (
    id SERIAL NOT NULL PRIMARY KEY,
    name varchar,
    distance float,
    stars varchar,
    category varchar,
    favourite_dish varchar,
    does_takeout varchar,
    last_visit varchar
);


INSERT INTO restaurant2 (id,name,distance , stars, category, favourite_dish, does_takeout,last_visit) VALUES 
    (DEFAULT, 'Mcdonalds' , 5.3 , '5/5' , 'Junk' , 'Hot n Spicy' , 'Yes' , 'last week' ),
    (DEFAULT, 'Taco Bell' , 12 , '5/5' , 'Junk' , 'Tacos' , 'Yes' , 'this week'  ),
    (DEFAULT, 'KFC' , 7 , '3/5' , 'Junk' , 'Fried Chicken' , 'Yes' , '2011'  ),
    (DEFAULT, 'Waffle House' , 1.7 , '4.5/5' , 'Diner' , 'Hot n Spicy' , 'Yes' , 'lsat year' ),
    (DEFAULT, 'Moon Tower' , 1.4 , '5/5' , 'Junk' , 'Hot n Spicy' , 'Yes' , 'last week' ),
    (DEFAULT, 'Taco Bell' , 1 , '5/5' , 'Junk' , 'Tacos' , 'No' , 'this week'  ),
    (DEFAULT, 'KFC' , 0.1 , '3/5' , 'BBQ' , 'Fried Chicken' , 'Yes' , '2011'  ),
    (DEFAULT, 'Waffle House' , 4.3 , '4.5/5' , 'Diner' , 'Hot n Spicy' , 'Yes' , 'lsat year' ),
    (DEFAULT, 'Mcdonalds' , 1 , '5/5' , 'Junk' , 'Hot n Spicy' , 'Yes' , 'last week' ),
    (DEFAULT, 'Taco Bell' , 12 , '5/5' , 'BBQ' , 'Tacos' , 'No' , 'this week'  ),
    (DEFAULT, 'KFC' , 7 , '3/5' , 'BBQ' , 'Fried Chicken' , 'Yes' , '2011'  ),
    (DEFAULT, 'Waffle House' , 9 , '4.5/5' , 'Diner' , 'Hot n Spicy' , 'Yes' , 'lsat year' );

SELECT * FROM restaurant2;

-- 1
SELECT * FROM restaurant2
ORDER BY distance ASC;

-- 2
SELECT * FROM restaurant2
ORDER BY distance ASC
LIMIT 2;

-- 3
SELECT * FROM restaurant2
ORDER BY stars DESC
LIMIT 2;

-- 4
SELECT * FROM restaurant2
WHERE distance < 2
ORDER BY stars DESC
LIMIT 2;

-- 5
SELECT COUNT(*) FROM restaurant2;


-- 6
SELECT category, COUNT(*)
FROM restaurant2
GROUP BY category;

-- 7
-- my stars was a string so this returns an error.
SELECT AVG(stars), COUNT(*)
FROM restaurant2
GROUP BY category;

-- 8
SELECT MAX(stars), COUNT(*)
FROM restaurant2
GROUP BY category;

