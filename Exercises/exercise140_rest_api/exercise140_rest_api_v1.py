"""REST API exercise"""

from json import dumps, loads

class RestAPI:
    """Simple REST class that handles user balance operations."""

    def __init__(self, database=None, /):

        # Thorough input validation.
        if database is not None and not isinstance(database, dict):
            raise TypeError("Database must be a dictionary.")
        if "users" not in database.keys():
            raise ValueError("Missing users category.")
        if database["users"] is None:
            raise ValueError("Missing users category.")
        if not isinstance(database["users"], list):
            raise ValueError("Users category must be a list.")
        for user in database["users"]:
            if not isinstance(user, dict):
                raise ValueError("Users must be dictionaries.")
            for subcategory in ("name", "owes", "owed_by", "balance"):
                if subcategory not in user.keys():
                    raise ValueError("Missing user subcategories.")
            if not isinstance(user["name"], str):
                raise TypeError("User names must be strings.")
            if not isinstance(user["owes"], dict):
                raise TypeError("User owes subcategory must be a dictionary.")
            if not isinstance(user["owed_by"], dict):
                raise TypeError("User owed_by subcategory must be a dictionary.")
            if not isinstance(user["balance"], float):
                raise TypeError("User balance must be a float.")
            for name, amount in user["owes"].items():
                if not isinstance(name, str):
                    raise TypeError("Lender names must be strings.")
                if not isinstance(amount, float):
                    raise TypeError("Lent amounts must be floats.")
            for name, amount in user["owed_by"].items():
                if not isinstance(name, str):
                    raise TypeError("Borrower names must be strings.")
                if not isinstance(amount, float):
                    raise TypeError("Borrowed amounts must be floats.")

        self._database = database

    def get(self, url, payload=None, /) -> str:
        """Returns the requested user data.
 
        :param str url: The method's URL.
        :param str payload: The method's payload, defaults to None
        :return str: The response.
        """

        # Input validation.
        if url is None or not url:
            raise ValueError("Missing URL.")
        if not isinstance(url, str):
            raise TypeError("URL must be a string.")
        if url != "/users":
            raise ValueError("Invalid URL.")
        if payload is not None:
            if not isinstance(payload, str):
                raise TypeError("Payload must be in a string format.")

        if payload is None and url == "/users":
            return dumps(self._database)
        requested_users = loads(payload)

        # Input validation.
        if not isinstance(requested_users, dict):
            raise TypeError("Payload must be a dictionary.")
        if "users" not in requested_users.keys():
            raise ValueError("Missing users category.")
        if requested_users["users"] is None or not requested_users["users"]:
            raise ValueError("Missing users list.")
        if not isinstance(requested_users["users"], list):
            raise TypeError("Users list must ba a list.")

        response_users = []
        for user in sorted(requested_users["users"]):
            # Input validation.
            if user is None or not user:
                raise ValueError("Missing user name.")
            if not isinstance(user, str):
                raise TypeError("User names must be strings.")

            for db_user in self._database["users"]:
                if db_user["name"] == user:
                    response_users.append(db_user)
        return dumps({"users": response_users})

    def post(self, url, payload=None, /) -> str:
        """Responds to add and IOU requests. Add creates a new user. IOU updates the database's
        balances for the given lender and borrower. 
 
        :param str url: The request URL.
        :param str payload: The request contents, defaults to None.
        :return str: The response to the request. Add returns the new user data. IOU returns the
                     lender's and borrower's data. 
        """

        # Input validation.
        if url is None or not url:
            raise ValueError("Missing URL.")
        if not isinstance(url, str):
            raise TypeError("URL must be a string.")
        if url not in ("/add", "/iou"):
            raise ValueError("Invalid URL.")
        if payload is None or not payload:
            raise ValueError("Missing payload.")
        if not isinstance(payload, str):
            raise TypeError("Payload must be in a string format.")

        request_payload = loads(payload)

        # Input validation.
        if not isinstance(request_payload, dict):
            raise TypeError("Payload must be a dictionary.")

        if url == "/add":
            # Input validation.
            if "user" not in request_payload.keys():
                raise ValueError("Missing user category.")
            if request_payload["user"] is None or not request_payload["user"]:
                raise ValueError("Missing user name.")
            if not isinstance(request_payload["user"], str):
                raise TypeError("User name must ba a string.")

            return dumps(self._add_user(request_payload["user"]))

        if url == "/iou":
            # Input validation.
            if "lender" not in request_payload.keys():
                raise ValueError("Missing lender category.")
            if "borrower" not in request_payload.keys():
                raise ValueError("Missing borrower category.")
            if "amount" not in request_payload.keys():
                raise ValueError("Missing amount category.")
            if request_payload["lender"] is None or not request_payload["lender"]:
                raise ValueError("Missing lender name.")
            if request_payload["borrower"] is None or not request_payload["borrower"]:
                raise ValueError("Missing borrower name.")
            if request_payload["amount"] is None or not request_payload["amount"]:
                raise ValueError("Missing amount.")
            if not isinstance(request_payload["lender"], str):
                raise TypeError("Lender name must ba a string.")
            if not isinstance(request_payload["borrower"], str):
                raise TypeError("Borrower name must ba a string.")
            if not isinstance(request_payload["amount"], float):
                raise TypeError("Amount must ba a float.")

            lender = request_payload["lender"]
            leant = False
            borrower = request_payload["borrower"]
            borrowed = False
            amount = request_payload["amount"]

            for index, user in enumerate(self._database["users"]):
                if user["name"] == lender:
                    amount_balance = amount
                    user_owes = borrower in self._database["users"][index]["owes"]
                    if not user_owes:
                        user_owed = lender in self._database["users"][index]["owed_by"]
                    if user_owes:
                        amount_balance -= self._database["users"][index]["owes"][borrower]
                        self._database["users"][index]["owes"][borrower] -= amount
                        if self._database["users"][index]["owes"][borrower] <= 0:
                            self._database["users"][index]["owes"].pop(borrower)
                        if amount_balance > 0:
                            self._database["users"][index]["owed_by"][borrower] = amount_balance
                    elif user_owed:
                        self._database["users"][index]["owed_by"][borrower] += amount_balance
                    else:
                        self._database["users"][index]["owed_by"][borrower] = amount
                    self._database["users"][index]["balance"] += amount
                    borrowed = True
                elif user["name"] == borrower:
                    amount_balance = amount
                    user_owes = lender in self._database["users"][index]["owes"]
                    if not user_owes:
                        user_owed = lender in self._database["users"][index]["owed_by"]
                    if user_owed:
                        amount_balance -= self._database["users"][index]["owed_by"][lender]
                        self._database["users"][index]["owed_by"][lender] -= amount
                        if self._database["users"][index]["owed_by"][lender] <= 0:
                            self._database["users"][index]["owed_by"].pop(lender)
                        if amount_balance > 0:
                            self._database["users"][index]["owes"][lender] = amount_balance
                    elif user_owes:
                        self._database["users"][index]["owes"][lender] += amount
                    else:
                        self._database["users"][index]["owes"][lender] = amount
                    self._database["users"][index]["balance"] -= amount
                    leant = True
                if borrowed and leant: 
                    break
            return self.get("/users", dumps({"users": [lender, borrower]}))

    def _add_user(self, name, /) -> dict:
        """Adds the given user to the database."""

        new_user = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
        self._database["users"].append(new_user)
        return new_user
