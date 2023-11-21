SET @tabla = 'tiposdegasto';
SET @base = 'depython';

SET SESSION group_concat_max_len = 1000000; -- alarga la cantidad de caracteres admisibles por la variable @sql
SELECT CONCAT('SELECT * FROM ',@tabla ,' WHERE ', 
              GROUP_CONCAT(column_name, ' IS NULL OR ' SEPARATOR ''))
INTO @sql -- eso es basicamente hacer un SET @SQL = lo que resulta del concat de arriba
FROM information_schema.columns
WHERE table_schema = @base -- Nombre de mi DB
  AND table_name = @tabla; -- Genera una string que basicamente es SELECT * FROM tabla WHERE col1 IS NULL OR col2 IS NULL... etc.

SET @sql = LEFT(@sql, LENGTH(@sql) - 3);  -- Eliminar el último 'OR' -- Saca el ultimo OR del loop
PREPARE stmt FROM @sql; -- Prepara la consulta dinamica (consulta desde una variable)
EXECUTE stmt; -- la ejecuta
DEALLOCATE PREPARE stmt; -- la elimina



/*
DELIMITER $$ 
CREATE PROCEDURE proc_1()
BEGIN 
DECLARE contador INT DEFAULT 0;
DECLARE max_contador INT DEFAULT 4;
DECLARE res_parcial TEXT DEFAULT '';
DECLARE resultado TEXT DEFAULT '';
WHILE contador < max_contador DO 
		SELECT descripcion
        INTO res_parcial
		FROM (SELECT row_number() OVER () as fila, descripcion FROM canaldeventa) AS tabla1
		WHERE fila = contador;
        SET contador = contador + 1;
        SET resultado = CONCAT(resultado,' ',res_parcial);
END WHILE;
SELECT resultado;
END $$
DELIMITER ;

DROP PROCEDURE proc_1;
CALL proc_1;
*/