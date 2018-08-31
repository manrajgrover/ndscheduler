CREATE EVENT purge_executions
  ON SCHEDULE
    EVERY 1 DAY
    STARTS (TIMESTAMP(CURRENT_DATE) + INTERVAL 1 DAY + INTERVAL 1 HOUR)
  DO
    DELETE FROM scheduler_execution
    WHERE updated_time < NOW() - INTERVAL 7 DAY
        AND state NOT IN (1, 2);
