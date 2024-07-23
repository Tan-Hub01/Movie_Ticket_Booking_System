# Ticket_Booking_System

## Overview
The Book My Show system is a command-line ticket booking application designed to provide users with an easy and efficient way to book tickets for current shows. The system includes features for adding, editing, deleting, displaying, and searching for bookings. This application is implemented in Python and uses a MySQL database for data storage.

## Features
### Main Menu
- **Make a Booking:** Allows users to book tickets by providing their name, email, show name, phone number, credit card number, and password.
- **Delete a Booking:** Provides options to delete bookings by various criteria such as name, email, show booked, phone number, credit card number, and password.
- **Edit Booking:** Enables users to update their booking details including name, email, show booked, phone number, credit card number, and password.
- **Display Bookings:** Offers multiple display options to view all records or filter by specific details such as name, email, show booked, phone number, credit card number, and password.
- **Search Record:** Allows users to search for specific records in the database by name, email, show booked, phone number, credit card number, and password.
- **Exit:** Exits the application.

## Current Shows
- Mirzapur Season II
- Laxmii
- Aashram II
- Ludo
- Chhalaang
- Serious Men
- Kota Factory
- Scam 1992: The Harshad Mehta Story

### Booking Process
The user is prompted to enter their details for booking a show.
The system verifies the availability of the selected show.
Upon successful verification, the booking is confirmed and payment is processed.
### Deleting Bookings
The user can delete all records or filter the deletion by specific criteria.
Before deletion, the current data is displayed for verification.
### Editing Bookings
The user can update specific details of their bookings.
The current data is displayed for verification before making any changes.
### Display and Search
The user can display all bookings or filter the display by specific details.
The search functionality allows the user to find records based on different criteria.

## Database Schema
The application uses a MySQL database with a table named BOOKINGS with the following fields:

- Name: User's name
- Email_id: User's email address
- Show: Name of the show booked
- Phone_No: User's phone number
- Credit_Card_No: User's credit card number
- Password: User's password

## Installation and Setup
- **Install MySQL:** Ensure MySQL is installed and running on your machine.
- **Database Setup:** Create a database named tick and a table BOOKINGS using the provided schema.
- **Python Dependencies:** Install the required Python packages using pip install MySQLdb prettytable.
- **Run the Application:** Execute the script using python ticket_booking_system.py.

## Conclusion
The Book My Show ticket booking system is a comprehensive solution for managing show bookings. With a user-friendly command-line interface and robust database integration, it simplifies the process of booking, editing, deleting, displaying, and searching for tickets.
