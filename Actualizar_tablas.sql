USE depython;
SET @base = 'depython';

DROP PROCEDURE IF EXISTS actualizar_tabla; -- elimina procedimiento si ya existe
DELIMITER $$ -- cambia delimiter para que los ; no corten el procedimiento
CREATE PROCEDURE actualizar_tabla (IN tabla1 TEXT, IN tabla2 TEXT) -- crea procedimiento con los dos inputs mencionados en README.md
BEGIN
    DECLARE sinicial TEXT; -- declaracion de variables
	DECLARE sset TEXT;
	DECLARE swhere TEXT;
    DECLARE sand TEXT;
	SET sinicial = CONCAT(' UPDATE ',tabla1,', ',tabla2,' SET '); -- inicia el UPDATE con los nombres de las tablas
    SET sset = (SELECT GROUP_CONCAT(tabla1,'.',column_name,' = ',tabla2,'.',column_name SEPARATOR ', ') FROM information_schema.columns WHERE table_schema = @base AND table_name = tabla1); 
-- genera una sentencia que iguala todos las las columnas de la tabla 1 a las columnas de la tabla 2
    SET swhere =  CONCAT(' WHERE ',tabla1,'.',(SELECT column_name FROM information_schema.columns WHERE table_schema = @base AND table_name = tabla1 AND COLUMN_KEY = 'PRI'),' = ',tabla2,'.',(SELECT column_name FROM information_schema.columns WHERE table_schema = @base AND table_name = tabla1 AND COLUMN_KEY = 'PRI'));
-- clausula WHERE, primero iguala las claves primarias como condicion.
    SET sand = CONCAT(' AND (',(SELECT GROUP_CONCAT(tabla1,'.',column_name,' <> ',tabla2,'.',column_name SEPARATOR ' OR ') FROM information_schema.columns WHERE table_schema = @base AND table_name = tabla1),');');
-- continua el WHERE indicando que ademas se debe cumpir con que las columnas a actualizar deben teber registros diferentes.   
    SET @sinicial = CONCAT(sinicial,sset,swhere,sand); -- unifica los textos
    PREPARE stmt FROM @sinicial; -- prepara la consulta dinamica
    EXECUTE stmt; -- la ejecuta
    DEALLOCATE PREPARE stmt; -- la elimina
END $$
DELIMITER ;

CALL actualizar_tabla('clientes','clientes_actualizado'); -- llama al procedimiento para ejecucion, se deben cambiar los nombres de las tablas.
