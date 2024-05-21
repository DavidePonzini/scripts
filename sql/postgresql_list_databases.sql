SELECT
	datname,
	usename AS dba,
	datistemplate AS is_template,
	datallowconn AS allow_connection
FROM
	pg_database db
	JOIN pg_user u ON db.datdba = u.usesysid
;
