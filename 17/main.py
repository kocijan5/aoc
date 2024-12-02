import numpy as np

class Maze:
    def __init__(self, lines):
        
        self.x_pos = 0
        self.y_pos = 0
        self.line_limit = 3
        

        _maze = []
        for line in lines:
            r = []
            for c in line:
                if not c.isnumeric():
                    break
                r.append(int(c))
            _maze.append(r)
        self.maze = np.array(_maze)
        self.y_goal = len(self.maze) - 1
        self.x_goal = len(self.maze[0]) - 1


    def bfs_ver_1(self):
        def expand(past_pos, instruction):
            new_frontier = []
            if self.last_instruction == instruction:
                self.same_counter += 1
            else:
                self.same_counter = 0
            self.last_instruction = instruction
            if instruction == 'left' or None:
                new_frontier.append((past_pos[0] - 1, past_pos[1] - 1, 'top'), (past_pos[0] + 1, past_pos[1] - 1, 'bottom'))
                if self.same_counter < self.line_limit:
                    new_frontier.append(past_pos[0], past_pos[1] - 2, 'left')
            elif instruction == 'right' or None:
                new_frontier.append((past_pos[0] + 1, past_pos[1] + 1, 'bottom'), (past_pos[0] - 1, past_pos[1] + 1, 'top'))
                if self.same_counter < self.line_limit:
                    new_frontier.append(past_pos[0], past_pos[1] + 2, 'right')
            elif instruction == 'top' or None:
                new_frontier.append((past_pos[0] - 1, past_pos[1] - 1, 'left'), (past_pos[0] - 1, past_pos[1] + 1, 'right'))
                if self.same_counter < self.line_limit:
                    new_frontier.append(past_pos[0] - 2, past_pos[1], 'top')
            elif instruction == 'bottom' or None:
                new_frontier.append((past_pos[0] + 1, past_pos[1] - 1, 'left'), (past_pos[0] + 1, past_pos[1] + 1, 'right'))
                if self.same_counter < self.line_limit:
                    new_frontier.append(past_pos[0] + 2, past_pos[1], 'bottom')
            return [pos for pos in new_frontier if self.test_limits(pos)]
        
        visited = {}
        frontier = {}
        self.last_instruction = None
        while self.x_pos != self.x_goal and self.y_pos != self.y_goal:
            pass

    def test_limits(self, pos):
        if pos[0] < 0 or pos[1] < 0 or pos[0] > self.x_goal or pos[1] > self.y_goal:
            return False
        return True

def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()

    maze = Maze(lines)
    return 102

if __name__ == '__main__':
    r = main()
    assert r == 102  