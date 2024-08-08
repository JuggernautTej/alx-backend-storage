-- A SQL script that creates a trigger that resets the
-- valid_email attribute only when the email attribute
-- has been changed.
DELIMITER $$
	
	CREATE TRIGGER 
        change_valid_email
	BEFORE UPDATE ON 
        users
	FOR EACH ROW
	    BEGIN
            IF NEW.email <> OLD.email THEN
            SET
                NEW.valid_email = 0;
            END IF;
	END $$
	
DELIMITER ;
