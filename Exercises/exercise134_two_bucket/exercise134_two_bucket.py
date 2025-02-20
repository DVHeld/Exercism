"""Two Bucket exercise"""

from math import gcd

ONE = 0
TWO = 1
FILL_ONE = 1
FILL_TWO = 2
EMPTY_ONE = 3
EMPTY_TWO = 4

def measure(bucket_one, bucket_two, goal, start_bucket, /):
    """Solves the two bucket puzzle, given the capacity of the buckets, the goal and the first
    bucket to be filled.
 
    :param int bucket_one: The first bucket's capacity.
    :param int bucket_two: The second bucket's capacity.
    :param int goal: The goal.
    :param str start_bucket: The first bucket to be filled.
    :return tuple: A tuple containing the solution. Move amount, final bucket and remaining amount
    in the other bucket.
    """

    def _fill(bucket, /):

        return [bucket_one if bucket == ONE else buckets[ONE],
                bucket_two if bucket == TWO else buckets[TWO]]

    def _empty(bucket, /):

        return [0 if bucket == ONE else buckets[ONE],
                0 if bucket == TWO else buckets[TWO]]

    def _transfer(source, /):

        total_content = buckets[ONE] + buckets[TWO]
        if source == ONE:
            return [max(0, total_content - bucket_two), min(bucket_two, total_content)]
        return [min(bucket_one, total_content), max(0, total_content - bucket_one)]

    def _is_full(bucket, /):

        return buckets[bucket] == (bucket_one if bucket == ONE else bucket_two)

    def _is_empty(bucket, /):

        return buckets[bucket] == 0

    if None in (bucket_one, bucket_two, goal, start_bucket):
        raise ValueError("Missing inputs.")
    if not (isinstance(bucket_one, int) and \
            isinstance(bucket_two, int) and \
            isinstance(goal, int)):
        raise TypeError("Capacities and goal must be integers.")
    if start_bucket not in ("one", "two"):
        raise ValueError("Invalid start bucket input.")
    if min(bucket_one, bucket_two, goal) <= 0:
        raise ValueError("Invalid capacity or goal input. They must be greater than zero.")
    if goal > bucket_one and goal > bucket_two:
        raise ValueError("No bucket has enough capacity to reach the goal.")
    if bucket_one > bucket_two:
        raise ValueError("The first bucket must be smaller than the second.")
    if goal % gcd(bucket_one, bucket_two) != 0:
        raise ValueError("This combination has no possible solution.")

    buckets = [bucket_one if start_bucket == "one" else 0,
               bucket_two if start_bucket == "two" else 0]
    moves = 1
    last_move = 0

    while goal not in buckets:
        if goal == bucket_one:
            buckets = _fill(ONE)
            last_move = FILL_ONE
        elif goal == bucket_two:
            buckets = _fill(TWO)
            last_move = FILL_TWO
        elif _is_full(ONE) and _is_empty(TWO):
            buckets = _transfer(ONE)
            last_move = 0
        elif _is_full(TWO) and _is_empty(ONE):
            buckets = _transfer(TWO)
            last_move = 0
        elif _is_full(ONE) and last_move != FILL_ONE:
            buckets = _empty(ONE)
            last_move = EMPTY_ONE
        elif _is_full(TWO) and last_move != FILL_TWO:
            buckets = _empty(TWO)
            last_move = EMPTY_TWO
        elif _is_full(ONE):
            buckets = _transfer(ONE)
            last_move = 0
        elif _is_empty(ONE) and last_move == EMPTY_ONE:
            buckets = _transfer(TWO)
            last_move = 0
        elif _is_empty(TWO) and last_move != EMPTY_TWO:
            buckets = _fill(TWO)
            last_move = FILL_TWO
        elif _is_empty(TWO):
            buckets = _transfer(ONE)
            last_move = 0
        elif _is_empty(ONE):
            buckets = _fill(ONE)
            last_move = FILL_ONE
        elif not _is_empty(ONE) and not _is_empty(TWO) and last_move == FILL_TWO:
            buckets = _transfer(TWO)
            last_move = 0
        moves += 1
    final_bucket = 0 if buckets[0] == goal else 1
    return (moves, "two" if final_bucket else "one", buckets[(final_bucket + 1) % 2])
