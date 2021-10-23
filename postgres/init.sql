CREATE DATABASE metrics;
\c metrics

CREATE TABLE IF NOT EXISTS rate(
    ID                serial          PRIMARY KEY,
    created_at        DATE            NOT NULL,
    coast             smallint        NOT NULL,
    stonks            bool            default false,
    coins             varchar(255)    NOT NULL
)