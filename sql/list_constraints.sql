SELECT constraint_schema, constraint_name, table_catalog, table_schema, table_name, constraint_type

FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE
	constraint_schema <> 'pg_catalog'
;
