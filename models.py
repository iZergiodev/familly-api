
    
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        data = member
        self._members.append(data)
        pass

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                del self._members[i]
                return self._members       
        pass

    def get_member(self, id):
        
        for member in self._members:
            if member['id'] == id:
                return member


    def get_all_members(self):
        return self._members