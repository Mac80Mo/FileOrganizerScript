# Datei-Organizer Skript

Dieses Python-Skript organisiert Dateien aus einem definierten Basisverzeichnis, indem es sie basierend auf ihrer Dateiendung in verschiedene Unterordner verschiebt. Es wurde speziell entwickelt, um den Ordner `dateien` (relativ zum Skript) aufzuräumen, indem Dateien in die Kategorien Bilder, Dokumente, Code und Sonstiges einsortiert werden.

## Funktionsweise

- **Basisverzeichnis:**  
  Das Skript arbeitet mit dem Ordner `dateien`, der sich im selben Verzeichnis wie das Skript befindet.  
  *Hinweis:* Möchtest Du ein anderes Basisverzeichnis (z. B. den Downloads-Ordner) verwenden, passe die Zuweisung der Variable `folder` an.

- **Erstellen von Unterordnern:**  
  Es werden automatisch vier Unterordner im Basisverzeichnis erstellt, falls diese noch nicht existieren:
  - **Bilder:** Für Bilddateien (Dateiendungen `.png` und `.jpg`).
  - **Dokumente:** Für Dokumente (Dateiendungen `.txt` und `.docx`).
  - **Code:** Für Quellcodedateien (Dateiendungen `.cpp`, `.py` und `.php`).
  - **Sonstiges:** Für alle Dateien, die keiner der oben genannten Kategorien zugeordnet werden können.

- **Dateiverarbeitung:**  
  Das Skript durchläuft alle Dateien und Ordner im Basisverzeichnis.  
  - **Ordner werden übersprungen:** Nur Dateien werden verarbeitet.  
  - **Dateiüberprüfung:** Anhand der Dateiendung wird ermittelt, in welchen Zielordner die Datei verschoben werden soll.  
  - **Verschieben:** Mit `shutil.move()` werden die Dateien in den entsprechenden Unterordner verschoben.

## Voraussetzungen

- **Python 3.x:**  
  Stelle sicher, dass Python 3.x installiert ist.

- **Dateiberechtigungen:**  
  Das Skript benötigt Lese- und Schreibrechte für das Basisverzeichnis.

## Nutzung

1. **Vorbereitung:**  
   - Lege das Skript in einem Ordner ab.
   - Stelle sicher, dass sich im selben Verzeichnis ein Ordner namens `dateien` befindet, der die zu organisierenden Dateien enthält.

2. **Ausführen:**  
   Führe das Skript über die Kommandozeile oder eine integrierte Entwicklungsumgebung (IDE) aus:
   ```bash
   python dein_skriptname.py
   ```

3. **Ergebnis:**  
   Nach der Ausführung findest Du im Ordner `dateien` die Unterordner `Bilder`, `Dokumente`, `Code` und `Sonstiges` mit den entsprechend verschobenen Dateien.

## Anpassungsmöglichkeiten

- **Basisverzeichnis ändern:**  
  Um z. B. den Downloads-Ordner als Basisverzeichnis zu nutzen, ändere die Definition der Variable `folder`:
  ```python
  folder = os.path.join(os.path.expanduser("~"), "Downloads")
  ```
  *Hinweis:* Passe ggf. den Ordnernamen an, wenn Dein System einen anderen Standardnamen verwendet (z. B. "Herunterladen").

- **Zielordnernamen anpassen:**  
  Die Namen der Zielordner (`Bilder`, `Dokumente`, `Code`, `Sonstiges`) können individuell angepasst werden. Ändere dazu einfach die entsprechenden Variablen im Skript.

## Hinweise

- **Dateitypen:**  
  - **Bilder:** `.png`, `.jpg`
  - **Dokumente:** `.txt`, `.docx`
  - **Code:** `.cpp`, `.py`, `.php`  
  Alle anderen Dateitypen werden im Ordner `Sonstiges` abgelegt.

- **Sicherheitsaspekt:**  
  Da das Skript Dateien verschiebt, empfiehlt es sich, zunächst ein Backup anzulegen oder das Skript in einem Testverzeichnis auszuprobieren, um unbeabsichtigte Datenverluste zu vermeiden.

## Fazit

Dieses Skript bietet eine einfache Möglichkeit, Dateien automatisch nach Typ zu sortieren und in entsprechende Unterordner zu verschieben. Es ist leicht anpassbar und kann als Grundlage für komplexere Dateiorganisationslösungen dienen.

---

Below is the English version of your **README.md**:

---

# File Organizer Script

This Python script organizes files from a specified base directory by moving them into different subfolders based on their file extensions. It is specifically designed to tidy up the `dateien` folder (located relative to the script) by categorizing files into Images, Documents, Code, and Others.

## How It Works

- **Base Directory:**  
  The script works with the `dateien` folder, which is located in the same directory as the script.  
  *Note:* If you want to use a different base directory (for example, the Downloads folder), simply adjust the assignment of the variable `folder`.

- **Creating Subfolders:**  
  Four subfolders are automatically created within the base directory if they do not already exist:
  - **Images:** For image files (file extensions `.png` and `.jpg`).
  - **Documents:** For document files (file extensions `.txt` and `.docx`).
  - **Code:** For source code files (file extensions `.cpp`, `.py`, and `.php`).
  - **Others:** For all files that do not match any of the above categories.

- **File Processing:**  
  The script iterates through all files and folders in the base directory.
  - **Folders are skipped:** Only files are processed.
  - **File type check:** The file extension is used to determine which target folder the file should be moved to.
  - **Moving Files:** Files are moved to the appropriate subfolder using `shutil.move()`.

## Requirements

- **Python 3.x:**  
  Ensure that Python 3.x is installed.

- **File Permissions:**  
  The script requires read and write permissions for the base directory.

## Usage

1. **Preparation:**  
   - Place the script in a folder.
   - Make sure there is a folder named `dateien` in the same directory, containing the files you want to organize.

2. **Execution:**  
   Run the script from the command line or an integrated development environment (IDE):
   ```bash
   python your_script_name.py
   ```

3. **Outcome:**  
   After execution, you will find the subfolders `Images`, `Documents`, `Code`, and `Others` inside the `dateien` folder with the respective files moved into them.

## Customization Options

- **Changing the Base Directory:**  
  For example, to use the Downloads folder as your base directory, change the definition of the variable `folder`:
  ```python
  folder = os.path.join(os.path.expanduser("~"), "Downloads")
  ```
  *Note:* Adjust the folder name if your system uses a different name (e.g., "Downloads" vs. "Herunterladen").

- **Customizing Subfolder Names:**  
  You can individually adjust the names of the target folders (`Images`, `Documents`, `Code`, `Others`) by simply modifying the respective variables in the script.

## Notes

- **File Types:**  
  - **Images:** `.png`, `.jpg`
  - **Documents:** `.txt`, `.docx`
  - **Code:** `.cpp`, `.py`, `.php`  
  All other file types will be placed in the `Others` folder.

- **Safety Considerations:**  
  Since the script moves files, it is recommended to back up your files or test the script in a safe environment first to avoid accidental data loss.

## Conclusion

This script provides an easy way to automatically sort files by type and move them into appropriate subfolders. It is easily customizable and can serve as a foundation for more complex file organization solutions.

---