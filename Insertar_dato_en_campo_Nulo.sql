DROP PROCEDURE setcero;

SET @tabla = 'proveedores'; -- define la tabla
SET @defaults = '\'Sin Datos\''; -- lo que se quiera insertar en el campo nulo

DELIMITER $$
CREATE PROCEDURE setcero ()
BEGIN 
DECLARE contador INT DEFAULT 1; -- esta vez usamos contador
	SET @max_contador = (SELECT COUNT(*)
    FROM information_schema.columns
    WHERE table_name = @tabla); -- inicializamos el limite maximo del contador como la cantidad de columnas de la tabla
SET SESSION group_concat_max_len = 100000000;
WHILE contador <= @max_contador DO -- inicializamos contador
	SET @sql = CONCAT(
	'UPDATE ', @tabla, 
	' SET ', (SELECT column_name 
			  FROM information_schema.columns 
			  WHERE table_name = @tabla 
				AND ordinal_position = contador), 
	' = ',@defaults,' WHERE ', -- basicamente decimos que los registros vacios sean igual al valor deseado cuando...
	(SELECT column_name 
	 FROM information_schema.columns 
	 WHERE table_name = @tabla 
	   AND ordinal_position = contador), ' IS NULL;'
	); -- la columna tenga registros vacios
	SET contador = contador + 1; -- avanzo mi contador para el proximo loop
	PREPARE stmt FROM @sql; -- preparo sentencia
	EXECUTE stmt; -- ejecuto sentencia
	DEALLOCATE PREPARE stmt; -- elimino sentencia
END WHILE; -- termino el loop
END $$
DELIMITER ;

CALL setcero; -- ejecuto