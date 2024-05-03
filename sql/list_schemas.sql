SELECT
	schema_name,
	schema_owner
FROM
	information_schema.schemata
WHERE
	schema_name <> 'information_schema'
	AND schema_name <> 'pg_catalog'
	AND schema_name <> 'pg_toast'
;
