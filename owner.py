import os, csv
class Owner:

    def __init__(self, id, last, first, address=None, city=None, state=None):
        self.id = id
        self.last = last
        self.first = first
        self.address = address
        self.city = city
        self.state = state

    @classmethod
    def all_owners(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./support/owners.csv")
        owners_lst = []
        with open(path) as ownerfile:
            header = ['id', 'last', 'first', 'address', 'city', 'state']
            reader = csv.DictReader(ownerfile, fieldnames=header)
            for row in reader:
                owners_lst.append(Owner(**row))
        return owners_lst