import json
import random
from pprint import pprint

from docopt import docopt


class Person(object):
    def __init__(self, name: str, favor_list: list):
        """
        parameters:
            name(string) - a name of this object; used as an id
            favor_list(list) - a list of names ordered by preference
        """
        self.name = name
        self.favor_list = favor_list
        self.suitor = None

    def __repr__(self):
        return str(self.favor_list)

    def __eq__(self, other):
        return self.name == other

    def get_favor_list(self):
        return self.favor_list.copy()

    def update_favor_list(self, names_to_delete: list):
        favor_list_copy = self.get_favor_list()
        for name in names_to_delete:
            if name in favor_list_copy:
                favor_list_copy.remove(name)

        self.favor_list = favor_list_copy

    def set_suitor(self, name):
        self.suitor = name


class Woman(Person):
    def __init__(self, name: str, favor_list: list):
        super().__init__(name, favor_list)

    def __repr__(self):
        return super().__repr__()

    def make_decision(self, suitors: list):
        """
        Choose a man, who she favors the most, from the given suitors

        return string
        """
        favor_list = self.get_favor_list()
        return favor_list[min([favor_list.index(man) for man in suitors])]


class Man(Person):
    def __init__(self, name: str, favor_list: list):
        super().__init__(name, favor_list)

    def __repr__(self):
        return super().__repr__()

    def serenade(self):
        """
        Serenade to a woman who he favors the most.
        If he already has his suitor, then he serenades to her.

        exception: ValueError when a man has an empty list
        return string
        """
        if not self.favor_list:
            raise ValueError('Empty list')

        if not self.suitor:
            return self.favor_list[0]

        return self.suitor


def prepare_ritual(num_of_people=10):
    MEN = ['m' + str(i) for i in range(num_of_people)]
    WOMEN = ['w' + str(i) for i in range(num_of_people)]

    men_dict, women_dict = dict(), dict()

    for name in MEN:
        random.shuffle(WOMEN)
        men_dict[name] = Man(name, WOMEN.copy())

    for name in WOMEN:
        random.shuffle(MEN)
        women_dict[name] = Woman(name, MEN.copy())

    return men_dict, women_dict


def ritual(men, women, verbose=False):
    day_count = 0

    while True:
        serenade_status, serenade_logs, decision_logs = dict(), list(), list()

        # Terminate when all women has a suitor
        if all([w.suitor for w in women.values()]):
            return {w.suitor: w.name for w in women.values()}, day_count

        # Men serenade to his most favorite woman
        for name, man in men.items():
            woman_name = man.serenade()
            serenade_status[woman_name] = serenade_status.get(woman_name, [])
            serenade_status[woman_name].append(name)

            serenade_logs.append((name, man.favor_list))

        # Women choose her favorite man
        for woman_name, suitors in serenade_status.items():
            woman = women.get(woman_name)
            chosen_man = woman.make_decision(suitors)
            decision_logs.append((woman.name, chosen_man))

            for suitor in suitors:
                if suitor is chosen_man:
                    # set as a suitor
                    men[chosen_man].set_suitor(woman_name)
                    woman.set_suitor(chosen_man)

                else:
                    # cross out the women from his list
                    men[suitor].set_suitor(None)
                    men[suitor].update_favor_list([woman_name])

        if verbose:
            print('\nDAY {}:'.format(day_count))
            print("== MEN'S LIST ==")
            for prog in sorted(serenade_logs, key=lambda x: int(x[0][1:])):
                print(prog)
            print('== SERENADES ==')
            pprint(serenade_status)
            print("== WOMEN'S CHOICE ==")
            for prog in sorted(decision_logs, key=lambda x: int(x[0][1:])):
                print(prog)

        day_count += 1


if __name__ == '__main__':
    doc = """The Mating Ritual.

    Usage:
        the_mating_ritual.py (-c COUNT) [-v] [-s FILE]

    Arguments:
        COUNT   a number of people
        FILE    optional output file

    Options:
        -c --count      a number of people
        -s --save       save results to a txt file
        -v --verbose    print more text
    """
    args = docopt(doc)

    # Create men and women set for a ritual
    men, women = prepare_ritual(num_of_people=int(args['COUNT']))
    print('===MEN===')
    pprint(men)
    print('==WOMEN==')
    pprint(women)

    # Execute the ritual
    result, day = ritual(men, women, verbose=args['--verbose'])

    # Reformat the result
    result = sorted(result.items(), key=lambda x: int(x[0][1:]))
    print('\n==STABLE COUPLES AFTER {} DAYS=='.format(day))
    pprint(dict(result))

    # Save the result
    if args['--save']:
        with open('./{}'.format(args['FILE']), 'w') as f:
            json.dump(dict(result), f)
