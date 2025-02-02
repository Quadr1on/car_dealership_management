import mysql.connector as m
import matplotlib.pyplot as plt
import numpy as np 
import time
from table import tabulate
import pickle

# to create a connection with the MySQL server
con = m.connect(host="localhost", user="root", passwd="your_password", database="cars")
cur = con.cursor()

def Admin():
    def add_car():
        car_name = input("Enter car name: ")
        year = input("Enter year: ")
        selling_price = input("Enter selling price: ")
        km_driven = input("Enter kilometers driven: ")
        fuel = input("Enter fuel type: ")
        seller_type = input("Enter seller type: ")
        transmission = input("Enter transmission type: ")
        owner = input("Enter owner information: ")

        # Inserts data into the database table    
        insert_query = "INSERT INTO car_data (name, year, selling_price, km_driven, fuel, seller_type, transmission, owner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = [car_name, year, selling_price, km_driven, fuel, seller_type, transmission, owner]

        cur.execute(insert_query, values)
        con.commit()
        print("Car details added successfully!")

    def updateCarDetails():
        sno = input("Enter the sno you want to update: ")
        
        l = [sno]
        check_query = "SELECT * FROM car_data WHERE sno = %s"
        cur.execute(check_query, l)
        car = cur.fetchone()
        
        if car is None:
            print("Car with the provided name not found.")
            return

        print("Current Car Details:")
        print(f"Car Name: {car[1]}")
        print(f"Year: {car[2]}")
        print(f"Selling Price: {car[3]}")
        print(f"Kilometers Driven: {car[4]}")
        print(f"Fuel Type: {car[5]}")
        print(f"Seller Type: {car[6]}")
        print(f"Transmission Type: {car[7]}")
        print(f"Owner: {car[8]}")

        
        new_car_name = input("Enter the new car name: ")
        new_year = input("Enter the new year: ")
        new_selling_price = input("Enter the new selling price: ")
        new_km_driven = input("Enter the new kilometers driven: ")
        new_fuel = input("Enter the new fuel type: ")
        new_seller_type = input("Enter the new seller type: ")
        new_transmission = input("Enter the new transmission type: ")
        new_owner = input("Enter the new owner information: ")

        
        update_query = "UPDATE car_details SET car_name = %s, year = %s, selling_price = %s, km_driven = %s, fuel = %s, seller_type = %s, transmission = %s, owner = %s WHERE sno = %s"
        values = (new_car_name, new_year, new_selling_price, new_km_driven, new_fuel, new_seller_type, new_transmission, new_owner,sno)

        cur.execute(update_query, values)
        con.commit()
        print("Car details updated successfully!")

    def deletedata():
        sno = input("enter slno you want to delete: ")
        qry = f"delete from car_data where sno = {sno}"
        cur.execute(qry)
        cur.commit()
        print("successfully deleted all the data!!")

    def addColumn():
        cName = input("enter column name: ")
        dType = input("enter data type: ")
        val = [cName,dType]
        alter = "alter table car_data add column %s %s"
        cur.execute(alter,val)
        cur.commit()
        print("column added successfully!!")

    while True:
        print("############# AdminMenu ############")
        print("1.Add data")
        print("2.update")
        print("3.delete data")
        print("4.add new column")
        c = eval(input("Enter Choice: "))
        if c == 1:
            add_car()
        elif c == 2:
            updateCarDetails()
        elif c == 3:
            deletedata()
        elif c == 4:
            addColumn()
        else: 
                print("invalid input")
                x = input("do u want to continue(y/n):")
                if x == "y":
                    continue
                else:
                    break
        
def User():

    def displayAll():
        qry = "select * from car_data"
        cur.execute(qry)
        data = cur.fetchall()
        headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
        print(tabulate(data, headers, tablefmt="pretty"))


    def countCars():
        count_query = "SELECT COUNT(*) FROM car_data"
        cur.execute(count_query)
        total_cars = cur.fetchone()[0]
        print(f"Total number of cars in the database: {total_cars}")


    def maxPrice():
        qry = "select max(selling_price) from car_data"
        cur.execute(qry)
        data = cur.fetchall()
        for rec in data:
            print(rec)

    def minPrice():
        qry = "select min(selling_price) from car_data"
        cur.execute(qry)
        data = cur.fetchall()
        for rec in data:
            print(rec)

    def search():
        def carName():
            car = input("Enter car name you want to search: ")
            l = [f"%{car}%"]
            qry = "select * from car_data where name like %s"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def manuYear():
            year = input("Enter Year of Manufacturing you want to search: ")
            l = [year]
            qry = "select * from car_data where year = %s"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def sellPrice():
            strbud = input("Enter Your budget starting Range: ")
            maxbud = input("Enter Your budget Maximum Range: ")
            l = [strbud, maxbud]
            qry = "select * from car_data where selling_price between %s and %s order by selling_price"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def kmsDriven():
            kmDs = input("Enter Km Driven starting Range: ")
            kmdmax = input("Enter Km Driven Maximum Range: ")
            l = [kmDs, kmdmax]
            qry = "select * from car_data where km_driven between %s and %s order by km_driven"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def fuelType():
            fuel = input("Enter fuel type you want to search: ")
            l = [fuel]
            qry = "select * from car_data where fuel = %s"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def sellType():
            sType = input("Enter what kind of a seller would you like to purchase from (dealer|individual): ")
            l = [sType]
            qry = "select * from car_data where seller_type = %s"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def transmission():
            tmison = input("Would you like Manual or Automatic: ")
            l = [tmison]
            qry = "select * from car_data where transmission = %s"
            cur.execute(qry, l)
            data = cur.fetchall()
            headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
            print(tabulate(data, headers, tablefmt="pretty"))

        def nOwner():
            c = input("Do you want only:\n1. First owner cars (or)\n2. Get a range\n=>")
            if c == "1":
                l = ["first owner"]
                qry = 'SELECT * FROM car_data WHERE owner LIKE %s'
                cur.execute(qry, l)
                data = cur.fetchall()
                headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
                print(tabulate(data, headers, tablefmt="pretty"))
            elif c == "2":
                Ownermin = input("Enter Your minimum number of owner Range (first owner): ")
                ownMax = input("Enter Your Maximum number of owner Range (n owner, n = second owner, third owner etc): ")
                l = [Ownermin, ownMax]
                qry = "SELECT * FROM car_data WHERE owner BETWEEN %s AND %s ORDER BY owner"
                cur.execute(qry, l)
                data = cur.fetchall()
                headers = ["Serial No", "Car Name", "Year", "Selling Price", "Kilometers Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"]
                print(tabulate(data, headers, tablefmt="pretty"))
            else:
                print("Invalid input")

        while True:
            # Menu for the search function
            print("######## Search Menu ########")
            print("1. Car name")
            print("2. Year of manufacturing")
            print("3. Selling Price")
            print("4. KMs Driven")
            print("5. Fuel Type")
            print("6. Seller Type")
            print("7. Transmission")
            print("8. No of Owners")
            print("9. Quit (q)")

            c = input("What Would you like to Search: ").lower()

            if c == "1" or c == "car name":
                carName()
            elif c == "2" or c == "year of manufacturing" or c == "year":
                manuYear()
            elif c == "3" or c == "selling price":
                sellPrice()
            elif c == "4" or c == "kms driven":
                kmsDriven()
            elif c == "5" or c == "fuel type":
                fuelType()
            elif c == "6" or c == "seller type":
                sellType()
            elif c == "7" or c == "transmission":
                transmission()
            elif c == "8" or c == "no of owners":
                nOwner()
            elif c == "9" or c == "q":
                break
            else:
                print("Invalid input")
                x = input("Do you want to continue (y/n): ")
                if x != "y":
                    break

    def Graph():

        def visualizeCarPrices():
            # Fetching data from the database
            cur.execute("SELECT selling_price FROM car_data")
            selling_prices = [row[0] for row in cur.fetchall()]

            # Calculate mean and median
            mean_price = np.mean(selling_prices)
            median_price = np.median(selling_prices)

            # Create a figure for the visualization
            fig, ax = plt.subplots(figsize=(10, 6))

            # Plotting a bar graph of selling prices
            ax.bar(range(len(selling_prices)), selling_prices, color='Lightgreen')

            # Set plot title and labels
            ax.set_title('Selling Prices of Cars', fontsize=16)
            ax.set_xlabel('Cars', fontsize=14)
            ax.set_ylabel('Selling Price', fontsize=14)
            ax.grid(True)

            # Display mean and median values on the plot with increased font size for visibility
            ax.text(0.6, 0.85, f"Y axis = 10lakhs", fontsize=12, transform=ax.transAxes)
            ax.text(0.6, 0.80, f"Median Price: ${median_price:.0f}", fontsize=12, transform=ax.transAxes)

            plt.tight_layout()
            plt.show()

        def visualizeKilometersDriven():
            cur.execute("SELECT km_driven FROM car_data")
            kilometers_driven = [row[0] for row in cur.fetchall()]

            plt.figure(figsize=(8, 6))
            plt.hist(kilometers_driven, bins=20, color='LightGreen')
            plt.title('Distribution of Kilometers Driven')
            plt.xlabel('Kilometers Driven')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()

        def visualizeManufacturingYears():
            cur.execute("SELECT year FROM car_data")
            manufacturing_years = [row[0] for row in cur.fetchall()]

            plt.figure(figsize=(8, 6))
            plt.hist(manufacturing_years, bins=20, color='salmon')
            plt.title('Distribution of Manufacturing Years')
            plt.xlabel('Manufacturing Year')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()
        while True:    
            print("############ Graph Menu #############")
            print("1.Car price Graph")
            print("2.Kilometer driven")
            print("3.Year")
            c = eval(input("enter Choice: "))
            if c == 1:
                visualizeCarPrices()
            elif c == 3:
                visualizeManufacturingYears()
            elif c == 2:
                visualizeKilometersDriven()
            else: 
                    print("invalid input")
                    x = input("do u want to continue(y/n):")
                    if x == "y":
                        continue
                    else:
                        break

    while True:
        print("############# User Menu ############")
        print("1.Display all")
        print("2.Search")
        print("3.Count all the cars present in the DB")
        print("4.Highest priced vehicle")
        print("5.Lowest priced vehicle")
        print("6.Graphs of  Our DataBase")
        c = eval(input("Enter you choice "))
        if c == 1:
            displayAll()
        
        elif c ==2:
            search()

        elif c == 3:
            countCars()
        
        elif c == 4:
            maxPrice()

        elif c == 5:
            minPrice()
            
        elif c==6:
            Graph()

        else: 
            print("invalid input")
            x = input("do u want to continue(y/n):")
            if x == "y":
                continue
            else:
                break


if con.is_connected() == False:
    print("error")

else:
    def adminCheck():
        f = open("password.dat","rb")
        try:
            while True:
                l = pickle.load(f)
                for i in l:
                    password = i
        except:
            f.close()
            
        nI = 0
        run = True
        while run:
            pwd = input("Enter Password:")
            if pwd == password:
                Admin()
            else: 
                print("invalid password, Try Again")
                nI += 1
                if nI == 5:
                    run = False
                    print("You Entered wrong password:5 times\nTry again After 30 seconds.")
                    for i in range(30):
                        i = 30-i
                        print("time remaining:",i)
                        time.sleep(1)
                    break
    #Main Menu 
    while True:
        print("####### MainMenu #######")
        checkUser = eval(input("Who are You?\n1.Admin\n2.User\n3.Exit\n=>"))
        if checkUser == 1:
            adminCheck()

        elif checkUser ==2:
            User()

        elif checkUser == 3:
            break

        else: 
            print("invalid input")
            x = input("do u want to continue(y/n):")
            if x == "y":
                continue
            else:
                break
    
