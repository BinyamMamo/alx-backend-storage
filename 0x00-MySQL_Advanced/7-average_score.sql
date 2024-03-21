-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_count INT;

    -- Calculate the total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the total count of corrections for the user
    SELECT COUNT(*) INTO total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Compute the average score (handle division by zero)
    IF total_count > 0 THEN
        SET @average_score = total_score / total_count;
    ELSE
        SET @average_score = 0;
    END IF;

    -- Update the user's average score
    UPDATE users
    SET average_score = @average_score
    WHERE id = user_id;
END //

DELIMITER ;
