# Defined by user
fuel_capacity = input('What is the fuel capacity in gallons? ')
fuel_capacity = int(fuel_capacity)
fuel_consumption_rate = input('What is your consumption rate of gallons per hour? ')
fuel_consumption_rate = int(fuel_consumption_rate )
true_air_speed = input('What is the true air speed in knots? ')
true_air_speed = int(true_air_speed)
payload = input('What is the payload in pounds? ')
payload = int(payload)
fuel_weight = input('What is the weight of the fuel? ')
fuel_weight = int(fuel_weight)
moment_list = [10000, 2500]  # pound-feet

total_weight = input("What is the total weight in pounds? ")
total_weight = int(total_weight)
cl = input('What is the lift coefficient? ')
cl = int(cl)
rho = input('What is the air density in kg/m^3? ')
rho = int(rho)
v = input('What is the velocity in m/s? ')
v = int(v)
s = input('What is the wing area in m^2? ')
s = int(s)
cd = input('What is the drag coefficient? ')
cd = int(cd)
mass = input('What is the mass in kg? ')
mass = int(mass)
g = input("What is the acceleration of the gravity in m/s^2? ")
g = int(g)
thrust = input('What is the thrust in N? ')
thrust = int(thrust)
drag = input("What is the drag in N? ")
drag = int(drag)
velocity = input('What is the initial velocity in m/s? ')
velocity = int(velocity)
acceleration = input('What is the acceleration in m/s^2? ')
acceleration = int(acceleration)
time = input('What is the time in seconds? ')
time = int(time)

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
