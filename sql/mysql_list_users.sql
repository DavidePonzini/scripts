SELECT
    host,
    user,
    account_locked,
    CASE WHEN authentication_string = '$A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED' THEN '[invalid]'
        WHEN authentication_string = '' THEN '[not set]'
        ELSE '[set]' END as password
FROM
    mysql.user
;




