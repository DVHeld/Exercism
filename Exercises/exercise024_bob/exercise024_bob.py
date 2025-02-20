"""Bob exercise"""

def response(hey_bob):
    """Bob's response.
 
    :param hey_bob: str - What is said to Bob.
    :return: str - Bob's response.
 
    This function returns a string containing Bob's answer to whatever
    is said to him. His possible answers are as follows:
 
    "Sure." This is his response if a question is asked of him.
 
    "Whoa, chill out!" This is his answer if he's yelled at.
    
    "Calm down, I know what I'm doing!" This is what he says if a question
    is yelled at him.
    
    "Fine. Be that way!" This is how he responds to silence.
 
    "Whatever." This is what he answers to anything else.
    """

    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob.strip()[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip()[-1] == "?":
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
