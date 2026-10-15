from pathlib import Path

from storage.json_storage import sauvegarder_json, charger_json
from storage.csv_storage import exporter_csv, importer_csv


if __name__ == "__main__":

    # 1. Préparer les chemins
    dossier_data = Path("data")
    dossier_data.mkdir(exist_ok=True)

    chemin_json = str(dossier_data / "historique.json")
    chemin_csv = str(dossier_data / "export.csv")

    # 2. Créer les données de démonstration
    donnees = [
        {
            "nom": "Kévin",
            "ville": "Kinshasa",
            "age": 32,
            "actif": True
        },
        {
            "nom": "François",
            "ville": "Matadi",
            "age": 28,
            "actif": False
        }
    ]

    # 3. Sauvegarder et recharger le JSON
    sauvegarder_json(donnees, chemin_json)
    donnees_json = charger_json(chemin_json)

    print("=== DONNÉES JSON ===")
    print(donnees_json)

    # Vérifier la conservation des types
    assert donnees_json == donnees
    assert isinstance(donnees_json[0]["age"], int)
    assert isinstance(donnees_json[0]["actif"], bool)

    print("JSON : types conservés avec succès !")

    # 4. Exporter et importer le CSV
    champs = ["nom", "ville", "age", "actif"]

    exporter_csv(donnees, chemin_csv, champs)
    donnees_csv = importer_csv(chemin_csv)

    print("\n=== DONNÉES CSV ===")
    print(donnees_csv)

    # Vérifier que les nombres sont devenus des chaînes
    assert isinstance(donnees_csv[0]["age"], str)
    assert isinstance(donnees_csv[0]["actif"], str)

    print("CSV : valeurs relues sous forme de chaînes !")

    # 5. Tester un fichier inexistant
    resultat = charger_json("data/inexistant.json")

    assert resultat == []

    print("\nFichier inexistant : erreur gérée avec succès !")
    print("\nTOUS LES TESTS SONT VALIDÉS !")

# 6. Tester un fichier JSON corrompu
print("\n=== TEST JSON CORROMPU ===")

try:
    charger_json("data/corrompu.json")

except ValueError as erreur:
    print("Erreur détectée correctement :", erreur)

# 7. Tester une erreur de permission
from unittest.mock import patch

print("\n=== TEST PERMISSION REFUSÉE ===")

try:
    with patch(
        "storage.json_storage.open",
        side_effect=PermissionError("Accès refusé (test simulé)")
    ):
        sauvegarder_json(donnees, chemin_json)

except PermissionError as erreur:
    print("PermissionError détectée correctement :", erreur)