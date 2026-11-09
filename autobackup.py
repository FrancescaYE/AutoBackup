from pathlib import Path
import shutil
import datetime
import logging
import hashlib

BASE_DIR = Path(__file__).resolve().parent
source = BASE_DIR / "test_documents"
destination = BASE_DIR / "backups"
journaux = BASE_DIR / "logs"
timestamp = datetime.datetime.now().strftime("backup_%Y-%m-%d_%H-%M-%S")
backup_path = destination / timestamp

def calculate_hash(chemin):
  empreinte = hashlib.sha256(chemin.read_bytes()).hexdigest()
  return empreinte

#creer le dossier logs sil nexiste pas
journaux.mkdir(exist_ok=True)
logging.basicConfig(
  filename = journaux / "autobackup.log",
  level = logging.INFO,
  format = "%(asctime)s - %(levelname)s - %(message)s"
)



#mode dry_run
dry_run = False
if dry_run:
  print("MODE SIMULATION")
  print(f"Dossier source: {source}")
  print(f"Destination prévue: {backup_path}")
  print("Aucune copie n'a été effectuée")
else:
  if source.exists() and source.is_dir(): 
    try:
      destination.mkdir(exist_ok=True)
      shutil.copytree(source, backup_path)
      logging.info("Sauvegarde terminée")

       #verifier si chaque element de source est un fichier
      for fichier in source.rglob("*"):
        if fichier.is_file():
          chemin_relatif = fichier.relative_to(source)
          fichier_backup =backup_path / chemin_relatif 
          empreinte_source = calculate_hash(fichier)
          empreinte_backup = calculate_hash(fichier_backup)
           #comparer les deux empreintes
          if empreinte_source == empreinte_backup:
            logging.info(f"Le fichier {fichier} est vérifié")
          else:
            logging.error(f"La vérification du fichier {fichier} a échoué") 

    except PermissionError as e:
      logging.error(f"Permissions insuffisantes: {e}")
    except FileNotFoundError as e:
      logging.error(f"Fichier ou dossier introuvable: {e}")
    except shutil.Error as e:
      logging.error(f"Erreur pendant la copie: {e}")  
    except OSError as e:
      logging.error(f"Autres erreurs liées au système de fichiers : {e}")      
  else:
    logging.error(f"Le dossier {source} est invalide")