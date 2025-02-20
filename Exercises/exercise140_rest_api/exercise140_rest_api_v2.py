"""REST API exercise"""

from json import dumps, loads

class RestAPI:
    """Simple REST class that handles user balance operations."""

    def __init__(self, database=None, /):

        self._database = database

    def get(self, url, payload=None, /) -> str:
        """Returns the requested user data.
 
        :param str url: The method's URL.
        :param str payload: The method's payload, defaults to None
        :return str: The response.
        """

        if payload is None and url == "/users":
            return dumps(self._database)
        requested_users = loads(payload)
        response_users = []
        for user in sorted(requested_users["users"]):
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

        request_payload = loads(payload)
        if url == "/add":
            return dumps(self._add_user(request_payload["user"]))
        if url == "/iou":
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
