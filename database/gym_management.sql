DROP TABLE IF EXISTS instructor_timetables;
DROP TABLE IF EXISTS schedules_members;
DROP TABLE IF EXISTS schedules;
DROP TABLE IF EXISTS instructor_schedules;
DROP TABLE IF EXISTS instructor_details;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(30),
    date_of_birth DATE,
    membership BOOLEAN,
    premium BOOLEAN,
    member_since DATE,
    member_until DATE
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    room_name VARCHAR(255),
    capacity INT,
    description VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255),
    description VARCHAR(255),
    capacity INT,
    max_time INT
);

CREATE TABLE instructor_details (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_of_birth DATE
);

CREATE TABLE instructor_schedules (
    id SERIAL PRIMARY KEY,
    nickname VARCHAR(255),
    monday BOOLEAN,
    tuesday BOOLEAN,
    wednesday BOOLEAN,
    thursday BOOLEAN,
    friday BOOLEAN,
    saturday BOOLEAN,
    sunday BOOLEAN,
    start_time TIME,
    end_time TIME
);

CREATE TABLE instructor_timetables (
    id SERIAL PRIMARY KEY,
    week_start DATE,
    i_details_id INT REFERENCES instructor_details(id) ON DELETE CASCADE,
    i_schedules_id INT REFERENCES instructor_schedules(id) ON DELETE CASCADE
);

CREATE TABLE schedules (
    id SERIAL PRIMARY KEY,
    class_date DATE,
    start_time TIME,
    length_mins INT,
    instructor_id INT REFERENCES instructor_details(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE,
    room_id INT REFERENCES rooms(id) ON DELETE CASCADE
);

CREATE TABLE schedules_members (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    schedule_id INT REFERENCES schedules(id) ON DELETE CASCADE
);