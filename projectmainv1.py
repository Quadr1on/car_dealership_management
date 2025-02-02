import mysql.connector as m
from tabulate import tabulate

# to create a connection with the MySQL server
con = m.connect(host="localhost", user="root", passwd="your_pasword", database="cars")
cur = con.cursor()

# Main functions
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
    car_name = input("Enter the name of the car you want to update: ")
    
    l = [car_name]
    check_query = "SELECT * FROM car_data WHERE name = %s"
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

    
    update_query = "UPDATE car_data SET name = %s, year = %s, selling_price = %s, km_driven = %s, fuel = %s, seller_type = %s, transmission = %s, owner = %s WHERE name = %s"
    values = (new_car_name, new_year, new_selling_price, new_km_driven, new_fuel, new_seller_type, new_transmission, new_owner, car_name)

    cur.execute(update_query, values)
    con.commit()
    print("Car details updated successfully!")

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

def deletedata():
    sno = input("Enter slno you want to delete: ")
    qry = f"delete from car_data where sno = {sno}"
    cur.execute(qry)
    con.commit()
    print("Successfully deleted data!")

def addColumn():
    cName = input("Enter column name: ")
    dType = input("Enter data type: ")
    val = [cName, dType]
    alter = "alter table car_data add column %s %s"
    cur.execute(alter, val)
    con.commit()
    print("Column added successfully!")

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



if con.is_connected() == False:
    print("error")
else:
    while True:
        print("############# MainMenu ############")
        print("1. Add data")
        print("2. Display all")
        print("3. Search")
        print("4. Count all the cars present in the DB")
        print("5. Update")
        print("6. Delete data")
        print("7. Add new column")
        print("8. Highest priced vehicle")
        print("9. Lowest priced vehicle")

        c = eval(input("Enter Choice: "))
        if c == 1:
            add_car()
        elif c == 2:
            displayAll()
        elif c == 3:
            search()
        elif c == 4:
            countCars()
        elif c == 5:
            updateCarDetails()
        elif c == 6:
            deletedata()
        elif c == 7:
            addColumn()
        elif c == 8:
            maxPrice()
        elif c == 9:
            minPrice()
