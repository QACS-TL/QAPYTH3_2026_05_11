class Car:
    def __init__(self, top_speed, current_speed, make, model):
        self._top_speed = 0
        self._current_speed = 0
        self.make = make
        self.model = model

        # Use setters to enforce validation
        self.top_speed = top_speed
        self.current_speed = current_speed

    # ---- TOP SPEED PROPERTY ----
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

    # ---- CURRENT SPEED PROPERTY ----
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


# Dictionary storing cars
cars = {
    "AB12CDE": Car(180, 70, "Ford", "Focus"),
    "XY34ZRT": Car(200, 90, "BMW", "320i"),
    "LM56OPQ": Car(160, 60, "Toyota", "Corolla"),
    "GH78JKL": Car(220, 100, "Audi", "A4")
}

# Road order
road = ["AB12CDE", "XY34ZRT", "LM56OPQ", "GH78JKL"]


def display_road():
    print("\n--- Current Road ---")
    for i, plate in enumerate(road):
        print(f"Position {i + 1}: {plate} ({cars[plate]})")


def attempt_overtake():
    display_road()
    plate = input("\nEnter car registration: ").strip()

    if plate not in road:
        print("Car not found.")
        return

    index = road.index(plate)

    if index == 0:
        print("Already at the front.")
        return

    front_plate = road[index - 1]
    car = cars[plate]
    front_car = cars[front_plate]

    if car.top_speed > front_car.current_speed:
        road[index], road[index - 1] = road[index - 1], road[index]
        print(f"{plate} overtook {front_plate}")
    else:
        print("Overtake failed")

    display_road()


def add_car():
    print("\n--- Add New Car ---")
    plate = input("Registration: ").strip()

    if plate in cars:
        print("Already exists.")
        return

    make = input("Make: ")
    model = input("Model: ")

    try:
        top_speed = int(input("Top speed: "))
        current_speed = int(input("Current speed: "))

        new_car = Car(top_speed, current_speed, make, model)

        cars[plate] = new_car
        road.append(plate)

        print("Car added successfully.")

    except ValueError as e:
        print(f"Error: {e}")


def menu():
    while True:
        print("\n==== Car Simulation ====")
        print("1. View road")
        print("2. Attempt overtake")
        print("3. Add car")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            display_road()
        elif choice == "2":
            attempt_overtake()
        elif choice == "3":
            add_car()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()