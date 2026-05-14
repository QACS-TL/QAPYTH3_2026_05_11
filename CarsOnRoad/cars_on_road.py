# Car Road Simulation

# Dictionary storing car details
# Format: reg_plate: [top_speed, current_speed, make, model]
cars = {
    "AB12CDE": [80, 70, "Ford", "Focus"],
    "XY34ZRT": [200, 90, "BMW", "320i"],
    "LM56OPQ": [160, 60, "Toyota", "Corolla"],
    "GH78JKL": [220, 100, "Audi", "A4"]
}

# List representing the road (index 0 = front of the road)
road = ["AB12CDE", "XY34ZRT", "LM56OPQ", "GH78JKL"]


def display_road():
    print("\n--- Current Road ---")
    for i, plate in enumerate(road):
        top_speed, current_speed, make, model = cars[plate]
        print(f"Position {i + 1}: {plate} ({make} {model}) | Top: {top_speed} | Current: {current_speed}")


def attempt_overtake():
    display_road()
    plate = input("\nEnter the registration of the car that wants to overtake: ").strip()

    if plate not in road:
        print("Car not found on the road.")
        return

    index = road.index(plate)

    # If car is already at the front
    if index == 0:
        print("This car is already at the front and cannot overtake.")
        return

    # get car in front of selected car (note lead car has an index of 0)
    front_plate = road[index - 1]

    car_top_speed = cars[plate][0]
    front_current_speed = cars[front_plate][1]

    print(f"\nAttempting overtake...")
    print(f"{plate} top speed: {car_top_speed}")
    print(f"{front_plate} current speed: {front_current_speed}")

    if car_top_speed > front_current_speed:
        # Swap positions
        road[index], road[index - 1] = road[index - 1], road[index]
        print(f"{plate} successfully overtook {front_plate}!")
    else:
        print(f"Overtake failed. Not enough speed.")

    display_road()


def menu():
    while True:
        print("\n==== Car Road Simulation ====")
        print("1. View road")
        print("2. Attempt overtake")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_road()
        elif choice == "2":
            attempt_overtake()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# Run the program
if __name__ == "__main__":
    menu()
