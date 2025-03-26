create table stad(
    stad_id SERIAL PRIMARY KEY,
    stad VARCHAR(40) NOT NULL UNIQUE
);
create table live_weer(
    live_id SERIAL PRIMARY KEY,
    timestamp_api DATE NOT NULL,
    stad INT REFERENCES stad(stad_id)
);
create table week_verwachting(
    week_id SERIAL PRIMARY KEY,
    dag DATE NOT NULL,
    stad INT REFERENCES stad(stad_id)
);
create table uur_verwachting(
    uur_id SERIAL PRIMARY KEY,
    uur DATE NOT NULL,
    stad INT REFERENCES stad(stad_id)
);
create table weather(
    live_id INT REFERENCES live_weer(live_id),
    week_id INT REFERENCES week_verwachting(week_id),
    uur_id INT REFERENCES uur_verwachting(uur_id),
    stad_id INT REFERENCES stad(stad_id),
    temp  DECIMAL(10,2) NOT NULL,
    g_temp  DECIMAL(10,2) NOT NULL,
    min_temp  INT NOT NULL,
    max_temp  INT NOT NULL
)


