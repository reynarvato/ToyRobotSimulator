from robot import Table, Robot
import os

_COMMANDS_PATH = os.path.join(os.path.dirname(__file__), "commands.txt")

DIRECTIONS = ("NORTH", "EAST", "SOUTH", "WEST")
VALID_COMMANDS = ("PLACE", "MOVE", "LEFT", "RIGHT", "REPORT")


class Simulator:
    def __init__(self):
        self.table = Table()
        self.robot = Robot()

    def run(self):
        with open(_COMMANDS_PATH, encoding="utf-8") as f:
            for command in f:
                self._parse_command(command)

    def _parse_command(self, command):
        parts = command.strip().split()
        # print(parts)
        if not parts:
            return

        if parts[0] not in VALID_COMMANDS:
            return

        if parts[0] == "PLACE":
            if len(parts) != 2:
                return
            args = parts[1].split(",")
            if len(args) != 3:
                return
            raw_x, raw_y, direction = args
            # Check if x and y are digits, at this stage, 
            # allow negative numbers as its a valid command.
            if (not raw_x.lstrip("-").isdigit()
                    or not raw_y.lstrip("-").isdigit()):
                return
            x = int(raw_x)
            y = int(raw_y)
            # print(x, y, direction)
            valid_position = self.table.is_valid_position(x, y)
            valid_direction = direction in DIRECTIONS
            # print(valid_position, valid_direction)
            if valid_position and valid_direction:
                self._place(x, y, direction)

        elif parts[0] in ("MOVE", "LEFT", "RIGHT"):
            if not self.robot.is_placed:
                # ignore
                pass
            elif parts[0] == "MOVE":
                self._move_command()
            elif parts[0] == "LEFT":
                self._left_command()
            elif parts[0] == "RIGHT":
                self._right_command()

        elif parts[0] == "REPORT":
            self._report_command()

    def _place(self, x, y, direction):
        self.robot.is_placed = True
        self.robot.x = x
        self.robot.y = y
        self.robot.direction = direction
        # print(self.robot.X, self.robot.Y, self.robot.direction)

    def _report_command(self):
        if not self.robot.is_placed:
            return ""
        report = f"{self.robot.x},{self.robot.y},{self.robot.direction}"
        print(report)
        return report

    def _move_command(self):
        # Compute potential new position
        new_x, new_y = self.robot.x, self.robot.y

        if self.robot.direction == "NORTH":
            new_y += 1
        elif self.robot.direction == "EAST":
            new_x += 1
        elif self.robot.direction == "SOUTH":
            new_y -= 1
        elif self.robot.direction == "WEST":
            new_x -= 1

        # Only apply if the new position is safe
        if self.table.is_valid_position(new_x, new_y):
            self.robot.x = new_x
            self.robot.y = new_y

    def _left_command(self):
        current_index = DIRECTIONS.index(self.robot.direction)
        new_index = (current_index - 1) % 4
        self.robot.direction = DIRECTIONS[new_index]
        # print(self.robot.direction)

    def _right_command(self):
        current_index = DIRECTIONS.index(self.robot.direction)
        new_index = (current_index + 1) % 4
        self.robot.direction = DIRECTIONS[new_index]
        # print(self.robot.direction)


if __name__ == "__main__":
    simulator = Simulator()
    simulator.run()
