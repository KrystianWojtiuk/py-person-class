class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_classes = []
    for person in people:
        person_to_add = Person(person["name"], person["age"])
        if "wife" in person:
            if person["wife"]:
                person_to_add.wife = person["wife"]
        elif "husband" in person:
            if person["husband"]:
                person_to_add.husband = person["husband"]
        people_classes.append(person_to_add)

    for person in people_classes:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return people_classes
