import json
import logging


def sauvegarder_json(donnees: list[dict], chemin: str) -> None:
    """Sauvegarde une liste de dictionnaires dans un fichier JSON."""

    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)


def charger_json(chemin: str) -> list[dict]:
    """Charge les données JSON depuis un fichier."""

    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as erreur:
        logging.error("Fichier JSON corrompu : %s", erreur)
        raise ValueError(
            f"Le fichier JSON '{chemin}' est invalide."
        ) from erreur