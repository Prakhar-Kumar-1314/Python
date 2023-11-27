class Group:
    def __init__(self, name, members=None):
        if members is None:
            members = []
        self.name = name
        self.members = members

    def add(self, name2):
        self.members.append(name2)

    def delete(self, name2):
        if name2 not in self.members:
            raise Exception("Member not in group")
        else:
            self.members.remove(name2)

    def get_members(self):
        self.members = sorted(self.members)
        return self.members

    def merge(self, group):



