-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;

    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight > 0 THEN
        SET avg_score = total_score / total_weight;
        UPDATE users SET average_score = avg_score WHERE id = user_id;
    ELSE
        UPDATE users SET average_score = 0 WHERE id = user_id;
    END IF;
END;

DELIMITER ;
