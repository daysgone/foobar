import sys
import math

''''
google level 2
grid 8x8 grid
numbered 0-63
given start and end point calcuate min amount of moves
move are similar to knight move in chess 3 squares in any direction then 1 perpendicular ( L shape )
'''


def to_grid(number):
    """
    convert value to grid space
    :param number: cell value
    :return: x,y value of grid

    0}1|2|3|4|5|6|7
    8|....
    16|
    .............|63
    """
    x = number % 8
    y = math.trunc(number / 8)
    return x, y


def to_value(coord):
    """
    covert grid coords back to value
    :param coord:   x,y value pair
    :return: int value of grid
    """
    x, y = coord

    value = (8 * y) + x
    return value


def test_values(coord, x=7, y=7):
    """
    Make sure given coord is still on given grid
    :param coord: x,y int values of grid location
    :param x: size of x axis of grid
    :oaram y: size of y axis of grid
    :return: True if still in given grid
    """
    x, y = coord
    r = range(0, 7)

    if x in r and y in r:
        return True
    return False


def completed_path(coord, end_point):
    """
    if given point matches end point
    :param coord:   given coord
    :param end_point:  coord of point to end at
    :return:    True if match
    """
    if end_point == coord:
        # print "found end point (%d,%d)" % coord
        return True
    return False


def find_next(start_point, end_point):
    """
    take current given point and find next valid points it could reach in another step
    :param start_point: x,y grid space of given point
    :param end_point:  point we are heading too
    :return:  next set of valid coords
    """
    x, y = start_point
    valid_coords = []
    possible_paths = [(x - 1, y - 2),
                      (x + 1, y - 2),
                      (x + 2, y - 1),
                      (x + 2, y + 1),
                      (x - 1, y + 2),
                      (x + 1, y + 2),
                      (x - 2, y - 1),
                      (x - 2, y + 1)]

    # only add points to valid if doesnt fall outside of grid
    for p in possible_paths:
        if completed_path(p, end_point):
            print 'end point reached'
            return None

        if test_values(p):
            valid_coords.append(p)
        else:
            pass
        # print 'invalid coord (%d,%d), skipping' % p

    return valid_coords


def check_range(value,start=0, end=63):
    """
    check to see if user input correct values
    :param value: int value
    :return: True in range
    """
    return start <= value <= end


def main_func(valid_coords, start, end):
    """
    needed a function so that we can break out of loop as soon as endpoint is reached
    :param valid_coords: list of tuples (x,y) integers
    :param start:        starting point tuple (x,y)
    :param end:          ending point tuple (x,y)
    :return:            de-duped list of next coords, (x,y) tuple, to check
                        returns None if no more points to go to
    """
    step = []
    for coord in valid_coords:
        if coord == end:
            # first step found endpoint
            return None
        elif coord == start:  # no need to go back a step
            break
        else:
            cur_point = find_next(coord, end)
            if cur_point == end:
                return None
            if cur_point is None:
                return None
            step.extend(cur_point)
    step = list(set(step))
    return step

if __name__ == "__main__":
    # grab start and end values from command line
    values = [None, None]

    for i, j in enumerate(sys.argv[1:]):
        try:
            values[i] = int(j)
        except ValueError:
            print "Not a number"

    # make sure valid inputs
    start_valid = check_range(values[0])
    end_valid = check_range(values[1])

    while True:
        try:
            if not start_valid:
                values[0] = int(raw_input('Start invalid please enter value (0-63):\t'))
            if not end_valid:
                values[1] = int(raw_input('End invalid please enter value (0-63):\t'))
        except ValueError:
            print "Not a number"

        start_valid = check_range(values[0])
        end_valid = check_range(values[1])
        # print values
        if start_valid and end_valid:
            # print 'both values good'
            break
        else:
            # print 'values not good'
            break

    # change to grid units
    start = to_grid(values[0])
    end = to_grid(values[1])

    next_step = []
    counter = 0
    # start it off
    if start == end:
        pass
    else:
        next_step = find_next(start, end)

        while True:
            counter += 1
            if next_step is None:
                break
            else:
                next_step = main_func(next_step, start, end)

    print 'reached endpoint with %d steps' % counter
