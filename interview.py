import random

class RandomDraw:
    def prepare_data(self, participants):
        for tup in participants:
            person1 = tup[0]
            person2 = tup[1]
            self.list_persons.append(person1)
            self.list_persons.append(person2)
            self.map_partners[person1] = person2
            self.map_partners[person2] = person1

    def __init__(self, participant_list):
        # TODO: check for duplicates
        self.participants = participant_list # [(a, b), (c, d)]
        self.map_partners = {}
        self.list_persons = []
        self.prepare_data(participant_list)

    def condition(self, cur_person, potential_receiver, taken_indices):
        return (potential_receiver not in taken_indices and self.list_persons[potential_receiver] != cur_person and self.map_partners[cur_person] != self.list_persons[potential_receiver])
            

    def random_draw(self):
        taken_indices = set()
        final_pairs = []
        for i in range(len(self.list_persons)):
            cur_person = self.list_persons[i]
            potential_receiver = random.randint(0, len(self.list_persons) - 1)

            while not self.condition(cur_person, potential_receiver, taken_indices):
                potential_receiver = random.randint(0, len(self.list_persons) - 1)

            final_pairs.append((cur_person, self.list_persons[potential_receiver]))
            taken_indices.add(i)
            taken_indices.add(potential_receiver)

        print(final_pairs)
        return final_pairs
    
if __name__ == '__main__':
    rd = RandomDraw([("a", "b"), ("c", "d"), ("e", "f")])
    rd.random_draw()

