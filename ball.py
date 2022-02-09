class Ball():
    def __init__(self, screen_size, radius = 5, multiplier_speed = 1):
        self.radius = radius
        self.circle= ((0,0), self.radius)
        self.debug_square = (0, 0, 0, 0)

        self.movement = 0
        self.multiplier_speed = multiplier_speed
        
        self.x_offset = 0
        self.y_offset = 0

        self.direction = (-1, 0)
        self.move(screen_size)

    def move(self, screen_size):
        middle_x = screen_size[0] / 2
        middle_y = screen_size[1] / 2

        smaller_screen_size = screen_size[0] if screen_size[0] < screen_size[1] else screen_size[1]

        self.x_offset += self.movement * smaller_screen_size/240 * self.multiplier_speed * self.direction[0]
        self.y_offset += self.movement * smaller_screen_size/240 * self.multiplier_speed * self.direction[1]

        radius = self.radius + smaller_screen_size / 100
        self.debug_square = (middle_x - radius, middle_y - radius, radius * 2, radius * 2)
        self.circle = ((middle_x + self.x_offset, middle_y + self.y_offset), radius)