class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_classes = [Person(person["name"],
                      person["age"])
                      for person in people]

    for person in zip(people_classes, people):
        if person[1].get("wife"):
            person[0].wife = Person.people[person[1]["wife"]]
        elif person[1].get("husband"):
            person[0].husband = Person.people[person[1]["husband"]]

    return people_classes
