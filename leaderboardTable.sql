-- Active: 1729467801369@@127.0.0.1@3306
CREATE DATABASE leaderboard

USE leaderboard

CREATE TABLE games (
    GameID INT NOT NULL,
    Title VARCHAR(30),
    ReleaseDate DATE,
    PRIMARY KEY (GameID)
);

CREATE TABLE versions (
    GameID INT NOT NULL,
    VersionID VARCHAR(15) NOT NULL,
    Platform VARCHAR(20),
    PRIMARY KEY (GameID, VersionID),
    FOREIGN KEY (GameID) REFERENCES games (GameID)
);

CREATE TABLE categories (
    CategoryID INT NOT NULL,
    GameID INT NOT NULL,
    VersionID VARCHAR(15) NOT NULL,
    Name VARCHAR(30),
    Description VARCHAR(100),
    Type VARCHAR(15),
    PRIMARY KEY (CategoryID, GameID, VersionID),
    FOREIGN KEY (GameID, VersionID) REFERENCES games (GameID, VersionID)
);

CREATE TABLE users (
    UserID INT NOT NULL,
    Username VARCHAR(20),
    Password VARCHAR(20),
    PRIMARY KEY (UserID)
);

CREATE TABLE friends (
    UserID INT NOT NULL,
    FriendID INT NOT NULL,
    PRIMARY KEY (UserID, FriendID),
    FOREIGN KEY (UserID) REFERENCES users (UserID),
    FOREIGN KEY (FriendID) REFERENCES users (UserID)
);

CREATE TABLE requests (
    Sender INT NOT NULL,
    Receiver INT NOT NULL,
    PRIMARY KEY (Sender, Receiver),
    FOREIGN KEY (Sender) REFERENCES users (UserID),
    FOREIGN KEY (Receiver) REFERENCES users (UserID)
);

CREATE TABLE scores (
    UserID INT NOT NULL,
    CategoryID INT NOT NULL,
    Score DOUBLE,
    PRIMARY KEY (UserID, CategoryID),
    FOREIGN KEY (CategoryID) REFERENCES categories (CategoryID)
);