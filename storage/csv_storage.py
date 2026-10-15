import csv


def exporter_csv(donnees: list[dict], chemin: str, champs: list[str]) -> None:
    """Exporte une liste de dictionnaires vers un fichier CSV."""

    with open(chemin, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=champs)

        writer.writeheader()

        writer.writerows(donnees)


def importer_csv(chemin: str) -> list[dict]:
    """Importe les données depuis un fichier CSV."""

    try:
        with open(chemin, "r", newline="", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            return list(reader)

    except FileNotFoundError:
        return []