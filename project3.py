import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk


class ReservationUserWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Reservation and User Window")
        self.notebook = ttk.Notebook(self.master)
        background_image = Image.open("bg2.jpg")  # Replace with your image file
        background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image
        background_label = tk.Label(self.master, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.connection = sqlite3.connect("tourism.db")
        self.create_tables()
        self.create_reservation_tab()
        customer_label = tk.Label(self.master, text="Customer Name:")
        customer_label.place(in_=background_label, x=10, y=10)

    def create_tables(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT NOT NULL,
                    contact TEXT NOT NULL,  -- Add this line
                    duration TEXT NOT NULL,
                    hotel TEXT NOT NULL,
                    restaurant TEXT NOT NULL,
                    travel_mode TEXT NOT NULL,
                    total_cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    cuisine TEXT,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS hotels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    rating INTEGER,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS travels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destination TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    mode TEXT,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL
                )
                """
            )

    def close_connection(self):
        if self.connection:
            self.connection.close()
        self.master.destroy()

    def create_reservation_tab(self):
        reservation_tab = ttk.Frame(self.notebook)
        self.notebook.add(reservation_tab, text="Reservations")
        customer_label = tk.Label(reservation_tab, text="Customer Name:")
        customer_label.grid(row=0, column=0, padx=10, pady=10)
        customer_entry = tk.Entry(reservation_tab)
        customer_entry.grid(row=0, column=1, padx=10, pady=10)
        contact_label = tk.Label(reservation_tab, text="Contact Number:")
        contact_label.grid(row=1, column=0, padx=10, pady=10)
        contact_entry = tk.Entry(reservation_tab)
        contact_entry.grid(row=1, column=1, padx=10, pady=10)
        duration_label = tk.Label(reservation_tab, text="Tour Duration (days):")
        duration_label.grid(row=2, column=0, padx=10, pady=10)
        duration_entry = tk.Entry(reservation_tab)
        duration_entry.grid(row=2, column=1, padx=10, pady=10)

        destinations_combobox = ttk.Combobox(
            reservation_tab, values=self.get_travel_destinations()
        )
        destinations_combobox.grid(row=3, column=1, padx=10, pady=10)
        destinations = tk.Label(reservation_tab, text="Select Destination:")
        destinations.grid(row=3, column=0, padx=10, pady=10)
        hotel_label = tk.Label(reservation_tab, text="Select Hotel:")
        hotel_label.grid(row=4, column=0, padx=10, pady=10)

        restaurant_label = tk.Label(reservation_tab, text="Select Restaurant:")
        restaurant_label.grid(row=5, column=0, padx=10, pady=10)

        travel_mode_label = tk.Label(reservation_tab, text="Select Travel Mode:")
        travel_mode_label.grid(row=6, column=0, padx=10, pady=10)

        hotels_combobox = ttk.Combobox(reservation_tab, values=[])
        hotels_combobox.grid(row=4, column=1, padx=10, pady=10)

        restaurants_combobox = ttk.Combobox(reservation_tab, values=[])
        restaurants_combobox.grid(row=5, column=1, padx=10, pady=10)

        travel_modes_combobox = ttk.Combobox(reservation_tab, values=[])
        travel_modes_combobox.grid(row=6, column=1, padx=10, pady=10)

        destinations_combobox.bind("<<ComboboxSelected>>", lambda event, arg=(
        hotels_combobox, restaurants_combobox, travel_modes_combobox): self.update_options(event, arg))

        def update_options(self, event, comboboxes):
            selected_destination = event.widget.get()
            if selected_destination:
                hotels_combobox, restaurants_combobox, travel_modes_combobox = comboboxes
                hotels_combobox['values'] = self.get_hotels_by_destination(selected_destination)
                restaurants_combobox['values'] = self.get_restaurants_by_destination(selected_destination)
                travel_modes_combobox['values'] = self.get_travel_modes_by_destination(selected_destination)

        cost_entry = tk.Entry(reservation_tab)
        cost_entry.grid(row=7, column=2, padx=10, pady=10)
        calculate_cost_button = tk.Button(
            reservation_tab,
            text="Calculate Cost",
            command=lambda: self.calculate_and_display_cost(
                customer_entry.get(),
                duration_entry.get(),
                hotels_combobox.get(),
                restaurants_combobox.get(),
                travel_modes_combobox.get(),
                cost_entry,
            ),
        )
        calculate_cost_button.grid(row=7, column=0, columnspan=2, pady=10)
        reserve_button = tk.Button(
            reservation_tab,
            text="Make Reservation",
            command=lambda: self.make_reservation(
                customer_entry.get(),
                contact_entry.get(),
                duration_entry.get(),
                hotels_combobox.get(),
                restaurants_combobox.get(),
                travel_modes_combobox.get(),
                cost_entry.get(),
            ),
        )
        reserve_button.grid(row=8, column=0, columnspan=2, pady=10)
        display_reservations_button = tk.Button(
            reservation_tab,
            text="Display Reservations",
            command=self.display_reservations,
        )
        display_reservations_button.grid(row=9, column=0, columnspan=2, pady=10)
        search_customer_label = tk.Label(
            reservation_tab, text="Search Reservations by Customer:"
        )
        search_customer_label.grid(row=10, column=0, padx=10, pady=10)
        search_customer_entry = tk.Entry(reservation_tab)
        search_customer_entry.grid(row=10, column=1, padx=10, pady=10)
        search_button = tk.Button(
            reservation_tab,
            text="Search Reservations",
            command=lambda: self.display_reservations(search_customer_entry.get()),
        )
        search_button.grid(row=11, column=0, columnspan=2, pady=10)

        def update_options(*args):
            selected_destination = destinations_combobox.get()
            if selected_destination:
                hotels_combobox['values'] = self.get_hotels_by_destination(selected_destination)
                restaurants_combobox['values'] = self.get_restaurants_by_destination(selected_destination)
                travel_modes_combobox['values'] = self.get_travel_modes_by_destination(selected_destination)

        destinations_combobox.bind("<<ComboboxSelected>>", update_options)

    def get_hotels_by_destination(self, destination):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM hotels WHERE location = ?", (destination,))
            hotels = cursor.fetchall()
        return [hotel[0] for hotel in hotels]

    def get_restaurants_by_destination(self, destination):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM restaurants WHERE location = ?", (destination,))
            restaurants = cursor.fetchall()
        return [restaurant[0] for restaurant in restaurants]

    def get_travel_modes_by_destination(self, destination):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT mode FROM travels WHERE destination = ?", (destination,))
            travel_modes = cursor.fetchall()
        return [mode[0] for mode in travel_modes]

    def make_reservation(
            self,
            customer_name,
            contact,
            duration,
            selected_hotel,
            selected_restaurant,
            selected_travel_mode,
            total_cost,
    ):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO reservations (customer_name, contact, duration, hotel, restaurant, travel_mode, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    customer_name,
                    contact,
                    duration,
                    selected_hotel,
                    selected_restaurant,
                    selected_travel_mode,
                    total_cost,
                ),
            )
        print("Reservation made successfully!")

    def delete_reservation(self, reservation_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
        print(f"Reservation with ID {reservation_id} deleted successfully!")

    def display_reservations(self, customer_name=None):
        with self.connection:
            cursor = self.connection.cursor()
            if customer_name:
                cursor.execute(
                    "SELECT * FROM reservations WHERE customer_name=?", (customer_name,)
                )
            else:
                cursor.execute("SELECT * FROM reservations")
            reservations = cursor.fetchall()
        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Reservations")
        for reservation in reservations:
            reservation_frame = ttk.Frame(display_tab)
            reservation_frame.pack(pady=5)

            reservation_label = tk.Label(
                reservation_frame,
                text=f"Customer: {reservation[1]}, Contact: {reservation[2]}, No of days: {reservation[3]}, Hotel: {reservation[4]}, Resturant: {reservation[5]}, Travel Mode: {reservation[6]}",
            )
            reservation_label.pack(side=tk.LEFT)
            delete_button = tk.Button(
                reservation_frame,
                text="Delete",
                command=lambda res_id=reservation[0]: self.delete_reservation(res_id),
            )
            delete_button.pack(side=tk.RIGHT)
        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

    def search_reservations_by_customer(self, customer_name):
        self.display_reservations(customer_name)

    '''def create_user_tab(self):
        user_tab = ttk.Frame(self.notebook)
        self.notebook.add(user_tab, text="Users")

        name_label = tk.Label(user_tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        contact_label = tk.Label(user_tab, text="Contact:")
        contact_label.grid(row=1, column=0, padx=10, pady=10)
        preferences_label = tk.Label(user_tab, text="Preferences:")
        preferences_label.grid(row=2, column=0, padx=10, pady=10)
        name_entry = tk.Entry(user_tab)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        contact_entry = tk.Entry(user_tab)
        contact_entry.grid(row=1, column=1, padx=10, pady=10)
        preferences_entry = tk.Entry(user_tab)
        preferences_entry.grid(row=2, column=1, padx=10, pady=10)
        add_user_button = tk.Button(
            user_tab,
            text="Add User",
            command=lambda: self.add_user_tab(
                name_entry, contact_entry, preferences_entry
            ),
        )
        add_user_button.grid(row=3, column=0, columnspan=2, pady=10)
        display_users_button = tk.Button(
            user_tab, text="Display Users", command=self.display_users
        )
        display_users_button.grid(row=4, column=0, columnspan=2, pady=10)
    def add_user_tab(self, name_entry, contact_entry, preferences_entry):
        name = name_entry.get()
        contact = contact_entry.get()
        preferences = preferences_entry.get()

        try:
            self.add_user(name, contact, preferences)
            print("User added successfully!")
        except Exception as e:
            print(f"Error adding user: {e}")
    def display_users(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Users")
        user_listbox = tk.Listbox(display_tab)
        user_listbox.pack(fill=tk.BOTH, expand=True)
        for user in users:
            user_listbox.insert(tk.END, f"{user[1]} - {user[2]}")
    def add_user(self, name, contact, preferences):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, contact, preferences) VALUES (?, ?, ?)",
                (name, contact, preferences),
            )
    def get_customer_names(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM users")
            customers = cursor.fetchall()
        return [customer[0] for customer in customers]'''

    def calculate_and_display_cost(
            self,
            customer_name,
            tour_duration,
            selected_hotel,
            selected_restaurant,
            selected_travel_mode,
            cost_entry,
    ):
        try:
            if (
                    not selected_hotel
                    or not selected_restaurant
                    or not selected_travel_mode
            ):
                raise ValueError(
                    "Please select a valid hotel, restaurant, and travel mode."
                )

            tour_duration = int(tour_duration)
            hotel_cost = self.get_hotel_cost(selected_hotel)
            restaurant_cost = self.get_restaurant_cost(selected_restaurant)
            travel_mode_cost = self.get_travel_mode_cost(selected_travel_mode)
            total_cost = tour_duration * (
                    hotel_cost + restaurant_cost + travel_mode_cost
            )

            cost_entry.delete(0, tk.END)
            cost_entry.insert(tk.END, str(total_cost))

            total_cost = float(total_cost)

            self.display_cost_receipt(
                customer_name,
                selected_restaurant,
                selected_hotel,
                selected_travel_mode,
                total_cost,
            )
            return total_cost
        except ValueError as ve:
            print(f"Error calculating cost: {ve}")

            return 0.0
        except Exception as e:
            print(f"Error calculating cost: {e}")

            return 0.0

    def display_cost_receipt(
            self, customer_name, restaurant_name, hotel_name, travel_mode, cost
    ):
        receipt_tab = ttk.Frame(self.notebook)
        self.notebook.add(receipt_tab, text="Cost Receipt")
        receipt_text = tk.Text(receipt_tab, wrap=tk.WORD, height=10, width=50)
        receipt_text.insert(tk.END, f"Customer Name: {customer_name}\n")

        receipt_text.insert(
            tk.END, f"Hotel: {hotel_name} - Cost: ${self.get_hotel_cost(hotel_name)}\n"
        )
        receipt_text.insert(
            tk.END,
            f"Restaurant: {restaurant_name} - Cost: ${self.get_restaurant_cost(restaurant_name)}\n",
        )
        receipt_text.insert(
            tk.END,
            f"Travel Mode: {travel_mode} - Cost: ${self.get_travel_mode_cost(travel_mode)}\n",
        )
        receipt_text.insert(tk.END, f"Total Cost: ${cost}\n")
        receipt_text.config(state=tk.DISABLED)
        receipt_text.pack(padx=10, pady=10)

        exit_button = tk.Button(receipt_tab, text="Exit", command=receipt_tab.destroy)
        exit_button.pack(pady=10)

    def get_hotel_cost(self, hotel_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cost FROM hotels WHERE name = ?", (hotel_name,))
            result = cursor.fetchone()
            return (
                float(result[0])
                if result is not None and result[0] is not None
                else 0.0
            )

    def get_restaurant_cost(self, restaurant_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT cost FROM restaurants WHERE name = ?", (restaurant_name,)
            )
            result = cursor.fetchone()
            return float(result[0]) if result else 0.0

    def get_travel_destinations(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT destination FROM travels")
            destinations = cursor.fetchall()
        return [destination[0] for destination in destinations]

    def get_hotel_names(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM hotels")
            hotels = cursor.fetchall()
        return [hotel[0] for hotel in hotels]

    def get_restaurant_names(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM restaurants")
            restaurants = cursor.fetchall()
        return [restaurant[0] for restaurant in restaurants]

    def get_travel_modes(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT destination, mode FROM travels")
            travel_modes = cursor.fetchall()

        unique_modes_by_destination = {}
        for destination, mode in travel_modes:
            if destination not in unique_modes_by_destination:
                unique_modes_by_destination[destination] = set()
            unique_modes_by_destination[destination].add(mode)

        unique_travel_modes = []
        for destination, modes in unique_modes_by_destination.items():
            unique_travel_modes.extend([(destination, mode) for mode in modes])

        return unique_travel_modes

    def get_travel_mode_cost(self, mode_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cost FROM travels WHERE mode = ?", (mode_name,))
            result = cursor.fetchone()
            return float(result[0]) if result else 0.0


class HotelRestaurantTravelWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hotel, Restaurant, and Travel Window")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.connection = sqlite3.connect("tourism.db")
        self.create_tables()
        self.create_hotel_tab()
        self.create_restaurant_tab()
        self.create_travel_tab()

    def create_tables(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    cuisine TEXT,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS hotels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    rating INTEGER,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS travels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destination TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    mode TEXT,
                    cost REAL NOT NULL
                )
            """
            )

    def close_connection(self):
        if self.connection:
            self.connection.close()
        self.master.destroy()

    def add_hotel(self, name, location, rating, cost):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO hotels (name, location, rating, cost) VALUES (?, ?, ?, ?)",
                (name, location, rating, float(cost)),
            )

    def add_hotel_tab(self, name_entry, location_entry, rating_entry, cost_entry):
        name = name_entry.get()
        location = location_entry.get()
        rating = rating_entry.get()
        cost = cost_entry.get()

        try:
            self.add_hotel(name, location, rating, cost)
            print("Hotel added successfully!")
        except Exception as e:
            print(f"Error adding hotel: {e}")

    def create_hotel_tab(self):
        hotel_tab = ttk.Frame(self.notebook)
        self.notebook.add(hotel_tab, text="Hotels")

        name_label = tk.Label(hotel_tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        location_label = tk.Label(hotel_tab, text="Location:")
        location_label.grid(row=1, column=0, padx=10, pady=10)

        rating_label = tk.Label(hotel_tab, text="Rating:")
        rating_label.grid(row=2, column=0, padx=10, pady=10)

        name_entry = tk.Entry(hotel_tab)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        location_entry = tk.Entry(hotel_tab)
        location_entry.grid(row=1, column=1, padx=10, pady=10)

        rating_entry = tk.Entry(hotel_tab)
        rating_entry.grid(row=2, column=1, padx=10, pady=10)

        cost_label = tk.Label(hotel_tab, text="Cost:")
        cost_label.grid(row=3, column=0, padx=10, pady=10)

        cost_entry = tk.Entry(hotel_tab)
        cost_entry.grid(row=3, column=1, padx=10, pady=10)

        add_hotel_button = tk.Button(
            hotel_tab,
            text="Add Hotel",
            command=lambda: self.add_hotel_tab(
                name_entry, location_entry, rating_entry, cost_entry
            ),
        )
        add_hotel_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_hotels_button = tk.Button(
            hotel_tab, text="Display Hotels", command=self.display_hotels
        )
        display_hotels_button.grid(row=5, column=0, columnspan=2, pady=10)

    def delete_hotel(self, hotel_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM hotels WHERE id=?", (hotel_id,))
        print(f"Hotel with ID {hotel_id} deleted successfully!")

    def display_hotels(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, location, rating FROM hotels")
            hotels = cursor.fetchall()

        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Hotels")

        canvas = tk.Canvas(display_tab)
        scrollbar = ttk.Scrollbar(display_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for hotel in hotels:
            hotel_frame = ttk.Frame(scrollable_frame)
            hotel_frame.pack(pady=5)

            hotel_label = tk.Label(
                hotel_frame,
                text=f"Name: {hotel[1]}, Location: {hotel[2]}, Rating: {hotel[3]}",
            )
            hotel_label.pack(side=tk.LEFT)

            delete_button = tk.Button(
                hotel_frame,
                text="Delete",
                command=lambda hotel_id=hotel[0]: self.delete_hotel(hotel_id),
            )
            delete_button.pack(side=tk.RIGHT)

        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_restaurant_tab(self):
        restaurant_tab = ttk.Frame(self.notebook)
        self.notebook.add(restaurant_tab, text="Restaurants")

        name_label = tk.Label(restaurant_tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        location_label = tk.Label(restaurant_tab, text="Location:")
        location_label.grid(row=1, column=0, padx=10, pady=10)

        cuisine_label = tk.Label(restaurant_tab, text="Cuisine:")
        cuisine_label.grid(row=2, column=0, padx=10, pady=10)

        name_entry = tk.Entry(restaurant_tab)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        location_entry = tk.Entry(restaurant_tab)
        location_entry.grid(row=1, column=1, padx=10, pady=10)

        cuisine_entry = tk.Entry(restaurant_tab)
        cuisine_entry.grid(row=2, column=1, padx=10, pady=10)

        cost_label = tk.Label(restaurant_tab, text="Cost:")
        cost_label.grid(row=3, column=0, padx=10, pady=10)

        cost_entry = tk.Entry(restaurant_tab)
        cost_entry.grid(row=3, column=1, padx=10, pady=10)

        add_restaurant_button = tk.Button(
            restaurant_tab,
            text="Add Restaurant",
            command=lambda: self.add_restaurant_tab(
                name_entry, location_entry, cuisine_entry, cost_entry
            ),
        )
        add_restaurant_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_restaurants_button = tk.Button(
            restaurant_tab, text="Display Restaurants", command=self.display_restaurants
        )
        display_restaurants_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_restaurant(self, name, location, cuisine, cost):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO restaurants (name, location, cuisine, cost) VALUES (?, ?, ?, ?)",
                (name, location, cuisine, float(cost)),
            )

    def delete_restaurant(self, restaurant_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM restaurants WHERE id=?", (restaurant_id,))
        print(f"Restaurant with ID {restaurant_id} deleted successfully!")

    def display_restaurants(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, location FROM restaurants")
            restaurants = cursor.fetchall()

        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Restaurants")

        canvas = tk.Canvas(display_tab)
        scrollbar = ttk.Scrollbar(display_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for restaurant in restaurants:
            restaurant_frame = ttk.Frame(scrollable_frame)
            restaurant_frame.pack(pady=5)

            restaurant_label = tk.Label(
                restaurant_frame,
                text=f"Name: {restaurant[1]}, Location: {restaurant[2]}",
            )
            restaurant_label.pack(side=tk.LEFT)

            delete_button = tk.Button(
                restaurant_frame,
                text="Delete",
                command=lambda res_id=restaurant[0]: self.delete_restaurant(res_id),
            )
            delete_button.pack(side=tk.RIGHT)

        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def add_restaurant_tab(self, name_entry, location_entry, cuisine_entry, cost_entry):
        name = name_entry.get()
        location = location_entry.get()
        cuisine = cuisine_entry.get()
        cost = cost_entry.get()

        try:
            self.add_restaurant(name, location, cuisine, cost)
            print("Restaurant added successfully!")
        except Exception as e:
            print(f"Error adding restaurant: {e}")

    def add_travel(self, destination, duration, mode, cost):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO travels (destination, duration, mode, cost) VALUES (?, ?, ?, ?)",
                (destination, duration, mode, float(cost)),
            )

    def delete_travel_record(self, travel_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM travels WHERE id=?", (travel_id,))
        print(f"Travel record with ID {travel_id} deleted successfully!")

    def display_travel_records(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT id, destination, 'date', mode FROM travels"
            )
            travels = cursor.fetchall()

        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Travel Records")

        canvas = tk.Canvas(display_tab)
        scrollbar = ttk.Scrollbar(display_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for travel in travels:
            travel_frame = ttk.Frame(scrollable_frame)
            travel_frame.pack(pady=5)

            travel_label = tk.Label(
                travel_frame,
                text=f"Destination: {travel[1]}, Date: {travel[2]}, Mode: {travel[3]}",
            )
            travel_label.pack(side=tk.LEFT)

            delete_button = tk.Button(
                travel_frame,
                text="Delete",
                command=lambda travel_id=travel[0]: self.delete_travel_record(
                    travel_id
                ),
            )
            delete_button.pack(side=tk.RIGHT)

        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_travel_tab(self):
        travel_tab = ttk.Frame(self.notebook)
        self.notebook.add(travel_tab, text="Travel")

        destination_label = tk.Label(travel_tab, text="Destination:")
        destination_label.grid(row=0, column=0, padx=10, pady=10)

        duration_label = tk.Label(travel_tab, text="Duration:")
        duration_label.grid(row=1, column=0, padx=10, pady=10)

        mode_label = tk.Label(travel_tab, text="Mode of Transportation:")
        mode_label.grid(row=2, column=0, padx=10, pady=10)

        destination_entry = tk.Entry(travel_tab)
        destination_entry.grid(row=0, column=1, padx=10, pady=10)

        duration_entry = tk.Entry(travel_tab)
        duration_entry.grid(row=1, column=1, padx=10, pady=10)

        mode_entry = tk.Entry(travel_tab)
        mode_entry.grid(row=2, column=1, padx=10, pady=10)

        cost_label = tk.Label(travel_tab, text="Cost:")
        cost_label.grid(row=3, column=0, padx=10, pady=10)

        cost_entry = tk.Entry(travel_tab)
        cost_entry.grid(row=3, column=1, padx=10, pady=10)

        add_travel_button = tk.Button(
            travel_tab,
            text="Add Travel Mode",
            command=lambda: self.add_travel_tab(
                destination_entry, duration_entry, mode_entry, cost_entry
            ),
        )
        add_travel_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_travel_button = tk.Button(
            travel_tab,
            text="Display Travel Records",
            command=self.display_travel_records,
        )
        display_travel_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_travel_tab(self, destination_entry, duration_entry, mode_entry, cost_entry):
        destination = destination_entry.get()
        duration = duration_entry.get()
        mode = mode_entry.get()
        cost = cost_entry.get()

        try:
            self.add_travel(destination, duration, mode, cost)
            print("Travel record added successfully!")
        except Exception as e:
            print(f"Error adding travel record: {e}")


class MainPage:
    def __init__(self, master=None):
        if master is None:
            master = tk.Tk()
        self.master = master
        self.master.title("Main Page")
        self.master.geometry("400x200")

        # Load the background image using PIL
        image = Image.open("beach.png")  # Change to the actual image file path
        self.bg_image = ImageTk.PhotoImage(image)

        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(master, text="Choose an Interface:")
        self.label.pack(pady=20)

        self.user_button = tk.Button(
            master, text="User Interface", command=self.open_user_interface
        )
        self.user_button.pack(pady=10)

        self.reservation_button = tk.Button(
            master,
            text="Reservation Interface",
            command=self.open_reservation_interface,
        )
        self.reservation_button.pack(pady=10)

    def open_user_interface(self):
        self.master.destroy()
        root = tk.Tk()
        hotel_restaurant_travel_window = HotelRestaurantTravelWindow(root)
        root.mainloop()

    def open_reservation_interface(self):
        self.master.destroy()
        root = tk.Tk()
        reservation_user_window = ReservationUserWindow(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(root)
    root.mainloop()


class ReservationUserWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Reservation and User Window")
        self.notebook = ttk.Notebook(self.master)
        background_image = Image.open("beach.png")  # Replace with your image file
        background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image
        background_label = tk.Label(self.master, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.connection = sqlite3.connect("tourism.db")
        self.create_tables()
        self.create_reservation_tab()
        customer_label = tk.Label(self.master, text="Customer Name:")
        customer_label.place(in_=background_label, x=10, y=10)

    def create_tables(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT NOT NULL,
                    contact TEXT NOT NULL,  -- Add this line
                    duration TEXT NOT NULL,
                    hotel TEXT NOT NULL,
                    restaurant TEXT NOT NULL,
                    travel_mode TEXT NOT NULL,
                    total_cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    cuisine TEXT,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS hotels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    rating INTEGER,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS travels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destination TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    mode TEXT,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    contact TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL
                )
                """
            )
    def close_connection(self):
        if self.connection:
            self.connection.close()
        self.master.destroy()  
    def create_reservation_tab(self):
        reservation_tab = ttk.Frame(self.notebook)
        self.notebook.add(reservation_tab, text="Reservations")
        customer_label = tk.Label(reservation_tab, text="Customer Name:")
        customer_label.grid(row=0, column=0, padx=10, pady=10)
        customer_entry = tk.Entry(reservation_tab)
        customer_entry.grid(row=0, column=1, padx=10, pady=10)
        contact_label = tk.Label(reservation_tab, text="Contact Number:")
        contact_label.grid(row=1, column=0, padx=10, pady=10)
        contact_entry = tk.Entry(reservation_tab)
        contact_entry.grid(row=1, column=1, padx=10, pady=10)
        duration_label = tk.Label(reservation_tab, text="Tour Duration (days):")
        duration_label.grid(row=2, column=0, padx=10, pady=10)
        duration_entry = tk.Entry(reservation_tab)
        duration_entry.grid(row=2, column=1, padx=10, pady=10)
        
        destinations_combobox = ttk.Combobox(
        reservation_tab, values=self.get_travel_destinations()
    )
        destinations_combobox.grid(row=3, column=1, padx=10, pady=10)
        destinations = tk.Label(reservation_tab, text="Select Destination:")
        destinations.grid(row=3, column=0, padx=10, pady=10)
        hotel_label = tk.Label(reservation_tab, text="Select Hotel:")
        hotel_label.grid(row=4, column=0, padx=10, pady=10)

        restaurant_label = tk.Label(reservation_tab, text="Select Restaurant:")
        restaurant_label.grid(row=5, column=0, padx=10, pady=10)

        travel_mode_label = tk.Label(reservation_tab, text="Select Travel Mode:")
        travel_mode_label.grid(row=6, column=0, padx=10, pady=10)
       
        hotels_combobox = ttk.Combobox(reservation_tab, values=[])
        hotels_combobox.grid(row=4, column=1, padx=10, pady=10)

        restaurants_combobox = ttk.Combobox(reservation_tab, values=[])
        restaurants_combobox.grid(row=5, column=1, padx=10, pady=10)

        travel_modes_combobox = ttk.Combobox(reservation_tab, values=[])
        travel_modes_combobox.grid(row=6, column=1, padx=10, pady=10)

        
        destinations_combobox.bind("<<ComboboxSelected>>", lambda event, arg=(hotels_combobox, restaurants_combobox, travel_modes_combobox): self.update_options(event, arg))
        
        def update_options(self, event, comboboxes):
            selected_destination = event.widget.get()
            if selected_destination:
                hotels_combobox, restaurants_combobox, travel_modes_combobox = comboboxes
                hotels_combobox['values'] = self.get_hotels_by_destination(selected_destination)
                restaurants_combobox['values'] = self.get_restaurants_by_destination(selected_destination)
                travel_modes_combobox['values'] = self.get_travel_modes_by_destination(selected_destination)

        cost_entry = tk.Entry(reservation_tab)
        cost_entry.grid(row=7, column=2, padx=10, pady=10)
        calculate_cost_button = tk.Button(
            reservation_tab,
            text="Calculate Cost",
            command=lambda: self.calculate_and_display_cost(
                customer_entry.get(),
                duration_entry.get(),
                hotels_combobox.get(),
                restaurants_combobox.get(),
                travel_modes_combobox.get(),
                cost_entry,
            ),
        )
        calculate_cost_button.grid(row=7, column=0, columnspan=2, pady=10)
        reserve_button = tk.Button(
            reservation_tab,
            text="Make Reservation",
            command=lambda: self.make_reservation(
                customer_entry.get(),
                contact_entry.get(),
                duration_entry.get(),
                hotels_combobox.get(),
                restaurants_combobox.get(),
                travel_modes_combobox.get(),
                cost_entry.get(),
            ),
        )
        reserve_button.grid(row=8, column=0, columnspan=2, pady=10)
        display_reservations_button = tk.Button(
            reservation_tab,
            text="Display Reservations",
            command=self.display_reservations,
        )
        display_reservations_button.grid(row=9, column=0, columnspan=2, pady=10)
        search_customer_label = tk.Label(
            reservation_tab, text="Search Reservations by Customer:"
        )
        search_customer_label.grid(row=10, column=0, padx=10, pady=10)
        search_customer_entry = tk.Entry(reservation_tab)
        search_customer_entry.grid(row=10, column=1, padx=10, pady=10)
        search_button = tk.Button(
            reservation_tab,
            text="Search Reservations",
            command=lambda: self.display_reservations(search_customer_entry.get()),
        )
        search_button.grid(row=11, column=0, columnspan=2, pady=10)
        def update_options(*args):
            selected_destination = destinations_combobox.get()
            if selected_destination:
                hotels_combobox['values'] = self.get_hotels_by_destination(selected_destination)
                restaurants_combobox['values'] = self.get_restaurants_by_destination(selected_destination)
                travel_modes_combobox['values'] = self.get_travel_modes_by_destination(selected_destination)

        destinations_combobox.bind("<<ComboboxSelected>>", update_options)

    def get_hotels_by_destination(self, destination):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM hotels WHERE location = ?", (destination,))
            hotels = cursor.fetchall()
        return [hotel[0] for hotel in hotels]

    def get_restaurants_by_destination(self, destination):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM restaurants WHERE location = ?", (destination,))
            restaurants = cursor.fetchall()
        return [restaurant[0] for restaurant in restaurants]

    def get_travel_modes_by_destination(self, destination):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT mode FROM travels WHERE destination = ?", (destination,))
            travel_modes = cursor.fetchall()
        return [mode[0] for mode in travel_modes]    
    def make_reservation(
        self,
        customer_name,
        contact,
        duration,
        selected_hotel,
        selected_restaurant,
        selected_travel_mode,
        total_cost,
    ):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO reservations (customer_name, contact, duration, hotel, restaurant, travel_mode, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    customer_name,
                    contact,
                    duration,
                    selected_hotel,
                    selected_restaurant,
                    selected_travel_mode,
                    total_cost,
                ),
            )
        print("Reservation made successfully!")
    
    def delete_reservation(self, reservation_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
        print(f"Reservation with ID {reservation_id} deleted successfully!")
    def display_reservations(self, customer_name=None):
        with self.connection:
            cursor = self.connection.cursor()
            if customer_name:
                cursor.execute(
                    "SELECT * FROM reservations WHERE customer_name=?", (customer_name,)
                )
            else:
                cursor.execute("SELECT * FROM reservations")
            reservations = cursor.fetchall()
        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Reservations")
        for reservation in reservations:
            reservation_frame = ttk.Frame(display_tab)
            reservation_frame.pack(pady=5)

            reservation_label = tk.Label(
                reservation_frame,
                text=f"Customer: {reservation[1]}, Contact: {reservation[2]}, No of days: {reservation[3]}, Hotel: {reservation[4]}, Resturant: {reservation[5]}, Travel Mode: {reservation[6]}",
            )
            reservation_label.pack(side=tk.LEFT)
            delete_button = tk.Button(
                reservation_frame,
                text="Delete",
                command=lambda res_id=reservation[0]: self.delete_reservation(res_id),
            )
            delete_button.pack(side=tk.RIGHT)
        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)
    def search_reservations_by_customer(self, customer_name):
        self.display_reservations(customer_name)
    '''def create_user_tab(self):
        user_tab = ttk.Frame(self.notebook)
        self.notebook.add(user_tab, text="Users")
        
        name_label = tk.Label(user_tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        contact_label = tk.Label(user_tab, text="Contact:")
        contact_label.grid(row=1, column=0, padx=10, pady=10)
        preferences_label = tk.Label(user_tab, text="Preferences:")
        preferences_label.grid(row=2, column=0, padx=10, pady=10)
        name_entry = tk.Entry(user_tab)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        contact_entry = tk.Entry(user_tab)
        contact_entry.grid(row=1, column=1, padx=10, pady=10)
        preferences_entry = tk.Entry(user_tab)
        preferences_entry.grid(row=2, column=1, padx=10, pady=10)
        add_user_button = tk.Button(
            user_tab,
            text="Add User",
            command=lambda: self.add_user_tab(
                name_entry, contact_entry, preferences_entry
            ),
        )
        add_user_button.grid(row=3, column=0, columnspan=2, pady=10)
        display_users_button = tk.Button(
            user_tab, text="Display Users", command=self.display_users
        )
        display_users_button.grid(row=4, column=0, columnspan=2, pady=10)
    def add_user_tab(self, name_entry, contact_entry, preferences_entry):
        name = name_entry.get()
        contact = contact_entry.get()
        preferences = preferences_entry.get()
        
        try:
            self.add_user(name, contact, preferences)
            print("User added successfully!")
        except Exception as e:
            print(f"Error adding user: {e}")
    def display_users(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Users")
        user_listbox = tk.Listbox(display_tab)
        user_listbox.pack(fill=tk.BOTH, expand=True)
        for user in users:
            user_listbox.insert(tk.END, f"{user[1]} - {user[2]}")
    def add_user(self, name, contact, preferences):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, contact, preferences) VALUES (?, ?, ?)",
                (name, contact, preferences),
            )
    def get_customer_names(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM users")
            customers = cursor.fetchall()
        return [customer[0] for customer in customers]'''
    def calculate_and_display_cost(
        self,
        customer_name,
        tour_duration,
        selected_hotel,
        selected_restaurant,
        selected_travel_mode,
        cost_entry,
    ):
        try:
            if (
                not selected_hotel
                or not selected_restaurant
                or not selected_travel_mode
            ):
                raise ValueError(
                    "Please select a valid hotel, restaurant, and travel mode."
                )
            
            tour_duration = int(tour_duration)
            hotel_cost = self.get_hotel_cost(selected_hotel)
            restaurant_cost = self.get_restaurant_cost(selected_restaurant)
            travel_mode_cost = self.get_travel_mode_cost(selected_travel_mode)
            total_cost = tour_duration * (
                hotel_cost + restaurant_cost + travel_mode_cost
            )
            
            cost_entry.delete(0, tk.END)
            cost_entry.insert(tk.END, str(total_cost))
            
            total_cost = float(total_cost)
            
            self.display_cost_receipt(
                customer_name,
                selected_restaurant,
                selected_hotel,
                selected_travel_mode,
                total_cost,
            )
            return total_cost
        except ValueError as ve:
            print(f"Error calculating cost: {ve}")
            
            return 0.0
        except Exception as e:
            print(f"Error calculating cost: {e}")
            
            return 0.0
    def display_cost_receipt(
        self, customer_name, restaurant_name, hotel_name, travel_mode, cost
    ):
        receipt_tab = ttk.Frame(self.notebook)
        self.notebook.add(receipt_tab, text="Cost Receipt")
        receipt_text = tk.Text(receipt_tab, wrap=tk.WORD, height=10, width=50)
        receipt_text.insert(tk.END, f"Customer Name: {customer_name}\n")
        
        receipt_text.insert(
            tk.END, f"Hotel: {hotel_name} - Cost: ${self.get_hotel_cost(hotel_name)}\n"
        )
        receipt_text.insert(
            tk.END,
            f"Restaurant: {restaurant_name} - Cost: ${self.get_restaurant_cost(restaurant_name)}\n",
        )
        receipt_text.insert(
            tk.END,
            f"Travel Mode: {travel_mode} - Cost: ${self.get_travel_mode_cost(travel_mode)}\n",
        )
        receipt_text.insert(tk.END, f"Total Cost: ${cost}\n")
        receipt_text.config(state=tk.DISABLED) 
        receipt_text.pack(padx=10, pady=10)
        
        exit_button = tk.Button(receipt_tab, text="Exit", command=receipt_tab.destroy)
        exit_button.pack(pady=10)
    def get_hotel_cost(self, hotel_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cost FROM hotels WHERE name = ?", (hotel_name,))
            result = cursor.fetchone()
            return (
                float(result[0])
                if result is not None and result[0] is not None
                else 0.0
            )
    def get_restaurant_cost(self, restaurant_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT cost FROM restaurants WHERE name = ?", (restaurant_name,)
            )
            result = cursor.fetchone()
            return float(result[0]) if result else 0.0
        
    def get_travel_destinations(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT destination FROM travels")
            destinations = cursor.fetchall()
        return [destination[0] for destination in destinations]

    def get_hotel_names(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM hotels")
            hotels = cursor.fetchall()
        return [hotel[0] for hotel in hotels]
    def get_restaurant_names(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM restaurants")
            restaurants = cursor.fetchall()
        return [restaurant[0] for restaurant in restaurants]
    
    def get_travel_modes(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT destination, mode FROM travels")
            travel_modes = cursor.fetchall()

        unique_modes_by_destination = {}
        for destination, mode in travel_modes:
            if destination not in unique_modes_by_destination:
                unique_modes_by_destination[destination] = set()
            unique_modes_by_destination[destination].add(mode)

        unique_travel_modes = []
        for destination, modes in unique_modes_by_destination.items():
            unique_travel_modes.extend([(destination, mode) for mode in modes])

        return unique_travel_modes


    def get_travel_mode_cost(self, mode_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cost FROM travels WHERE mode = ?", (mode_name,))
            result = cursor.fetchone()
            return float(result[0]) if result else 0.0


class HotelRestaurantTravelWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hotel, Restaurant, and Travel Window")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.connection = sqlite3.connect("tourism.db")
        self.create_tables()
        self.create_hotel_tab()
        self.create_restaurant_tab()
        self.create_travel_tab()

    def create_tables(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    cuisine TEXT,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS hotels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    rating INTEGER,
                    cost REAL NOT NULL
                )
            """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS travels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destination TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    mode TEXT,
                    cost REAL NOT NULL
                )
            """
            )

    def close_connection(self):
        if self.connection:
            self.connection.close()
        self.master.destroy()  

    def add_hotel(self, name, location, rating, cost):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO hotels (name, location, rating, cost) VALUES (?, ?, ?, ?)",
                (name, location, rating, float(cost)),
            )

    def add_hotel_tab(self, name_entry, location_entry, rating_entry, cost_entry):
        name = name_entry.get()
        location = location_entry.get()
        rating = rating_entry.get()
        cost = cost_entry.get()

        try:
            self.add_hotel(name, location, rating, cost)
            print("Hotel added successfully!")
        except Exception as e:
            print(f"Error adding hotel: {e}")

    def create_hotel_tab(self):
        hotel_tab = ttk.Frame(self.notebook)
        self.notebook.add(hotel_tab, text="Hotels")

        name_label = tk.Label(hotel_tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        location_label = tk.Label(hotel_tab, text="Location:")
        location_label.grid(row=1, column=0, padx=10, pady=10)

        rating_label = tk.Label(hotel_tab, text="Rating:")
        rating_label.grid(row=2, column=0, padx=10, pady=10)

        name_entry = tk.Entry(hotel_tab)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        location_entry = tk.Entry(hotel_tab)
        location_entry.grid(row=1, column=1, padx=10, pady=10)

        rating_entry = tk.Entry(hotel_tab)
        rating_entry.grid(row=2, column=1, padx=10, pady=10)

        cost_label = tk.Label(hotel_tab, text="Cost:")
        cost_label.grid(row=3, column=0, padx=10, pady=10)

        cost_entry = tk.Entry(hotel_tab)
        cost_entry.grid(row=3, column=1, padx=10, pady=10)

        add_hotel_button = tk.Button(
            hotel_tab,
            text="Add Hotel",
            command=lambda: self.add_hotel_tab(
                name_entry, location_entry, rating_entry, cost_entry
            ),
        )
        add_hotel_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_hotels_button = tk.Button(
            hotel_tab, text="Display Hotels", command=self.display_hotels
        )
        display_hotels_button.grid(row=5, column=0, columnspan=2, pady=10)

    def delete_hotel(self, hotel_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM hotels WHERE id=?", (hotel_id,))
        print(f"Hotel with ID {hotel_id} deleted successfully!")

    def display_hotels(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, location, rating FROM hotels")
            hotels = cursor.fetchall()

        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Hotels")

        canvas = tk.Canvas(display_tab)
        scrollbar = ttk.Scrollbar(display_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for hotel in hotels:
            hotel_frame = ttk.Frame(scrollable_frame)
            hotel_frame.pack(pady=5)

            hotel_label = tk.Label(
                hotel_frame,
                text=f"Name: {hotel[1]}, Location: {hotel[2]}, Rating: {hotel[3]}",
            )
            hotel_label.pack(side=tk.LEFT)

            delete_button = tk.Button(
                hotel_frame,
                text="Delete",
                command=lambda hotel_id=hotel[0]: self.delete_hotel(hotel_id),
            )
            delete_button.pack(side=tk.RIGHT)

        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


    def create_restaurant_tab(self):
        restaurant_tab = ttk.Frame(self.notebook)
        self.notebook.add(restaurant_tab, text="Restaurants")

        name_label = tk.Label(restaurant_tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)

        location_label = tk.Label(restaurant_tab, text="Location:")
        location_label.grid(row=1, column=0, padx=10, pady=10)

        cuisine_label = tk.Label(restaurant_tab, text="Cuisine:")
        cuisine_label.grid(row=2, column=0, padx=10, pady=10)

        name_entry = tk.Entry(restaurant_tab)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        location_entry = tk.Entry(restaurant_tab)
        location_entry.grid(row=1, column=1, padx=10, pady=10)

        cuisine_entry = tk.Entry(restaurant_tab)
        cuisine_entry.grid(row=2, column=1, padx=10, pady=10)

        cost_label = tk.Label(restaurant_tab, text="Cost:")
        cost_label.grid(row=3, column=0, padx=10, pady=10)

        cost_entry = tk.Entry(restaurant_tab)
        cost_entry.grid(row=3, column=1, padx=10, pady=10)

        add_restaurant_button = tk.Button(
            restaurant_tab,
            text="Add Restaurant",
            command=lambda: self.add_restaurant_tab(
                name_entry, location_entry, cuisine_entry, cost_entry
            ),
        )
        add_restaurant_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_restaurants_button = tk.Button(
            restaurant_tab, text="Display Restaurants", command=self.display_restaurants
        )
        display_restaurants_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_restaurant(self, name, location, cuisine, cost):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO restaurants (name, location, cuisine, cost) VALUES (?, ?, ?, ?)",
                (name, location, cuisine, float(cost)),
            )

    def delete_restaurant(self, restaurant_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM restaurants WHERE id=?", (restaurant_id,))
        print(f"Restaurant with ID {restaurant_id} deleted successfully!")

    def display_restaurants(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, name, location FROM restaurants")
            restaurants = cursor.fetchall()

        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Restaurants")

        canvas = tk.Canvas(display_tab)
        scrollbar = ttk.Scrollbar(display_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for restaurant in restaurants:
            restaurant_frame = ttk.Frame(scrollable_frame)
            restaurant_frame.pack(pady=5)

            restaurant_label = tk.Label(
                restaurant_frame,
                text=f"Name: {restaurant[1]}, Location: {restaurant[2]}",
            )
            restaurant_label.pack(side=tk.LEFT)

            delete_button = tk.Button(
                restaurant_frame,
                text="Delete",
                command=lambda res_id=restaurant[0]: self.delete_restaurant(res_id),
            )
            delete_button.pack(side=tk.RIGHT)

        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def add_restaurant_tab(self, name_entry, location_entry, cuisine_entry, cost_entry):
        name = name_entry.get()
        location = location_entry.get()
        cuisine = cuisine_entry.get()
        cost = cost_entry.get()

        try:
            self.add_restaurant(name, location, cuisine, cost)
            print("Restaurant added successfully!")
        except Exception as e:
            print(f"Error adding restaurant: {e}")

    def add_travel(self, destination, duration, mode, cost):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO travels (destination, duration, mode, cost) VALUES (?, ?, ?, ?)",
                (destination, duration, mode, float(cost)),
            )

    def delete_travel_record(self, travel_id):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM travels WHERE id=?", (travel_id,))
        print(f"Travel record with ID {travel_id} deleted successfully!")

    def display_travel_records(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT id, destination, 'date', mode FROM travels"
            )
            travels = cursor.fetchall()

        display_tab = ttk.Frame(self.notebook)
        self.notebook.add(display_tab, text="Display Travel Records")

        canvas = tk.Canvas(display_tab)
        scrollbar = ttk.Scrollbar(display_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for travel in travels:
            travel_frame = ttk.Frame(scrollable_frame)
            travel_frame.pack(pady=5)

            travel_label = tk.Label(
                travel_frame,
                text=f"Destination: {travel[1]}, Date: {travel[2]}, Mode: {travel[3]}",
            )
            travel_label.pack(side=tk.LEFT)

            delete_button = tk.Button(
                travel_frame,
                text="Delete",
                command=lambda travel_id=travel[0]: self.delete_travel_record(
                    travel_id
                ),
            )
            delete_button.pack(side=tk.RIGHT)

        exit_button = tk.Button(display_tab, text="Exit", command=display_tab.destroy)
        exit_button.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    def create_travel_tab(self):
        travel_tab = ttk.Frame(self.notebook)
        self.notebook.add(travel_tab, text="Travel")

        destination_label = tk.Label(travel_tab, text="Destination:")
        destination_label.grid(row=0, column=0, padx=10, pady=10)

        duration_label = tk.Label(travel_tab, text="Duration:")
        duration_label.grid(row=1, column=0, padx=10, pady=10)

        mode_label = tk.Label(travel_tab, text="Mode of Transportation:")
        mode_label.grid(row=2, column=0, padx=10, pady=10)

        destination_entry = tk.Entry(travel_tab)
        destination_entry.grid(row=0, column=1, padx=10, pady=10)

        duration_entry = tk.Entry(travel_tab)
        duration_entry.grid(row=1, column=1, padx=10, pady=10)

        mode_entry = tk.Entry(travel_tab)
        mode_entry.grid(row=2, column=1, padx=10, pady=10)

        cost_label = tk.Label(travel_tab, text="Cost:")
        cost_label.grid(row=3, column=0, padx=10, pady=10)

        cost_entry = tk.Entry(travel_tab)
        cost_entry.grid(row=3, column=1, padx=10, pady=10)

        add_travel_button = tk.Button(
            travel_tab,
            text="Add Travel Mode",
            command=lambda: self.add_travel_tab(
                destination_entry, duration_entry, mode_entry, cost_entry
            ),
        )
        add_travel_button.grid(row=4, column=0, columnspan=2, pady=10)

        display_travel_button = tk.Button(
            travel_tab,
            text="Display Travel Records",
            command=self.display_travel_records,
        )
        display_travel_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_travel_tab(self, destination_entry, duration_entry, mode_entry, cost_entry):
        destination = destination_entry.get()
        duration = duration_entry.get()
        mode = mode_entry.get()
        cost = cost_entry.get()

        try:
            self.add_travel(destination, duration, mode, cost)
            print("Travel record added successfully!")
        except Exception as e:
            print(f"Error adding travel record: {e}")


class MainPage:
    def __init__(self, master=None):
        if master is None:
            master = tk.Tk()
        self.master = master
        self.master.title("Main Page")
        self.master.geometry("400x200")

        # Load the background image using PIL
        image = Image.open("beach.png")  # Change to the actual image file path
        self.bg_image = ImageTk.PhotoImage(image)

        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(master, text="Choose an Interface:")
        self.label.pack(pady=20)

        self.user_button = tk.Button(
            master, text="User Interface", command=self.open_user_interface
        )
        self.user_button.pack(pady=10)

        self.reservation_button = tk.Button(
            master,
            text="Reservation Interface",
            command=self.open_reservation_interface,
        )
        self.reservation_button.pack(pady=10)

    def open_user_interface(self):
        self.master.destroy()
        root = tk.Tk()
        hotel_restaurant_travel_window = HotelRestaurantTravelWindow(root)
        root.mainloop()

    def open_reservation_interface(self):
        self.master.destroy()
        root = tk.Tk()
        reservation_user_window = ReservationUserWindow(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(root)
    root.mainloop()

