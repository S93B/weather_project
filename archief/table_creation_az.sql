CREATE TABLE stad (
    stad_id INT IDENTITY(1,1) PRIMARY KEY,
    stad VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE live_weer (
    live_id INT IDENTITY(1,1) PRIMARY KEY,
    timestamp_api DATE NOT NULL,
    stad_id INT REFERENCES stad(stad_id)
);

CREATE TABLE week_verwachting (
    week_id INT IDENTITY(1,1) PRIMARY KEY,
    dag DATE NOT NULL,
    stad_id INT REFERENCES stad(stad_id)
);

CREATE TABLE uur_verwachting (
    uur_id INT IDENTITY(1,1) PRIMARY KEY,
    uur DATE NOT NULL,
    stad_id INT REFERENCES stad(stad_id)
);

CREATE TABLE weather (
    live_id INT REFERENCES live_weer(live_id),
    week_id INT REFERENCES week_verwachting(week_id),
    uur_id INT REFERENCES uur_verwachting(uur_id),
    stad_id INT REFERENCES stad(stad_id),
    temp DECIMAL(10,2) NOT NULL,
    g_temp DECIMAL(10,2) NOT NULL,
    min_temp INT NOT NULL,
    max_temp INT NOT NULL
);
