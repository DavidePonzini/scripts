SELECT
	table_schema AS schema,
	table_name as table,
	table_type as type
FROM
	information_schema.tables
WHERE
	table_schema <> 'pg_catalog'
	AND table_schema <> 'information_schema'
ORDER BY
	table_schema,
	table_name

