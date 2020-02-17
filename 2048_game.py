# 2048 game
import random
import arcade


class Game(arcade.Window):
    def __init__(self,game_field,width,height):
               # Call the parent class initializer
        super().__init__(width, height, "2048 Game")
        if game_field:
            self.game_field = game_field
        else:
            self.game_field =[
            [0,0,0,0],
            [0,0,0,0],
            [0,0,2,0],
            [0,0,0,0]
            ]
        self.score = 0
        arcade.set_background_color((205,193,181))
        self.last_move = None
    def full(self):
        for i in range(4):
            for j in range(4):
                if self.game_field[i][j] == 0:
                    return False
        return True

    def win(self):
        for i in range(4):
            for j in range(4):
                if self.game_field[i][j] == 2048:
                    return True
        return False 

    def add_element(self):
        free_positions = []
        new_element = [2,4]
        for i in range(4):
            for j in range(4):
                if game_field[i][j]==0:
                    free_positions.append([i,j])
        position = random.sample(free_positions,1)[0]
        value = random.sample(new_element,1)[0]
        game_field[position[0]][position[1]]= value

    def get_left_max(self,i,j):
        if j == 0:
            return 0
        for k in range(0,j):
            if self.game_field[i][k]==0:
                return k
        return j 

    def get_top_max(self,i,j):
        if i == 0:
            return 0
        for k in range(0,i):
            if self.game_field[k][j]==0:
                return k
        return i 

    def get_right_max(self,i,j):
        if j == 3:
            return 3
        for k in range(3,j,-1):
            if self.game_field[i][k]==0:
                return k
        return j 

    def get_bottom_max(self,i,j):
        if i == 3:
            return 3
        for k in range(3,i,-1):
            if self.game_field[k][j]==0:
                return k
        return i 


    def swipe_left(self):
        for i in range(4):
            for j in range(4):
                if self.game_field[i][j] != 0:
                    left_max = self.get_left_max(i,j)
                    help = self.game_field[i][j]
                    self.game_field[i][j] = 0
                    self.game_field[i][left_max] = help 

    def swipe_right(self):
        for i in range(4):
            for j in range(3,-1,-1):
                if game_field[i][j] != 0:
                    right_max = self.get_right_max(i,j)
                    help = self.game_field[i][j]
                    self.game_field[i][j] = 0
                    self.game_field[i][right_max] = help 

    def swipe_top(self):
        for i in range(4):
            for j in range(4):
                if self.game_field[i][j] != 0:
                    top_max = self.get_top_max(i,j)
                    help = game_field[i][j]
                    self.game_field[i][j] = 0
                    self.game_field[top_max][j] = help 

    def swipe_bottom(self):
        for i in range(3,-1,-1):
            for j in range(4):
                if game_field[i][j] != 0:
                    bottom_max = self.get_bottom_max(i,j)
                    help = self.game_field[i][j]
                    self.game_field[i][j] = 0
                    self.game_field[bottom_max][j] = help 
                    

    def reduce_left(self):
        reduce_score = 0
        for i in range(4):
            for j in range(3):
                if self.game_field[i][j] == game_field[i][j+1]:
                    self.game_field[i][j] *=2
                    self.game_field[i][j+1] = 0
                    reduce_score += self.game_field[i][j]
        return reduce_score


    def reduce_right(self):
        reduce_score = 0
        for i in range(4):
            for j in range(3,0,-1):
                if self.game_field[i][j] == self.game_field[i][j-1]:
                    self.game_field[i][j] *=2
                    self.game_field[i][j-1] = 0
                    reduce_score += self.game_field[i][j]
        return reduce_score

    def reduce_top(self):
        reduce_score = 0
        for i in range(0,3):
            for j in range(4):
                if self.game_field[i][j] == self.game_field[i+1][j]:
                    self.game_field[i][j] *=2
                    self.game_field[i+1][j] = 0
                    reduce_score += self.game_field[i][j]
        return reduce_score

    def reduce_bottom(self):
        reduce_score = 0
        for i in range(3,0,-1):
            for j in range(4):
                if self.game_field[i][j] == self.game_field[i-1][j]:
                    self.game_field[i][j] *=2
                    self.game_field[i-1][j] = 0
                    reduce_score += self.game_field[i][j]
        return reduce_score             

    def move_left(self):
        self.swipe_left()
        move_score = self.reduce_left()
        self.swipe_left()
        return move_score

    def move_right(self):
        self.swipe_right()
        move_score = self.reduce_right()
        self.swipe_right()
        return move_score

    def move_top(self):
        self.swipe_top()
        move_score = self.reduce_top()
        self.swipe_top()
        return move_score

    def move_bottom(self):
        self.swipe_bottom()
        move_score = self.reduce_bottom()
        self.swipe_bottom()
        return move_score
    
    def setup(self):
        self.score += 0
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.move_top()
            self.add_element()
        elif key == arcade.key.DOWN:
            self.move_bottom()
            self.add_element()
        elif key == arcade.key.LEFT:
            self.move_left()
            self.add_element()
        elif key == arcade.key.RIGHT:
            self.move_right()
            self.add_element()


    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()
        for x in range(0, 801, 200):
            arcade.draw_line(x, 0, x, 800, (187,173,161), 12)

        # Draw horizontal lines every 200 pixels
        for y in range(0, 801, 200):
            arcade.draw_line(0, y, 800, y, (187,173,161), 12)

        for i in range(4):
            for j in range(4):
                if game_field[i][j] != 0:
                    texture = texture = arcade.load_texture('images/'+str(self.game_field[i][j])+'.png')
                    scale=0.95
                    row_pixel = 700 - (i * 200)
                    column_pixel = 100 + (j * 200)
                    arcade.draw_texture_rectangle(column_pixel,row_pixel, scale * texture.width,scale * texture.height, texture, 0)

score = 0
game_field =[
            [0,0,0,0],
            [0,0,0,0],
            [0,0,2,0],
            [0,0,0,0]
            ]
def main():
    """ Main method """
    game = Game(game_field,800,800)
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()




    

