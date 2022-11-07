use sakila;



DELIMITER //

CREATE FUNCTION sum_string_to_ascii ( inputStr TEXT )
RETURNS TEXT
DETERMINISTIC
BEGIN
  DECLARE strLen INT DEFAULT 0;
  DECLARE idx INT DEFAULT 0;
  DECLARE current_char VARCHAR(1);
  DECLARE current_char_ascii VARCHAR(10);
  DECLARE outputStr int default 0;
  
  IF inputStr IS NULL THEN
    SET inputStr = '';
  END IF;
  
  SET strLen = CHAR_LENGTH(inputStr);
  SET idx = 1;
    
  WHILE idx <= strLen DO
    SET current_char = SUBSTR(inputStr, idx, 1);
    SET current_char_ascii = ASCII(current_char);
    IF idx = 1 THEN
        SET outputStr = current_char_ascii;
    ELSE
        SET outputStr = outputStr + current_char_ascii;
    END IF;
    
    SET idx = idx+1;

  END WHILE;
  
  RETURN outputStr;
END; //

select sum_string_to_ascii('abcd');

-- DROP FUNCTION sum_string_to_ascii;
