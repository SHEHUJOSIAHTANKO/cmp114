class Mathematics:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
    
    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            raise ValueError("cannnot calculate square root of a negative number")

class Physics:
    def velocity(distance, time):
        if time == 0:
            raise ValueError("Time cannot be zero.")
        return distance / time

    def acceleration(velocity, time):
        if time == 0:
            raise ValueError("Time cannot be zero.")
        return velocity / time
    
    def energy(mass, velocity):
        return 0.5 * mass * velocity**2
    
    def force(mass, acceleration):
        return mass * acceleration
    
    def calculate_work(self, force, distance, angle=0):
        return force * distance * math.cos(math.radians(angle))

    


math_result = Mathematics.add(19, 3)
print("Math Addition:", math_result)

physics_result = Physics.velocity(1000, 15)
print("Physics Velocity:", physics_result)

