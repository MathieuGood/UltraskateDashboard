#!/usr/bin/env python3
"""
Script pour démarrer l'API FastAPI avec les événements pré-chargés.
"""

import sys
from file_manager import FileManager
from models.event import Event
from models.event_registry import EventRegistry


def load_events():
    """Charge tous les événements depuis les fichiers JSON."""
    json_files = FileManager.get_all_json_in_dir("scraped_events_save")

    if not json_files:
        print("⚠️  Aucun fichier d'événement trouvé dans 'scraped_events_save/'")
        return False

    for file in json_files:
        try:
            event = Event.from_json_file(file)
            EventRegistry.add_event(event)
            print(f"✓ Chargé: {event.track.city} {event.date.year}")
        except Exception as e:
            print(f"✗ Erreur lors du chargement {file}: {e}")

    return len(EventRegistry.events) > 0


if __name__ == "__main__":
    print("🚀 Démarrage de l'API UltraskateDashboard...\n")

    # Charger les événements
    print("📂 Chargement des événements...")
    if load_events():
        print(f"\n✓ {len(EventRegistry.events)} événement(s) chargé(s)\n")
    else:
        print("\n⚠️  Aucun événement chargé - l'API fonctionnera en mode vide\n")

    # Démarrer le serveur
    import uvicorn
    from api.app import app

    print("🌐 Serveur en cours de démarrage...")
    print("📖 Documentation: http://localhost:8000/docs")
    print("🛑 Appuyez sur CTRL+C pour arrêter\n")

    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        print("\n\n✓ API arrêtée")
        sys.exit(0)
