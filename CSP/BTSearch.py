import random
from typing import List, Callable, Optional, Tuple, Any


class House:
    """Represents a house with its attributes in the CSP problem."""

    ATTRIBUTES = ['number', 'color', 'nationality',
                  'pet', 'drink', 'cigarettes']

    def __init__(self):
        self.number = None
        self.color = None
        self.nationality = None
        self.pet = None
        self.drink = None
        self.cigarettes = None

    def is_solved(self) -> bool:
        """Check if all attributes of the house are assigned."""
        return all(getattr(self, attr) is not None for attr in self.ATTRIBUTES)

    def __str__(self) -> str:
        """String representation of the house."""
        values = [str(getattr(self, attr)) for attr in self.ATTRIBUTES]
        return ", ".join(values)


class Constraint:
    """Represents a constraint in the CSP problem."""

    def __init__(self, rule: Callable, needs_two_houses: bool = False):
        """
        Initialize a constraint.

        Args:
            rule: Function that validates the constraint
            needs_two_houses: Whether this constraint involves two houses
        """
        self.rule = rule
        self.needs_two_houses = needs_two_houses

    def is_satisfied(self, house1: House, house2: Optional[House] = None) -> bool:
        """Check if the constraint is satisfied."""
        if self.needs_two_houses:
            return self.rule(house1, house2)
        else:
            return self.rule(house1)


def check_all_constraints(constraints: List[Constraint], houses: List[House]) -> bool:
    """Check if all constraints are satisfied by the current house assignments."""
    for constraint in constraints:
        if constraint.needs_two_houses:
            for h1 in houses:
                for h2 in houses:
                    if h1 != h2 and not constraint.is_satisfied(h1, h2):
                        return False
        else:
            for h in houses:
                if not constraint.is_satisfied(h):
                    return False
    return True


def all_houses_solved(houses: List[House]) -> bool:
    """Check if all houses have all their attributes assigned."""
    return all(house.is_solved() for house in houses)


def remove_value(values: List[Any], value: Any) -> List[Any]:
    """Return a new list with the specified value removed."""
    return [v for v in values if v != value]


class BacktrackingSolver:
    """Solves CSP using backtracking search with constraint checking."""

    def __init__(self, constraints: List[Constraint]):
        """Initialize the solver with constraints."""
        self.constraints = constraints
        self.domains = {}

    def set_domains(self, attribute_idx: int, values: List[Any]) -> None:
        """Set the domain (available values) for an attribute."""
        self.domains[attribute_idx] = values

    def solve(self, houses: List[House], attribute_idx: int = 0, house_idx: int = 0) -> bool:
        """
        Recursively solve the CSP using backtracking.

        Args:
            houses: List of House objects to assign values to
            attribute_idx: Index of the current attribute being assigned
            house_idx: Index of the current house being processed

        Returns:
            True if a valid solution is found, False otherwise
        """
        # Check if we've assigned all attributes to all houses
        if all_houses_solved(houses) and check_all_constraints(self.constraints, houses):
            return True

        # Move to next house if current house is complete
        if attribute_idx >= len(House.ATTRIBUTES):
            return self.solve(houses, 0, house_idx + 1)

        # All houses processed
        if house_idx >= len(houses):
            return False

        attribute = House.ATTRIBUTES[attribute_idx]
        available_values = self.domains.get(attribute_idx, [])

        for value in available_values:
            # Try assigning this value
            setattr(houses[house_idx], attribute, value)

            # Check if constraints are still satisfiable
            if check_all_constraints(self.constraints, houses):
                # Recursively try to complete the assignment
                remaining_values = remove_value(available_values, value)
                self.domains[attribute_idx] = remaining_values

                if self.solve(houses, attribute_idx + 1, house_idx):
                    return True

                self.domains[attribute_idx] = available_values

            # Backtrack: undo the assignment
            setattr(houses[house_idx], attribute, None)

        return False


def create_constraints() -> List[Constraint]:
    """Create all constraints for the zebra puzzle."""
    constraints = []

    # Der Engländer wohnt im roten Haus.
    constraints.append(Constraint(
        lambda a: a.color is None or a.nationality is None or (
            a.color == "rot") == (a.nationality == "Engländer")
    ))

    # Der Spanier hat einen Hund.
    constraints.append(Constraint(
        lambda a: a.pet is None or a.nationality is None or (
            a.pet == "Hund") == (a.nationality == "Spanier")
    ))

    # Kaffee wird im grünen Haus getrunken.
    constraints.append(Constraint(
        lambda a: a.drink is None or a.color is None or (
            a.drink == "Kaffee") == (a.color == "grün")
    ))

    # Der Ukrainer trinkt Tee.
    constraints.append(Constraint(
        lambda a: a.drink is None or a.nationality is None or (
            a.drink == "Tee") == (a.nationality == "Ukrainer")
    ))

    # Das grüne Haus ist direkt rechts vom weißen Haus.
    constraints.append(Constraint(
        lambda a, b: (a.color is None or b.color is None or not ((a.color == "grün") and (b.color == "weiß"))
                      or a.number is None or b.number is None or (a.number - b.number == 1)),
        needs_two_houses=True
    ))

    # Der Raucher von Old-Gold-Zigaretten hält Schnecken als Haustiere.
    constraints.append(Constraint(
        lambda a: a.cigarettes is None or a.pet is None or (
            a.cigarettes == "OldGold") == (a.pet == "Schnecken")
    ))

    # Die Zigaretten der Marke Kools werden im gelben Haus geraucht.
    constraints.append(Constraint(
        lambda a: a.cigarettes is None or a.color is None or (
            a.cigarettes == "Kools") == (a.color == "gelb")
    ))

    # Milch wird im mittleren Haus getrunken.
    constraints.append(Constraint(
        lambda a: a.number is None or a.drink is None or (
            (a.drink == "Milch") == (a.number == 3))
    ))

    # Der Norweger wohnt im ersten Haus.
    constraints.append(Constraint(
        lambda a: a.number is None or a.nationality is None or (
            (a.nationality == "Norweger") == (a.number == 1))
    ))

    # Der Mann, der Chesterfield raucht, wohnt neben dem Mann mit dem Fuchs.
    constraints.append(Constraint(
        lambda a, b: ((a.cigarettes is None or b.pet is None or not ((a.cigarettes == "Chesterfield") and (b.pet == "Fuchs"))
                       or a.number is None or b.number is None or (abs(a.number - b.number) == 1))
                      and not (a.cigarettes == "Chesterfield" and a.pet == "Fuchs")),
        needs_two_houses=True
    ))

    # Die Marke Kools wird geraucht im Haus neben dem Haus mit dem Pferd.
    constraints.append(Constraint(
        lambda a, b: ((a.cigarettes is None or b.pet is None or not ((a.cigarettes == "Kools") and (b.pet == "Pferd"))
                       or a.number is None or b.number is None or (abs(a.number - b.number) == 1))
                      and not (a.cigarettes == "Kools" and a.pet == "Pferd")),
        needs_two_houses=True
    ))

    # Der Lucky-Strike-Raucher trinkt am liebsten Orangensaft.
    constraints.append(Constraint(
        lambda a: a.cigarettes is None or a.drink is None or (
            a.cigarettes == "LuckyStrike") == (a.drink == "O-Saft")
    ))

    # Der Japaner raucht Zigaretten der Marke Parliaments.
    constraints.append(Constraint(
        lambda a: a.cigarettes is None or a.nationality is None or (
            a.cigarettes == "Parliaments") == (a.nationality == "Japaner")
    ))

    # Der Norweger wohnt neben dem blauen Haus.
    constraints.append(Constraint(
        lambda a, b: ((a.nationality is None or b.color is None or not ((a.nationality == "Norweger") and (b.color == "blau"))
                       or a.number is None or b.number is None or (abs(a.number - b.number) == 1))
                      and not (a.nationality == "Norweger" and a.color == "blau")),
        needs_two_houses=True
    ))

    return constraints


def main() -> None:
    """Main function to solve the zebra puzzle."""
    # Initialize domain values
    numbers = [1, 2, 3, 4, 5]
    colors = ["gelb", "blau", "rot", "weiß", "grün"]
    nationalities = ["Norweger", "Ukrainer", "Engländer", "Spanier", "Japaner"]
    pets = ["Fuchs", "Pferd", "Schnecken", "Hund", "Zebra"]
    drinks = ["Wasser", "Tee", "Milch", "O-Saft", "Kaffee"]
    cigarettes = ["Kools", "Chesterfield",
                  "OldGold", "LuckyStrike", "Parliaments"]

    # Shuffle to add some randomness
    random.shuffle(numbers)
    random.shuffle(colors)
    random.shuffle(nationalities)
    random.shuffle(pets)
    random.shuffle(drinks)
    random.shuffle(cigarettes)

    # Create houses
    houses = [House() for _ in range(5)]

    # Create and initialize solver
    constraints = create_constraints()
    solver = BacktrackingSolver(constraints)
    solver.set_domains(0, numbers)
    solver.set_domains(1, colors)
    solver.set_domains(2, nationalities)
    solver.set_domains(3, pets)
    solver.set_domains(4, drinks)
    solver.set_domains(5, cigarettes)

    # Solve the puzzle
    if solver.solve(houses):
        print("Solution found!")
        for house in houses:
            print(house)
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()
