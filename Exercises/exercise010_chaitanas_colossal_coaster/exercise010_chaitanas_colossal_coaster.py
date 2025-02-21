"""Chaitana's Collossal Coaster exercise

Functions to manage and organize queues at Chaitana's roller coaster."""

def add_me_to_the_queue(express_queue: list, normal_queue: list, ticket_type: int, person_name: str) -> list:
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.
 
    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if express_queue is None or normal_queue is None or ticket_type is None or person_name is None:
        raise ValueError("Missing input.")
    if not isinstance(express_queue, list) or not isinstance(normal_queue, list):
        raise TypeError("Queues must be lists.")
    for person in normal_queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")
    for person in express_queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")
    if not isinstance(ticket_type, int):
        raise TypeError("Ticket type must be an integer.")
    if ticket_type not in (0, 1):
        raise ValueError("Invalid ticket type.")
    if not isinstance(person_name, str):
        raise TypeError("Person name must be a string.")

    if ticket_type:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue

def find_my_friend(queue: list, friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).
 
    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    if queue is None or friend_name is None:
        raise ValueError("Missing input.")
    if not isinstance(queue, list):
        raise TypeError("Queues must be lists.")
    for person in queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")
    if not isinstance(friend_name, str):
        raise TypeError("Person name must be a string.")

    return queue.index(friend_name)

def add_me_with_my_friends(queue: list, index: int, person_name: str) -> list:
    """Insert the late arrival's name at a specific index of the queue.
 
    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    if queue is None or person_name is None or index is None:
        raise ValueError("Missing input.")
    if not isinstance(queue, list):
        raise TypeError("Queues must be lists.")
    for person in queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index not in range(len(queue)+1):
        raise ValueError("Invalid index.")
    if not isinstance(person_name, str):
        raise TypeError("Person name must be a string.")

    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue: list, person_name: str) -> list:
    """Remove the mean person from the queue by the provided name.
 
    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    if queue is None or person_name is None:
        raise ValueError("Missing input.")
    if not isinstance(queue, list):
        raise TypeError("Queues must be lists.")
    for person in queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")
    if not isinstance(person_name, str):
        raise TypeError("Person name must be a string.")
    if person_name not in queue:
        raise ValueError("Person not in queue.")

    queue.remove(person_name)
    return queue

def how_many_namefellows(queue: list, person_name: str) -> int:
    """Count how many times the provided name appears in the queue.
 
    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

    if queue is None or person_name is None:
        raise ValueError("Missing input.")
    if not isinstance(queue, list):
        raise TypeError("Queues must be lists.")
    for person in queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")
    if not isinstance(person_name, str):
        raise TypeError("Person name must be a string.")

    return queue.count(person_name)

def remove_the_last_person(queue: list) -> list:
    """Remove the person in the last index from the queue and return their name.
 
    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    if queue is None:
        raise ValueError("Missing input.")
    if not isinstance(queue, list):
        raise TypeError("Queues must be lists.")
    for person in queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")

    return queue.pop()

def sorted_names(queue: list) -> list:
    """Sort the names in the queue in alphabetical order and return the result.
 
    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    if queue is None:
        raise ValueError("Missing input.")
    if not isinstance(queue, list):
        raise TypeError("Queues must be lists.")
    for person in queue:
        if not isinstance(person, str):
            raise TypeError("Persons in queues must be strings.")

    return sorted(queue)
