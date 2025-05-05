CREATE TABLE live_weather_data (
    live_id INT IDENTITY(1,1) PRIMARY KEY,
    temp DECIMAL(5,2) NOT NULL,
    g_temp DECIMAL(5,2) NOT NULL,
    windbft DECIMAL(5,2) NOT NULL,
    sup TIME NOT NULL,
    sunder TIME NOT NULL,
    stad VARCHAR(25) NOT NULL,
    timestamp_api DATETIME NOT NULL
);

CREATE TABLE week_weather_data (
   week_id INT IDENTITY(1,1) PRIMARY KEY,
    dag DATETIME NOT NULL,
   min_temp INT NOT NULL,
    max_temp INT NOT NULL,
    windbft DECIMAL(5,2) NOT NULL,
    neersl_perc_per_dag INT NOT NULL,
    zond_per_dag INT NOT NULL,
    stad VARCHAR(25),
    timestamp_api DATETIME NOT NULL
);

CREATE TABLE uur_weather_data (
    uur_id INT IDENTITY(1,1) PRIMARY KEY,
    uur VARCHAR(50) NOT NULL,
    temp DECIMAL(5,2) NOT NULL,
    windbft DECIMAL(5,2) NOT NULL,
    neersl INT NOT NULL,
    gr INT NOT NULL,
    stad VARCHAR(25),
    timestamp_api DATETIME NOT NULL
);