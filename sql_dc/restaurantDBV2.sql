-- CREATE TABLE restaurantHW (
--  id serial PRIMARY KEY,
--  name varchar,
--  address varchar,
--  category varchar
-- );

-- CREATE TABLE reviewerHW (
--  id serial PRIMARY KEY,
--  name varchar,
--  email varchar,
--  karma integer check (karma >= 0 and karma <= 7)
-- );

-- CREATE TABLE reviewHW (
--  id serial PRIMARY KEY,
--  title varchar,
--  review varchar,
--  stars integer check (stars >= 0 and stars <= 5),
--  reviewer_id integer REFERENCES reviewerHW (id),
--  restaurant_id integer REFERENCES restaurantHW (id)
-- );


-- INSERT INTO restaurantHW (id , name , address , category) VALUES 
--     (DEFAULT, 'Outback Steakhouse' , '15253 Southwest Fwy, Sugar Land, TX 77478' , 'Steakhouse' ),
--     (DEFAULT, 'Texas Land and Cattle' , '14010 U.S. 183 B, Austin, TX 78717' , 'Steakhouse'),
--     (DEFAULT, 'Chilis' , '15355 SW Frwy, Sugar Land, TX 77478' , 'Tex-Mex'),
--     (DEFAULT, 'Olive Garden' , '5005 Sweetwater Blvd, Sugar Land, TX 77479' , 'Italian'),
--     (DEFAULT, 'Maggiano''s Little Italy' , '2019 Post Oak Blvd, Houston, TX 77056' , 'Italian' ),
--     (DEFAULT, 'Grimaldi''s Pizzeria' , '12848 Queensbury Ln #101, Houston, TX 77024' , 'Italian'),
--     (DEFAULT, 'Moshi Sushi' , '5854 New Territory Blvd, Sugar Land, TX 77479' , 'Japanese'),
--     (DEFAULT, 'Fogo de Chao' , '8250 Westheimer Rd, Houston, TX 77063' , 'Steakhouse'),
--     (DEFAULT, 'Big 6' , '9907 S Texas 6 #500, Sugar Land, TX 77498' , 'BBQ'),
--     (DEFAULT, 'Taco Bell' , '1660 S Loop 35, Alvin, TX 77511' , 'Junk'),
--     (DEFAULT, 'Mcdonalds' , '9310 S Texas 6, Houston, TX 77083' , 'Junk'),
--     (DEFAULT, 'Waffle House' , '11240 Westheimer Rd, Houston, TX 77042' , 'Diner');

-- INSERT INTO reviewerHW (id,name, email, karma) VALUES 
--     (DEFAULT , 'Outback Steakhouse' , 'outbacksteakhouse@gmail.com' , 6 ),
--     (DEFAULT, 'Texas Land and Cattle' , 'txlandcattle@gmail.com' , 4),
--     (DEFAULT, 'Chilis' , 'chilis@yahoo.com' , 2),
--     (DEFAULT, 'Olive Garden' , 'og@outlook.com' , 2),
--     (DEFAULT, 'Maggiano''s Little Italy' , 'maggianos@houstonrestaurants.com' , 6 ),
--     (DEFAULT, 'Grimaldi''s Pizzeria' , 'grimaldis@gmail.com' , 6),
--     (DEFAULT, 'Moshi Sushi' , 'moshisushi@yahoo.com' , 7),
--     (DEFAULT, 'Fogo de Chao' , 'fogodechao@gmail.com' , 7),
--     (DEFAULT, 'Big 6' , NULL , 7),
--     (DEFAULT, 'Taco Bell' , 'tacobell@junk.com' , 5),
--     (DEFAULT, 'Mcdonalds' , 'mcdee@obesity.com, TX 77083' , 5),
--     (DEFAULT, 'Waffle House' , 'whdiner@yahoo.com' , 7);

-- INSERT INTO reviewHW (id, title, review, stars, reviewer_id, restaurant_id) VALUES 
--     (DEFAULT, 'Steakhouse Review' , 'Good' , 4 , 1 , 1 ),
--     (DEFAULT, 'Why Are They Leaving?' , 'Good' , 3, 2 , 2 ),
--     (DEFAULT, 'What Happened to Chili''s' , 'Trash' , 2 , 2 , 3 ),
--     (DEFAULT, 'When Italian Food Goes Wrong' , 'Bad' , 1 , 3 , 4 ),
--     (DEFAULT, 'The Best Pasta' , 'Amazing' , 5 , 3 , 5 ),
--     (DEFAULT, 'Good Grimaldi Pizza' , 'Great' , 5 , 3 , 6),
--     (DEFAULT, 'The Bests Ramen in Town' , 'Perfect' , 5 , 2 , 7),
--     (DEFAULT, 'Brazillian Steakhouse Worth Every Penny' , 'Perfect' , 5, 1 , 8 ),
--     (DEFAULT, 'This BBQ Truck is Better Than The Restaurants' , 'Good' , 4 , 1 , 9 ),
--     (DEFAULT, 'Who Cares What Happens in The Morning' , 'Bad' , 1, 10 , 10 ),
--     (DEFAULT, 'Join the See-Food Diet With Us' , 'Bad' , 1, 11 , 11),
--     (DEFAULT, 'Where do The Drunk People Go at Night?' , 'Great' , 5 , 12 , 12);


-- -- 1
-- SELECT restaurantHW.name , reviewHW.review 
-- FROM restaurantHW , reviewHW
-- LEFT OUTER JOIN reviewerHW
-- ON reviewHW.restaurant_id = reviewerHW.id
-- GROUP BY restaurantHW.name , reviewHW.review;

-- --  2
-- SELECT restaurantHW.id , restaurantHK.name
-- FROM restaurantHW , restaurantHK
-- LEFT OUTER JOIN reviewHW
-- ON restaurantHW.id = reviewHW.restaurant_id
-- GROUP BY restaurantHW.id ;


-- 3



-- 4


-- 5


-- 6


-- 7


-- 8


-- 9


-- 10


-- 11


-- 12



