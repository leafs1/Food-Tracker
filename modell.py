class Item():

    def __init__(self, id: int, name: str, amount_left: str, expiry_date: str, storage_number: int):
        self._id = id
        self._name = name
        self._amount_left = amount_left
        self._expiry_date = expiry_date
        self._storage_number = storage_number

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_amount_left(self):
        return self._amount_left

    def get_expiry_date(self):
        return self._expiry_date

    def get_storage_number(self):
        return self._storage_number

    def __repr__(self):
        return str(self._id) + " " + str(self._name)+ " " + str(self._amount_left) + " " + str(self._expiry_date)+ " " + str(self._storage_number)



