USE depython;
SET @base = 'depython';

DROP PROCEDURE IF EXISTS insertar_registros_nuevos;
DELIMITER $$
CREATE PROCEDURE insertar_registros_nuevos (IN tabla1 TEXT, IN tabla2 TEXT)
BEGIN
    DECLARE sdelete TEXT;
    DECLARE sadd TEXT;
	SET sdelete = CONCAT('DELETE FROM ',tabla2,' WHERE ',(SELECT column_name FROM information_schema.columns WHERE table_schema = @base AND table_name = tabla2 AND COLUMN_KEY = 'PRI'),' IN (SELECT ',(SELECT column_name FROM information_schema.columns WHERE table_schema = @base AND table_name = tabla1 AND COLUMN_KEY = 'PRI'),' FROM ',tabla1,');');
    SET @sdelete = sdelete;
    PREPARE stmt FROM @sdelete;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
    SET sadd = CONCAT('INSERT INTO ',tabla1,' SELECT * FROM ',tabla2,';');
    SET @sadd = sadd;
    PREPARE stmt FROM @sadd;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

CALL insertar_registros_nuevos('venta','venta_actualizado');