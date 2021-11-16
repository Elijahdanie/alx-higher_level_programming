-- This displays all scores greater than or equal to 10
-- In second table
SELECT
	score, name
FROM
	second_table
WHERE
      score >= 10
ORDER BY score DESC;
