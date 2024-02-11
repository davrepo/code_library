-- Create tables for the database

-- Table for humans
CREATE TABLE humans (
    human_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table for gods
CREATE TABLE gods (
    god_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table for priests
CREATE TABLE priests (
    priest_id INT PRIMARY KEY,
    human_id INT NOT NULL,
    god_id INT NOT NULL,
    FOREIGN KEY (human_id) REFERENCES humans(human_id),
    FOREIGN KEY (god_id) REFERENCES gods(god_id)
);

-- Table for sacrifice categories
CREATE TABLE sacrifice_categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

-- Table for sacrifices
CREATE TABLE sacrifices (
    sacrifice_id INT PRIMARY KEY,
    human_id INT NOT NULL,
    god_id INT NOT NULL,
    priest_id INT,
    category_id INT NOT NULL,
    time TIMESTAMP NOT NULL,
    place VARCHAR(255) NOT NULL,
    value FLOAT NOT NULL,
    FOREIGN KEY (human_id) REFERENCES humans(human_id),
    FOREIGN KEY (god_id) REFERENCES gods(god_id),
    FOREIGN KEY (priest_id) REFERENCES priests(priest_id),
    FOREIGN KEY (category_id) REFERENCES sacrifice_categories(category_id)
);

-- Table for flesh sacrifices
CREATE TABLE flesh_sacrifices (
    sacrifice_id INT PRIMARY KEY,
    animal_type VARCHAR(255) NOT NULL,
    FOREIGN KEY (sacrifice_id) REFERENCES sacrifices(sacrifice_id)
);

-- Table for wine sacrifices
CREATE TABLE wine_sacrifices (
    sacrifice_id INT PRIMARY KEY,
    wine_type VARCHAR(255) NOT NULL,
    volume FLOAT NOT NULL,
    FOREIGN KEY (sacrifice_id) REFERENCES sacrifices(sacrifice_id)
);

-- Table for valuable sacrifices
CREATE TABLE valuable_sacrifices (
    sacrifice_id INT PRIMARY KEY,
    item_type VARCHAR(255) NOT NULL,
    weight FLOAT NOT NULL,
    FOREIGN KEY (sacrifice_id) REFERENCES sacrifices(sacrifice_id)
);

-- Table for sea_monster_attacks
CREATE TABLE sea_monster_attacks (
    attack_id INT PRIMARY KEY,
    human_id INT NOT NULL,
    time TIMESTAMP NOT NULL,
    FOREIGN KEY (human_id) REFERENCES humans(human_id)
);

-- Table for cyclops_attacks
CREATE TABLE cyclops_attacks (
    attack_id INT PRIMARY KEY,
    human_id INT NOT NULL,
    time TIMESTAMP NOT NULL,
    FOREIGN KEY (human_id) REFERENCES humans(human_id)
);