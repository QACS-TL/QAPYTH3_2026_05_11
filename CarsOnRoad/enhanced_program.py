# Car class definition
class Car:
    def __init__(self, top_speed, current_speed, make, model):
        if current_speed > top_speed:
            raise ValueError("Current speed cannot exceed top speed.")
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.make = make
        self.model = model

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
        print("Car is already at the front.")
        return

    front_plate = road[index - 1]
    car = cars[plate]
    front_car = cars[front_plate]

    print(f"\nAttempting overtake...")

    if car.top_speed > front_car.current_speed:
        road[index], road[index - 1] = road[index - 1], road[index]
        print(f"{plate} overtook {front_plate}")
    else:
        print("Overtake failed (insufficient speed)")

    display_road()


def add_car():
    print("\n--- Add New Car ---")
    plate = input("Enter registration plate: ").strip()

    if plate in cars:
        print("This registration already exists.")
        return

    make = input("Enter make: ")
    model = input("Enter model: ")

    try:
        top_speed = int(input("Enter top speed: "))
        current_speed = int(input("Enter current speed: "))

        if current_speed > top_speed:
            print("Current speed cannot be greater than top speed.")
            return

        new_car = Car(top_speed, current_speed, make, model)

        # Add to dictionary and road
        cars[plate] = new_car
        road.append(plate)

        print(f"Car {plate} added successfully at the end of the queue.")

    except ValueError:
        print("Invalid input. Please enter numeric values for speeds.")


def menu():
    while True:
        print("\n==== Car Road Simulation ====")
        print("1. View road")
        print("2. Attempt overtake")
        print("3. Add new car")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_road()
        elif choice == "2":
            attempt_overtake()
        elif choice == "3":
            add_car()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# Run program
if __name__ == "__main__":
    menu()
