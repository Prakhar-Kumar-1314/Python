class Group:
    def __init__(self, name, members=[]):
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


g1 = Group("A-Team", ["Tim", "Joel"])
g1.add("Sally")
g1.add("Billy")

members = g1.get_members()
print(members)

g1.delete("Joel")
members = g1.get_members()
print(members)

g1.delete("Joe")
members = g1.get_members()
print(members)