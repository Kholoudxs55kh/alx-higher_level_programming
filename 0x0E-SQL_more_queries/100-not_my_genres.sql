-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres LEFT JOIN (SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows WHERE tv_genres.id = tv_show_genres.genre_id and
tv_shows.id = tv_show_genres.show_id and tv_shows.title = "Dexter") tile ON tv_genres.name = tile.name WHERE tile.name IS NULL ORDER BY tv_genres.name ASC;
