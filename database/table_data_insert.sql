UPDATE uur_weather_data
SET uur =
    CONVERT(
        DATETIME,
        SUBSTRING(uur, 7, 4) + '-' +
        SUBSTRING(uur, 4, 2) + '-' +
        SUBSTRING(uur, 1, 2) + ' ' +
        SUBSTRING(uur, 12, 5),
        120
    );

SELECT *
FROM uur_weather_data;