-- CREATE TABLE artist (
--     id serial PRIMARY KEY,
--     name VARCHAR
-- );

-- CREATE TABLE album (
--     id serial PRIMARY KEY,
--     name VARCHAR,
--     release INTEGER,
--     artist_id INTEGER REFERENCES artist (id)
-- );

-- CREATE TABLE song (
--     id serial PRIMARY KEY,
--     name varchar,
--     duration INTEGER,
--     album_id INTEGER REFERENCES album (id),
--     artist_id INTEGER REFERENCES artist (id)
-- );

-- INSERT INTO artist (id , name) VALUES 
--     (DEFAULT, 'Bob Dylan'),
--     (DEFAULT, 'The Beatles'),
--     (DEFAULT, 'The Rolling Stones'),
--     (DEFAULT, 'Led Zepplin');


INSERT INTO artist (id , name , release , artist_id) VALUES 
    (DEFAULT, 'Highway 61' , 1965 , 1),
    (DEFAULT, 'Blonde on Blonde' , 1966 , 1),
    (DEFAULT, 'Another Side of Bob Dylan' , 1964 , 1),
    (DEFAULT, 'A Hard Days Night' , 1964 , 2),
    (DEFAULT, 'Help!' , 1965 , 2),
    (DEFAULT, 'Rubber Soul' , 1966 , 2),
    (DEFAULT, 'Sgt Peppers Lonely Hearts Album' , 1966 , 2),
    (DEFAULT, 'The White Album' , 1967 , 2),
    (DEFAULT, 'Abbey Road' , 1968 , 2),
    (DEFAULT, 'Let It Be' , 1969 , 2),
    (DEFAULT, 'Led Zepplin I' , 1968 , 4),
    (DEFAULT, 'Led Zepplin II' , 1970 , 4),
    (DEFAULT, 'Led Zepplin III' , 1973 , 4),
    (DEFAULT, 'Led Zepplin IV' , 1975 , 4),
    (DEFAULT, 'Physical Graffitti' , 1978 , 4),
    (DEFAULT, 'Led Zepplin VI' , 1968 , 4),
    (DEFAULT, 'The Rolling Stones' , 1964 , 3),
    (DEFAULT, 'The Rolling Stones N0. 2' , 1965 , 3),
    (DEFAULT, 'Out of Our Heads' , 1965 , 3),
    (DEFAULT, 'Aftermath' , 1966 , 3);

INSERT INTO song (id , name , duration , album_id , artist_id) VALUES
    (DEFAULT, 'Like a Rolling Stone' , 6 , 1 , 1),
    (DEFAULT, 'Queen Jane Approximately' , 5 , 1 , 1),
    (DEFAULT, 'It Takes a Lot To Cry, It Takes a Train To Laugh' , 6 , 1 , 1),
    (DEFAULT, 'Just Like a Woman' , 6 , 2 , 1),
    (DEFAULT, 'I Want You' , 5 , 2 , 1),
    (DEFAULT, 'Sadeyed Lady of The Lowlands' , 11 , 2 , 1),
    (DEFAULT, 'Fourth Time Around' , 4 , 2 , 1),
    (DEFAULT, 'A Hard Days Night' , 3 , 4 , 2),
    (DEFAULT, 'I Should''ve Known Better' , 2 , 4 , 2),
    (DEFAULT, 'You Can''t Do That' , 2 , 4 , 2),
    (DEFAULT, 'Happy Just To Dance With You' , 2 , 4 , 2),
    (DEFAULT, 'Help!' , 2 , 5 , 2),
    (DEFAULT, 'I Need You' , 4 , 5 , 2),
    (DEFAULT, 'Dizzy Miss Lizzy' , 3 , 5 , 2),
    (DEFAULT, 'You''ve Got To Hide Your Love Away' , 4 , 5 , 2);




    

-- 1
SELECT song.name, artist.name 
    FROM song 
    INNER JOIN artist ON song.artist_id = artist.id AND artist.name = 'Bob Dylan';

-- 2
SELECT artist.name, album.name 
    FROM album 
    INNER JOIN artist ON album.artist_id = artist.id AND artist.name = 'Bob Dylan';

-- 3

SELECT MAX(song.duration)
    FROM song; 

-- 4
SELECT album.name, album.release
    FROM album
    WHERE album.release >= 1960 AND album.release <= 1969;

-- 5
SELECT album.name, album.release
    FROM album
    WHERE album.release >= 1970 AND album.release <= 1980;

-- 6
SELECT *
FROM artist
JOIN album ON artist.id = album.artist_id
WHERE
	album.release = (
		SELECT
			max(album.release)
		FROM
			album
		WHERE
			album.artist_id = artist.id
	);

-- 7
SELECT album.name, SUM(song.duration)
    FROM album, song
    WHERE album.id = song.album_id
    GROUP BY album.name;

-- 8
SELECT album.name, SUM(song.duration)
    FROM album, song
    WHERE album.id = song.album_id
    GROUP BY album.name LIMIT 1;

-- 9
SELECT artist.name , COUNT(album.name)
FROM artist
LEFT OUTER JOIN album ON artist.id = album.artist_id
GROUP BY artist.id
LIMIT 5;

-- 10
SELECT artist.name, song.name 
FROM artist 
INNER JOIN song ON artist.id = song.artist_id AND artist.name = 'The Beatles';