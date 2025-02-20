"""Book Store exercise"""

from collections import Counter

def total(basket):
    """Calculates the lowest possible price for the provided basket, the largest discount possible.
 
    :param list[int] basket: The shopping basket.
    """

    def _remove_books(basket, bundle):
        """An efficient approach to removing a bundle of books from a basket.
 
        :param list basket: The original basket.
        :param list bundle: The books to be removed.
        :return list: The original basket with the books removed.
        """

        sub_basket_counts = Counter(bundle)
        new_basket = []
        for book in basket:
            if sub_basket_counts[book] > 0:
                sub_basket_counts[book] -= 1
            else:
                new_basket.append(book)
        return new_basket

    def _prices(book_amount):

        return 8 * book_amount * (1 - [0, 0.05, 0.1, 0.2, 0.25][book_amount - 1])

    if basket is None:
        raise ValueError("Missing input.")
    if not isinstance(basket, list):
        raise TypeError("Input must be a list.")
    for book in basket:
        if not isinstance(book, int):
            raise TypeError("Books must be integers.")
        if book not in range(1,6):
            raise ValueError("Book number out of range (1-5).")

    # Exit early if there are no books.
    if basket == []:
        return 0

    # Create base bundles.
    basket_edit = basket[:]
    bundles = []
    while basket_edit:
        bundle = list(set(basket_edit))
        basket_edit = _remove_books(basket_edit, bundle)
        bundles.append(bundle)

    # Generate bundles of different lengths.
    # Balancing from max to min.
    original_combination = [len(bundle) for bundle in bundles]
    lengths_combinations_a = [original_combination]
    while not (max(lengths_combinations_a[-1]) - 1) <= min(lengths_combinations_a[-1]):
        lengths_combinations_a.append(lengths_combinations_a[-1].copy())
        longest_index = lengths_combinations_a[-1].index(max(lengths_combinations_a[-1]))
        shortest_index = lengths_combinations_a[-1].index(min(lengths_combinations_a[-1]))
        lengths_combinations_a[-1][longest_index] -= 1
        lengths_combinations_a[-1][shortest_index] += 1

    # Balancing from max to <= max-2.
    lengths_combinations_b = [original_combination]
    while not (max(lengths_combinations_b[-1]) - 1) <= min(lengths_combinations_b[-1]):
        lengths_combinations_b.append(lengths_combinations_b[-1].copy())
        longest_index = lengths_combinations_b[-1].index(max(lengths_combinations_b[-1]))
        for length in lengths_combinations_b[-1]:
            if length <= max(lengths_combinations_b[-1])-2:
                middle_index = lengths_combinations_b[-1].index(length)
                break
        lengths_combinations_b[-1][longest_index] -= 1
        lengths_combinations_b[-1][middle_index] += 1
    lengths_combinations = lengths_combinations_a + lengths_combinations_b

    # Calculate prices for each combination of bundle lengths.
    total_prices = []
    for lengths in lengths_combinations:
        total_prices.append(sum(_prices(book_amount) for book_amount in lengths))
    return int(round(min(total_prices) * 100, 0))
