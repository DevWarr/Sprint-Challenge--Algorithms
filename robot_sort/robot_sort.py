class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def swap_right(self):
        # We start out holding None
        self.swap_item()

        # Keep going until we can go no further!
        while self.can_move_right():
            self.move_right()
            if self.compare_item() == -1 and self.can_move_right():
                # If our held item is less, we want the bigger one!
                # However... If the item in front of us is bigger
                #     AND we're at the end of the list, we don't want
                #     to pick it up. It's at the end, and it's the biggest,
                #     so we won't waste a move by swapping
                self.swap_item()
            elif self.compare_item() == 1 and self.can_move_right() == False:
                # If we're at the end of the list and our held item
                # is larger than the one in front of us, swap em!
                self.swap_item()
        return

    def swap_left(self):
        # We start out holding the second highest value
        # at the end of our list

        # Keep going until we find our None spot!
        while self.compare_item() is not None:
            self.move_left()
            if self.compare_item() == 1:
                # If our held item is greater, we want the smaller one!
                self.swap_item()

        # If we find our None spot, we want to
        #     swap the number we have,
        #     and move one space to the right
        self.swap_item()
        self.move_right()
        return

    def sort(self):
        """
        Sort the robot's list.
        """
        # We have two sections to this sort:
        # Moving right:
        #     Keep moving right, swapping values that are larger
        #     until we can't move right anymor.
        # Moving left:
        #     Keep moving left, swapping numbers that are smaller
        #     until we find our None space.
        # Keep doing this loop until we reach the rightmost spot
        # with our None item.

        # This is similar to bubble sorting, with a few optimizations:
        # - We sort when moving both right and left through the list
        # - We don't have to move all the way to the left because our None
        #   spot lets us know where we left off.

        # I could not think of a way to stop the robot early. For example, 
        #     if the robot starts with a fully ordered list, it will still
        #     move as if it's sorting the entire list, swapping items as it 
        #     goes.
        #     It doesn't know whether the list is fully sorted before it
        #     reaches the end of the list.
        
        # I also could not think of how to use the light.
        # So the light could probably help optimize this further...
        #     I just don't know how :sweat_smile:
        while self.can_move_right():
            self.swap_right()
            self.swap_left()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
