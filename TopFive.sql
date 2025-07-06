-- DataLemur problem: https://datalemur.com/questions/top-fans-rank--

WITH top_ten AS 
(
  SELECT 
    song_id,
    rank
  FROM
    global_song_rank
  WHERE
    rank<=10
),
artist_songs AS 
(
SELECT
  artists.artist_id,
  artists.artist_name,
  songs.song_id
FROM 
  artists 
JOIN 
  songs 
ON 
  artists.artist_id = songs.artist_id
)

SELECT 
  artist_songs.artist_name,
  RANK() OVER (ORDER BY COUNT(artist_songs.artist_id)) AS artist_rank
FROM
  artist_songs
JOIN 
  top_ten 
ON 
  artist_songs.song_id = top_ten.song_id
GROUP BY
  artist_songs.artist_name;
  