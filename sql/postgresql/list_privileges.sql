SELECT *
FROM information_schema.role_table_grants
ORDER BY privilege_type, table_catalog, table_schema, table_name, grantee, grantor;
