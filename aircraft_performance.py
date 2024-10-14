def get_positive_int(prompt):
    while True:
        user_input = input(prompt + " (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            exit()
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def print_banner():
    banner = """
    \033[1;34m*********************************************
    *                                           *
    *          Aircraft Performance Calculator  *
    *                                           *
    *********************************************
    
    \033[1;35m
                  __|__
          --o--o--(_)--o--o--
    \033[0m
    """  # \033[1;34m for blue and \033[0m to reset color
    print(banner)

# Call the function to print the banner
print_banner()

# Defined by user
fuel_capacity = get_positive_int('What is the fuel capacity in gallons? ')

fuel_consumption_rate = get_positive_int('What is your consumption rate of gallons per hour? ')

true_air_speed = get_positive_int('What is the true air speed in knots? ')

payload = get_positive_int('What is the payload in pounds? ')

fuel_weight = get_positive_int('What is the weight of the fuel? ')

moment_list = [10000, 2500]  # pound-feet

total_weight = get_positive_int("What is the total weight in pounds? ")

cl = get_positive_int('What is the lift coefficient? ')

rho = get_positive_int('What is the air density in kg/m^3? ')

v = get_positive_int('What is the velocity in m/s? ')

s = get_positive_int('What is the wing area in m^2? ')

cd = get_positive_int('What is the drag coefficient? ')

mass = get_positive_int('What is the mass in kg? ')

g = get_positive_int("What is the acceleration of the gravity in m/s^2? ")

thrust = get_positive_int('What is the thrust in N? ')

drag = get_positive_int("What is the drag in N? ")

velocity = get_positive_int('What is the initial velocity in m/s? ')

acceleration = get_positive_int('What is the acceleration in m/s^2? ')

time = get_positive_int('What is the time in seconds? ')

# Helper function to pretty print performance data
def pretty_print(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    print("Performance Calculations:")
    print("Range: {} miles".format(range_))
    print("Endurance: {} hours".format(endurance))
    print("Total Weight: {} pounds".format(total_weight))
    print("Center of Gravity Position: {} feet".format(cg_position))
    print("Lift: {} Newtons".format(lift))
    print("Drag: {} Newtons".format(drag))
    print("Weight: {} Newtons".format(weight))
    print("Acceleration: {} m/s^2".format(acceleration))
    print("Velocity: {} m/s".format(velocity))
    print("Distance: {} meters".format(distance))

def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = (fuel_capacity / fuel_consumption_rate)
    range_in_miles = range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    total_moment = sum(moment_list)
    return total_moment / total_weight

def calculate_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust - drag - weight) / mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration * time

def calculate_distance(velocity, time):
    return velocity * time

range_ = calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)
endurance = calculate_endurance(fuel_capacity, fuel_consumption_rate)
total_weight = calculate_total_weight(payload, fuel_weight)
cg_position = calculate_cg_position(moment_list, total_weight)
lift = calculate_lift(cl, rho, v, s)
drag = calculate_drag(cd, rho, v, s)
weight = calculate_weight(mass, g)
acceleration = calculate_acceleration(thrust, drag, weight, mass)
velocity = calculate_velocity(velocity, acceleration, time)
distance = calculate_distance(velocity, time)

pretty_print(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance)


def save_info_to_file(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file):
    file.write("Performance Calculations:\n")
    file.write("Range: {} miles\n".format(range_))
    file.write("Endurance: {} hours\n".format(endurance))
    file.write("Total Weight: {} pounds\n".format(total_weight))
    file.write("Center of Gravity Position: {} feet\n".format(cg_position))
    file.write("Lift: {} Newtons\n".format(lift))
    file.write("Drag: {} Newtons\n".format(drag))
    file.write("Weight: {} Newtons\n".format(weight))
    file.write("Acceleration: {} m/s^2\n".format(acceleration))
    file.write("Velocity: {} m/s\n".format(velocity))
    file.write("Distance: {} meters\n".format(distance))

with open('aircraft_performance_analysis.txt', 'w') as f:
    save_info_to_file(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file=f)
