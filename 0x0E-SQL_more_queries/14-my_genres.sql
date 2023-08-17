-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_shows.name FROM tv_shows, tv_show_genres, tv_genres WHERE tv_genres.id = tv_show_genres.genre_id and tv_show_genres.show_id = tv_genres.id and
tv_shows.title = "Dexter" ORDER BY tv_shows.name ASC;
