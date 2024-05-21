SELECT
    host,
    user,
    account_locked,
    CASE WHEN authentication_string = '$A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED' THEN '[invalid]'
        WHEN authentication_string = '' THEN '[not set]'
        ELSE '[set]' END as password,
    CONCAT_WS(',',
        CASE WHEN Select_priv = 'Y' THEN 'Select' ELSE NULL END,
        CASE WHEN Insert_priv = 'Y' THEN 'Insert' ELSE NULL END,
        CASE WHEN Update_priv = 'Y' THEN 'Update' ELSE NULL END,
        CASE WHEN Delete_priv = 'Y' THEN 'Delete' ELSE NULL END,
        CASE WHEN Create_priv = 'Y' THEN 'Create' ELSE NULL END,
        CASE WHEN Drop_priv = 'Y' THEN 'Drop' ELSE NULL END,
        CASE WHEN Reload_priv = 'Y' THEN 'Reload' ELSE NULL END,
        CASE WHEN Shutdown_priv = 'Y' THEN 'Shutdown' ELSE NULL END,
        CASE WHEN Process_priv = 'Y' THEN 'Process' ELSE NULL END,
        CASE WHEN File_priv = 'Y' THEN 'File' ELSE NULL END,
        CASE WHEN Grant_priv = 'Y' THEN 'Grant' ELSE NULL END,
        CASE WHEN References_priv = 'Y' THEN 'References' ELSE NULL END,
        CASE WHEN Index_priv = 'Y' THEN 'Index' ELSE NULL END,
        CASE WHEN Alter_priv = 'Y' THEN 'Alter' ELSE NULL END,
        CASE WHEN Show_db_priv = 'Y' THEN 'Show_db' ELSE NULL END,
        CASE WHEN Super_priv = 'Y' THEN 'Super' ELSE NULL END,
        CASE WHEN Create_tmp_table_priv = 'Y' THEN 'Create_tmp_table' ELSE NULL END,
        CASE WHEN Lock_tables_priv = 'Y' THEN 'Lock_tables' ELSE NULL END,
        CASE WHEN Execute_priv = 'Y' THEN 'Execute' ELSE NULL END,
        CASE WHEN Repl_slave_priv = 'Y' THEN 'Repl_slave' ELSE NULL END,
        CASE WHEN Repl_client_priv = 'Y' THEN 'Repl_client' ELSE NULL END,
        CASE WHEN Create_view_priv = 'Y' THEN 'Create_view' ELSE NULL END,
        CASE WHEN Show_view_priv = 'Y' THEN 'Show_view' ELSE NULL END,
        CASE WHEN Create_routine_priv = 'Y' THEN 'Create_routine' ELSE NULL END,
        CASE WHEN Alter_routine_priv = 'Y' THEN 'Alter_routine' ELSE NULL END,
        CASE WHEN Create_user_priv = 'Y' THEN 'Create_user' ELSE NULL END,
        CASE WHEN Event_priv = 'Y' THEN 'Event' ELSE NULL END,
        CASE WHEN Trigger_priv = 'Y' THEN 'Trigger' ELSE NULL END,
        CASE WHEN Create_tablespace_priv = 'Y' THEN 'Create_tablespace' ELSE NULL END,
        CASE WHEN Create_role_priv = 'Y' THEN 'Create_role' ELSE NULL END,
        CASE WHEN Drop_role_priv = 'Y' THEN 'Drop_role' ELSE NULL END
    ) AS privileges
FROM
    mysql.user
;




