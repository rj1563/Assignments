CREATE TABLE Rooms(
	RoomID INT IDENTITY(1,1) PRIMARY KEY,
	RoomNumber VARCHAR(10),
	Type VARCHAR(15),
	Price DECIMAL(7, 2)
);

CREATE TABLE Bookings(
	BookingID INT IDENTITY(1,1) PRIMARY KEY,
	RoomID INT,
	CustomerName VARCHAR(20),
	CheckInDate DATE,
	CheckOutDate DATE,
	BookingStatus VARCHAR(10) CHECK (BookingStatus IN ('Confirmed', 'Cancelled')),
	Timestamp DATETIME DEFAULT GETDATE(),
	FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

INSERT INTO Rooms (RoomNumber, Type, Price) VALUES 
('101', 'Single', 50.00),
('102', 'Double', 75.00),
('103', 'Suite', 120.00),
('104', 'Single', 55.00),
('105', 'Double', 80.00),
('106', 'Suite', 130.00),
('107', 'Single', 60.00),
('108', 'Double', 85.00),
('109', 'Suite', 140.00),
('110', 'Single', 65.00);

INSERT INTO Bookings (RoomID, CustomerName, CheckInDate, CheckOutDate, BookingStatus) VALUES
(1, 'Alice Johnson', '2025-03-01', '2025-03-05', 'Confirmed'),
(2, 'Bob Smith', '2025-03-02', '2025-03-06', 'Confirmed'),
(3, 'Charlie Brown', '2025-03-03', '2025-03-07', 'Cancelled'),
(4, 'David Wilson', '2025-03-04', '2025-03-08', 'Confirmed'),
(5, 'Emma Davis', '2025-03-05', '2025-03-09', 'Confirmed'),
(6, 'Frank Thomas', '2025-03-06', '2025-03-10', 'Cancelled'),
(7, 'Grace Hall', '2025-03-07', '2025-03-11', 'Confirmed'),
(8, 'Henry Lee', '2025-03-08', '2025-03-12', 'Confirmed'),
(9, 'Ivy Scott', '2025-03-09', '2025-03-13', 'Cancelled'),
(10, 'Jack White', '2025-03-10', '2025-03-14', 'Confirmed');

SELECT * FROM Rooms;
SELECT * FROM Bookings;