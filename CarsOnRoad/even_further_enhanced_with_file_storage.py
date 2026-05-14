class Car:
    def __init__(self, top_speed, current_speed, make, model):
        self._top_speed = 0
        self._current_speed = 0
        self.make = make
        self.model = model

        self.top_speed = top_speed
        self.current_speed = current_speed

    @property
    def top_speed(self):
        return self._top_speed

    @top_speed.setter
    def top_speed(self, value):
        if value < 0:
            raise ValueError("Top speed cannot be negative.")
        if self._current_speed > value:
            raise ValueError("Top speed cannot be less than current speed.")
        self._top_speed = value

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value < 0:
            raise ValueError("Current speed cannot be negative.")
        if value > self._top_speed:
            raise ValueError("Current speed cannot exceed top speed.")
        self._current_speed = value

    def __str__(self):
        return f"{self.make} {self.model} | Top: {self.top_speed} | Current: {self.current_speed}"


# ---- FILE ----
FILE_NAME = "cars_data.csv"


# ---- SAVE TO CSV ----
def save_data(cars, road):
    with open(FILE_NAME, "w") as f:
        # Header
        f.write("plate,top_speed,current_speed,make,model\n")

        # Car data
        for plate, car in cars.items():
            line = f"{plate},{car.top_speed},{car.current_speed},{car.make},{car.model}\n"
            f.write(line)

        # Road order (special row)
        f.write("ROAD," + ",".join(road) + "\n")

    print("Data saved (CSV).")


# ---- LOAD FROM CSV ----
def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No file found. Using default data.")
        return create_default_data()

    cars = {}
    road = []

    # Skip header
    for line in lines[1:]:
        line = line.strip()
        parts = line.split(",")

        if parts[0] == "ROAD":
            road = parts[1:]
        else:
            plate = parts[0]
            top_speed = int(parts[1])
            current_speed = int(parts[2])
            make = parts[3]
            model = parts[4]

            cars[plate] = Car(top_speed, current_speed, make, model)

    print("Data loaded (CSV).")
    return cars, road


# ---- DEFAULT DATA ----
def create_default_data():
    cars = {
        "AB12CDE": Car(180, 70, "Ford", "Focus"),
        "XY34ZRT": Car(200, 90, "BMW", "320i"),
        "LM56OPQ": Car(160, 60, "Toyota", "Corolla"),
        "GH78JKL": Car(220, 100, "Audi", "A4")
    }

    road = list(cars.keys())
    return cars, road


# ---- FUNCTIONALITY ----
def display_road(cars, road):
    print("\n--- Current Road ---")
    for i, plate in enumerate(road):
        print(f"{i + 1}: {plate} ({cars[plate]})")


def attempt_overtake(cars, road):
    display_road(cars, road)
    plate = input("Enter car registration: ").strip()

    if plate not in road:
        print("Car not found.")
        return

    index = road.index(plate)

    if index == 0:
        print("Already at front.")
        return

    front_plate = road[index - 1]

    if cars[plate].top_speed > cars[front_plate].current_speed:
        road[index], road[index - 1] = road[index - 1], road[index]
        print(f"{plate} overtook {front_plate}")
    else:
        print("Overtake failed")


def add_car(cars, road):
    plate = input("Registration: ").strip()

    if plate in cars:
        print("Already exists.")
        return

    make = input("Make: ")
    model = input("Model: ")

    try:
        top_speed = int(input("Top speed: "))
        current_speed = int(input("Current speed: "))

        car = Car(top_speed, current_speed, make, model)

        cars[plate] = car
        road.append(plate)

        print("Car added.")

    except ValueError as e:
        print(f"{e}")


def menu():
    cars, road = load_data()

    while True:
        print("\n==== Car Simulation ====")
        print("1. View road")
        print("2. Attempt overtake")
        print("3. Add car")
        print("4. Save")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            display_road(cars, road)
        elif choice == "2":
            attempt_overtake(cars, road)
        elif choice == "3":
            add_car(cars, road)
        elif choice == "4":
            save_data(cars, road)
        elif choice == "5":
            save_data(cars, road)
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()