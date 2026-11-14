from pathlib import Path
import shutil
import datetime
import logging
import hashlib
import time
import argparse

BASE_DIR = Path(__file__).resolve().parent

parser = argparse.ArgumentParser(
  description = "Automated file and directory backup tool"
)
parser.add_argument("source", type=Path, help="Directory to backup")
parser.add_argument("destination", type=Path, help="Backup destination")

args = parser.parse_args()

source = args.source.resolve()
destination = args.destination.resolve()

if destination == source or source in destination.parents:
  print("Erreur: La destination ne peut pas être située dans le dossier source.")
  logging.error("Destination située dans le dossier source.")
  raise SystemExit(1)

journaux = BASE_DIR / "logs"
timestamp = datetime.datetime.now().strftime("backup_%Y-%m-%d_%H-%M-%S")
backup_path = destination / timestamp
start_time = time.perf_counter()

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
files_copied = 0
verified = 0
failed = 0
backup_success = False
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
      files_copied = sum(
        1 for fichier in backup_path.rglob("*") if fichier.is_file()
        )
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
            verified +=1
            logging.info(f"Le fichier {fichier} est vérifié")
          else:
            failed +=1
            logging.error(f"La vérification du fichier {fichier} a échoué")  

      backup_success = failed == 0  and files_copied == verified


    except PermissionError as e:
      failed +=1
      logging.error(f"Permissions insuffisantes: {e}")
    except FileNotFoundError as e:
      failed +=1
      logging.error(f"Fichier ou dossier introuvable: {e}")
    except shutil.Error as e:
      failed +=1
      logging.error(f"Erreur pendant la copie: {e}")  
    except OSError as e:
      failed +=1
      logging.error(f"Autres erreurs liées au système de fichiers : {e}")      
  else:
    failed +=1
    logging.error(f"Le dossier {source} est invalide")

end_time = time.perf_counter()
duration = end_time - start_time

status = "SUCCESS" if backup_success and failed == 0 else "FAILED"

print("\n" + "=" * 50)
print("             AUTOMATED BACKUP REPORT")
print("=" * 50)
print(f"Source          : {source}")
print(f"Destination     : {backup_path}")
print(f"Backup status   : {status}")
print(f"Date            : {datetime.datetime.now():%d/%m/%Y}")
print(f"Duration        : {duration:.2f} seconds")
print("-" * 50)
print("                 BACKUP SUMMARY")
print("-" * 50)
print(f"Files copied    : {files_copied}")
print(f"Verified        : {verified}")
print(f"Failed          : {failed}")
print("=" * 50)
