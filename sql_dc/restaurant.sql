CREATE TABLE restaurant (
    id SERIAL NOT NULL PRIMARY KEY,
    name varchar,
    distance float,
    stars varchar,
    category varchar,
    favourite_dish varchar,
    does_takeout varchar,
    last_visit varchar
);


INSERT INTO restaurant (id,name,distance , stars, category, favourite_dish, does_takeout,last_visit) VALUES 
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

SELECT * FROM restaurant;

-- 1
SELECT * FROM restaurant
WHERE stars = '5/5';

-- 2
SELECT favourite_dish FROM restaurant
WHERE stars = '5/5';

-- 3
SELECT name FROM restaurant
WHERE name = 'Moon Tower';

-- 4
SELECT * FROM restaurant
WHERE category = 'BBQ';

-- 5
SELECT * FROM restaurant
WHERE does_takeout = 'Yes';

-- 6
SELECT * FROM restaurant
WHERE does_takeout = 'Yes' AND category = 'BBQ';

-- 7
SELECT * FROM restaurant
WHERE distance < 2;

-- 8
SELECT * FROM restaurant
WHERE last_visit <> 'last week';

-- 9
SELECT * FROM restaurant
WHERE last_visit <> 'last week' AND stars = '5/5';