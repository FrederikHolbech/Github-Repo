class Pupil:
    grade_map = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "FX": 5,
        "F": 6
    }
    def __init__(self, name: str, grade: str) -> None:
        self.name = name
        for letter, value in self.grade_map.items():
            if grade.startswith(letter):
                self.grade = value
                break
        if grade.endswith("-"):
            self.modifier = -1 * grade.count("-")
        elif grade.endswith("+"):
            self.modifier = 1 * grade.count("+")
        else:
            self.modifier = 0

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        if self.grade < other.grade:
            return True
        if self.grade > other.grade:
            return False
        # Grades are the same
        if self.modifier > other.modifier:
            return True
        if self.modifier < other.modifier:
            return False
        # Grades and modifiers are the same
        return self.name < other.name
def read_input():
    pupils = []
    n = input().strip()
    for _ in range(int(n)):
        name, grade = input().strip().split(" ")
        pupils.append(Pupil(name, grade))
    return pupils



print("\n".join(str(item) for item in sorted(read_input())))