# SQL - More Queries

Scripts covering MySQL user management and privileges, table constraints
(NOT NULL, DEFAULT, UNIQUE, PRIMARY KEY, FOREIGN KEY), subqueries, and JOINs
across a states/cities schema and a TV shows database.

## Files

| File | Description |
|------|-------------|
| `0-privileges.sql` | List privileges of two users |
| `1-create_user.sql` | Create `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Create DB and a SELECT-only user |
| `3-force_name.sql` | `force_name` table with a NOT NULL name |
| `4-never_empty.sql` | `id_not_null` table with id defaulting to 1 |
| `5-unique_id.sql` | `unique_id` table with a unique id |
| `6-states.sql` | `states` table with an auto-increment PK |
| `7-cities.sql` | `cities` table with a foreign key to states |
| `8-cities_of_california_subquery.sql` | California cities via a subquery |
| `9-cities_by_state_join.sql` | Cities with their state via a JOIN |
| `10-genre_id_by_show.sql` | Shows with at least one genre |
| `11-genre_id_all_shows.sql` | All shows, NULL when no genre |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Number of shows per genre |
| `14-my_genres.sql` | Genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows and their genres, NULL when none |

## Requirements

- MySQL 8.0
- All files start with a comment and use uppercase SQL keywords

## Author

ALU - Higher Level Programming
