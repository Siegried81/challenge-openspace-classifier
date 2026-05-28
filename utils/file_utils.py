def load_people(filepath: str) -> list[str]:
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]