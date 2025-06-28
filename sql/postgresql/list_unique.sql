SELECT
    kcu.table_schema AS schema_name,
    kcu.table_name,
    tc.constraint_type,
    array_agg(kcu.column_name ORDER BY kcu.ordinal_position) AS columns
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
 AND tc.constraint_schema = kcu.constraint_schema
WHERE tc.constraint_type IN ('UNIQUE', 'PRIMARY KEY')
  AND kcu.table_schema NOT IN ('pg_catalog', 'information_schema')
GROUP BY
    kcu.table_schema,
    kcu.table_name,
    kcu.constraint_name,
    tc.constraint_type;
