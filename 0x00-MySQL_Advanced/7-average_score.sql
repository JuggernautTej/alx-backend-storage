-- A SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and 
-- store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
	
	CREATE PROCEDURE 
        ComputeAverageScoreForUser(
            IN user_id INT
            )
    BEGIN 
        DECLARE score_average FLOAT;

        -- Computes average score
        SELECT
            AVG(score)
        INTO
            score_average
        FROM
            corrections
        WHERE
            corrections.user_id = user_id;
   
        -- Store the computed average score for the student
        UPDATE
            users
        SET
            average_score = score_average
        WHERE
            id = user_id;
	END $$
	
DELIMITER ;
