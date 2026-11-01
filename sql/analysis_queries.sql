-- COVID-19 Trends | Table: covid_daily
SELECT country, SUM(new_cases) AS cases, SUM(new_recoveries) AS recoveries, SUM(new_deaths) AS deaths
FROM covid_daily GROUP BY country ORDER BY cases DESC;
SELECT date, SUM(new_cases) AS cases FROM covid_daily GROUP BY date ORDER BY date;
-- These are synthetic practice records, not official public-health statistics.