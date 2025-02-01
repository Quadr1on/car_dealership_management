# Car Dealership Management System

A comprehensive Python-based management system for car dealerships that handles inventory management, data visualization, and user access control.

## 🚗 Features

### Admin Portal
- **Inventory Management**
  - Add new cars to the database
  - Update existing car details
  - Delete car records
  - Add new data columns to the database
  
- **Analytics**
  - Calculate total value of all cars
  - Get total car count in inventory
  
### User Portal
- **Car Search & Filtering**
  - Search by car name
  - Filter by manufacturing year
  - Filter by price range
  - Filter by kilometers driven
  - Filter by fuel type
  - Filter by seller type
  - Filter by transmission
  - Filter by owner history

- **Data Visualization**
  - Car price distribution graphs
  - Kilometers driven distribution
  - Manufacturing year distribution

- **Quick Stats**
  - View highest priced vehicle
  - View lowest priced vehicle
  - Display complete inventory

## 🛠️ Technical Details

### Dependencies
- MySQL Connector
- Matplotlib
- Tabulate
- Pickle

### Database Structure
The system uses MySQL database with the following main fields:
- Serial Number
- Car Name
- Year
- Selling Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner Information

## 🔐 Security Features
- Admin access protected by password
- Failed login attempt management
  - 5 incorrect attempts trigger a 30-second timeout
- Separate user and admin interfaces

## 📊 Data Presentation
- Tabulated data display using the `tabulate` library
- Interactive graphs and charts
- Clean console-based user interface

## 🎯 Use Cases
- Car dealership inventory management
- Customer-facing car search portal
- Sales analytics and reporting
- Market value analysis

## 💻 Installation
1. Ensure MySQL is installed and running
2. Install required Python packages:
    1. mysql-connector-python
    2. matplotlib
    3. tabulate
3. Create a Schema/database called "cars"
4. Install the given datasets through MySQL workbench
5. Configure database connection parameters in the script
6. Run the main script to start the application

## 🔑 Access Levels
- **Admin**: Full access to management features
- **User**: Read-only access with search and visualization capabilities

---
*This system is designed to provide a complete solution for car dealership management with both administrative and customer-facing features.*
