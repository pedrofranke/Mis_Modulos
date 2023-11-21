SET @base = 'depython'; -- base de datos utilizada

DROP PROCEDURE IF EXISTS textoafecha;

DELIMITER $$
CREATE PROCEDURE textoafecha() -- inicia el procedimiento
BEGIN
	DECLARE var_final INT DEFAULT 0; -- declara variables
    DECLARE nomtabla VARCHAR(50);
    DECLARE nomcol VARCHAR(50);
	DECLARE cursor1 CURSOR FOR SELECT DISTINCT table_name, column_name FROM information_schema.columns WHERE Table_schema = @base;
-- crea cursor que basicamente toma datos de los registros de sistema, devolviendo el nombre de cada tabla y columa de la base de datos
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET var_final = 1; -- define variable para finalizar el loop
    
    OPEN cursor1; -- abre cursor
    bucle: LOOP -- inicia bucle
		FETCH cursor1 INTO nomtabla, nomcol; -- busca siguiente registro
        IF var_final = 1 THEN -- clausula de finalizacion
			LEAVE bucle;
		END IF;
        IF (nomcol LIKE '%Fecha%' OR nomcol LIKE '%Date%') = 1 THEN 
-- si la columna tiene en el nombre "Date" o "Fecha" ejecuta el codigo
			SET @sql = CONCAT('ALTER TABLE ', nomtabla,' CHANGE ',nomcol,' ', nomcol,' DATE;');
-- genera sentencia para cambiar el tipo de dato a date
            PREPARE stmt FROM @sql; -- prepara sentencia
            EXECUTE stmt; -- ejecuta sentencia
            DEALLOCATE PREPARE stmt; -- elimina sentencia
		END IF;
	END LOOP bucle; -- sigue a la siguiente combinacion tabla/columna
    CLOSE cursor1; -- cierra cursor
END $$
DELIMITER ;

CALL textoafecha; -- ejecuta funcion
