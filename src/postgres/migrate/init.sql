CREATE SCHEMA IF NOT EXISTS shape;
CREATE TABLE IF NOT EXISTS shape.rectangle (
  rectangle_id SERIAL PRIMARY KEY,
  a            INTEGER NOT NULL,
  b            INTEGER NOT NULL,
  area         INTEGER,
  perimeter    INTEGER
);
INSERT INTO shape.rectangle (a, b) VALUES (1, 2);
INSERT INTO shape.rectangle (a, b) VALUES (3, 4);
INSERT INTO shape.rectangle (a, b) VALUES (5, 6);
INSERT INTO shape.rectangle (a, b) VALUES (7, 8);
