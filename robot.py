from motor import Motor

class Robot():

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.right_motor = Motor()
        self.left_motor = Motor()

    def drive_forward(self, speed: float):
        self.right_motor.set_speed(speed)
        self.left_motor.set_speed(speed)

    def reverse(self):
        self.drive_forward(-1)

    def turn_left(self):
        self.right_motor.set_speed(1)
        self.left_motor.set_speed(0)

    def turn_right(self):
        self.right_motor.set_speed(0)
        self.left_motor.set_speed(1)




