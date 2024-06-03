CREATE TABLE Owners (
    owner_id INTEGER PRIMARY KEY,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    owner_address TEXT NOT NULL
);

CREATE TABLE Pets (
    pet_id INTEGER PRIMARY KEY,
    pet_name VARCHAR(32) NOT NULL,
    pet_age INTEGER NOT NULL,
    pet_type TEXT NOT NULL,
    pet_gender CHAR NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Owners (owner_id)
);

INSERT INTO Owners (first_name, last_name, owner_address) VALUES ("John", "Smith", "123 Faketon Street, Exampleville, PO15 4AB");

INSERT INTO Pets (pet_name, pet_age, pet_type, pet_gender, owner_id) VALUES ("Bob", 3, "Goldfish", 'F', 1);