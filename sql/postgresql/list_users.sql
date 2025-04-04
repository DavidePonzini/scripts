SELECT
	u.usename AS "User",
	CONCAT_WS(', ',
		CASE WHEN r.rolsuper THEN 'Superuser' ELSE NULL END,
		CASE WHEN r.rolcreaterole THEN 'Create role' ELSE NULL END,
		CASE WHEN r.rolcreatedb THEN 'Create DB' ELSE NULL END,
		CASE WHEN r.rolreplication THEN 'Replication' ELSE NULL END,
		CASE WHEN r.rolbypassrls THEN 'Bypass RLS' ELSE NULL END) AS "Attributes",
	ARRAY(SELECT b.rolname
		FROM pg_catalog.pg_auth_members m
		JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid)
		WHERE m.member = r.oid) AS "Member of"
FROM
	pg_catalog.pg_user u
	JOIN pg_catalog.pg_roles r ON (u.usename = r.rolname)
ORDER BY 1;
