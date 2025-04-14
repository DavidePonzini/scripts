SELECT
	constraint_schema,
	table_catalog,
	table_schema,
	constraint_type,
	table_name,
	constraint_name

FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE
	constraint_schema <> 'pg_catalog'
ORDER BY
	1, 2, 3, 4 DESC, 5, 6
;
