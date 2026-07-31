# SQL - Introduction

Introductory SQL scripts run against a MySQL server: creating and dropping
databases, creating and describing tables, and inserting, querying, updating,
deleting, and aggregating rows.

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | List all databases |
| `1-create_database_if_missing.sql` | Create `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Drop `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | List all tables of a database |
| `4-first_table.sql` | Create `first_table` (id, name) |
| `5-full_table.sql` | Show the full table description |
| `6-list_values.sql` | List all rows of `first_table` |
| `7-insert_value.sql` | Insert a row (89, "Best School") |
| `8-count_89.sql` | Count records with id = 89 |
| `9-full_creation.sql` | Create `second_table` and add rows |
| `10-top_score.sql` | List records ordered by score |
| `11-best_score.sql` | List records with score >= 10 |
| `12-no_cheating.sql` | Update Bob's score to 10 by name |
| `13-change_class.sql` | Delete records with score <= 5 |
| `14-average.sql` | Average score of all records |
| `15-groups.sql` | Count of records per score |
| `16-no_link.sql` | List named records by descending score |

## Usage

    cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

## Requirements

- MySQL 8.0
- All files end with a newline and start with a comment describing the task

## Author

ALU - Higher Level Programming
