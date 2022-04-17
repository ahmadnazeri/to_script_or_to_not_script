import random

def set_doors(num_doors):
    doors = [None for _ in range(num_doors)]
    car_door = random.randint(0, num_doors-1)

    doors[car_door] = "car"
    return doors

def initial_choices(num_choices):
    return [i for i in range(num_choices)]

def open_doors(doors, choices):
    i = 0
    car_position = doors.index("car")

    if car_position in choices:
        return [car_position]
    else:
        return [random.choice(choices)]


def main():
    num_doors = int(input("How many doors would you like in the problem? "))
    trials = int(input("How many times would you like to run this trial? "))

    if num_doors < 3:
        raise Exception("Number of doors need to be >= 3.")

    first_pick_car_found = 0
    second_pick_car_found = 0

    for i in range(trials):
        print(f"{i+1}/{trials}")
        doors = set_doors(num_doors)
        choices = initial_choices(num_doors)

        first_pick = random.choice(choices)
        del choices[first_pick]

        choices = open_doors(doors, choices)

        switch_pick = random.choice(choices)

        if doors[first_pick] == "car":
            first_pick_car_found += 1

        if doors[switch_pick] == "car":
            second_pick_car_found += 1


    print(f"After {trials}, the car was found behind pick:")
    print(f"\tFirst pick: {100*(first_pick_car_found/trials)}%")
    print(f"\tSecond pick: {100*(second_pick_car_found/trials)}%")


if __name__ == '__main__':
    main()