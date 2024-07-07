from cell import cell
import random, time


class Maze:
    __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)


        self._create_cells()
        self._open_ent_and_ext()
        self._break_walls(0,0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.1)


    def _break_ent_and_ext(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)


    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_idx_list = []
        # choosing next cell to visit: left|right|up|down
        if i > 0 and not self._cells[i-1][j].visited:
            next_idx_list.append((i-1, j))
        if i < self.num_cols -1 and not self._cells[i+1][j].visited:
            next_idx_list.append((i+1, j))
        if j > 0 and not self._cells[i][j-1].visited:
            next_idx_list.append((i, j-1))
        if j < self.num_cols -1 and not self._cells[i][j+1].visited:
            next_idx_list.append((i, j+1))

        if len(next_idx_list) == 0:
            self._draw_cell(i, j)
            return

        #randomly choose a direction to go and break through
        direction = random.ranrange(len(next_idx_list))
        next_idx = next_idx_list[direction]

        if next_idx[0] == i + 1:
            self._cells[i][j].has_right_wall = False
            self._cells[i+1][j].has_left_wall = False
        if next_idx[0] == i - 1:
            self._cells[i][j].has_left_wall = False
            self._cells[i-1][j].has_right_wall = False
        if next_idx[1] == j + 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j+1].has_top_wall = False
        if next_idx[1] == j - 1:
            self._cells[i][j].has_top_wall = False
            self._cells[i][j-1].has_bottom_wall = False

        # recurse until the maze is complete
        self._break_walls(next_idx[0], next_idx[1])


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False


    def _solve(self, i=0, j=0):
        self._animate()

        self._cells[i][j].visited = True
        if i == self.num_cols -1 and j == self.num_rows -1:
            return True

        # move left if no wall and left cell unvisited
        if (
            i > 0 and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        # move right if no wall and right cell unvisited
        if (
            i < self.num_cols-1 and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # move up if no wall and above cell unvisited
        if (
            j > 0 and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # move down if no wall and below cell unvisited
        if (
            j < self.num_rows-1 and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        # no more possible moves in current direction | return False & turn back
        return False

        

        
        





