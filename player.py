
class Player():
    def __init__(self, side, screen_size, multiplier_speed = 1):
        self.side = side
        self.movement = 0
        self.y_offset = 0
        self.multiplier_speed = multiplier_speed

        self.top_x = screen_size[0]/50
        self.top_y = screen_size[1]/2-screen_size[1]/12
        self.width = screen_size[0]/40
        self.heigth = screen_size[1]/6

        self.collision_box = (0, 0, 0, 0)

        self.move(screen_size)


    def move(self, screen_size):
        self.top_x = screen_size[0]/50
        self.top_y = screen_size[1]/2-screen_size[1]/12
        self.width = screen_size[0]/40
        self.heigth = screen_size[1]/6
        smaller_screen_size = screen_size[0] if screen_size[0] < screen_size[1] else screen_size[1]

        self.y_offset += self.movement * smaller_screen_size/240 * self.multiplier_speed

        if self.side == "left":
            self.rect = (self.top_x,self.top_y+self.y_offset, self.width, self.heigth)

            top_left = (self.top_x, self.top_y+self.y_offset)
            top_right = (self.top_x+self.width, self.top_y+self.y_offset)
            bottom_right = (self.top_x, self.top_y+self.y_offset+self.heigth)
            bottom_left = (self.top_x+self.width, self.top_y+self.y_offset+self.heigth)
            self.collision_box = (top_left, top_right, bottom_left, bottom_right)
        else:
            self.rect = (-2 * self.top_x + screen_size[0], self.top_y+self.y_offset, self.width, self.heigth)
            top_left = (-2 * self.top_x + screen_size[0], self.top_y + self.y_offset)
            top_right = (-2 * self.top_x + screen_size[0], self.top_y + self.y_offset)
            bottom_right = (self.top_x, self.top_y+self.y_offset+self.heigth)
            bottom_left = (self.top_x+self.width, self.top_y+self.y_offset+self.heigth)
            self.collision_box = (top_left, top_right, bottom_left, bottom_right)

    def ball_collide(self, ball_center, ball_direction, screen_size):
        ball_x = ball_center[0]
        ball_y = ball_center[1]
        
        
        if self.side == "left":
            # if collided with left side
            if ball_x < self.collision_box[0]:# and ball_x > self.collision_box[2]:
                # if collided with top half
                print(self.collision_box)
                if ball_y > self.collision_box[1] and ball_y < self.collision_box[4]:
                    if ball_y > self.collision_box[4]/6:
                        return [ball_direction[0]*-1, -0.5]
                    if ball_y > self.collision_box[4]/3:
                        return [ball_direction[0]*-1, ball_direction[1]]
                    if ball_y > self.collision_box[4]:
                        return [ball_direction[0]*-1, -0.5]
        
        # elif self.side == "right":
        #     # if collided with left side
        #     if ball_x < self.collision_box[0] and ball_x > self.collision_box[2]:
        #         # if collided with top half
        #         if ball_y > self.collision_box[1] and ball_y < self.collision_box[4]:
        #             if ball_y > self.collision_box[4]/6:
        #                 return [ball_direction[0]*-1, -0.5]
        #             if ball_y > self.collision_box[4]/3:
        #                 return [ball_direction[0]*-1, ball_direction[1]]
        #             if ball_y > self.collision_box[4]:
        #                 return [ball_direction[0]*-1, -0.5]

        return [ball_direction[0], ball_direction[1]]

    def key_inputs(self, key, keys, key_press):
        for index, item in enumerate(keys):
            if key[item]:
                self.movement = (-5 if index == 0 else 5) * self.multiplier_speed
                return True
        return True if key_press else False