-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title FROM tv_shows LEFT JOIN (SELECT tv_shows.title FROM tv_genres, tv_show_genres, tv_shows WHERE tv_show_genres.genre_id = tv_genres.id
and tv_shows.id = tv_show_genres.show_id and tv_genres.name = "Comedy") tile ON tv_shows.title = tile.title WHERE tile.title IS NULL ORDER BY tv_shows.title ASC;
