import os
import shutil

# Basisverzeichnis, in dem sich der Ordner "dateien" befindet
# relativer Pfad (__file__) zu diesem Skript
folder = os.path.join(os.path.dirname(__file__), "dateien")

# Unterordner "Bilder" erstellen IF NOT EXISTS
imageFolder = os.path.join(folder, "Bilder")
if not os.path.isdir(imageFolder):
    os.mkdir(imageFolder)

# Unterordner "Dokumente" erstellen IF NOT EXISTS
documentsFolder = os.path.join(folder, "Dokumente")
if not os.path.isdir(documentsFolder):
    os.mkdir(documentsFolder)

# Unterordner "Code" erstellen IF NOT EXISTS
codeFolder = os.path.join(folder, "Code")
if not os.path.isdir(codeFolder):
    os.mkdir(codeFolder)

# Unterordner "Sonstiges" erstellen IF NOT EXISTS
otherFolder = os.path.join(folder, "Sonstiges")
if not os.path.isdir(otherFolder):
    os.mkdir(otherFolder)

    
# Durchlaufe alle Dateien u. Ordner im Basisverzeichnis (s.o.)
for filename in os.listdir(folder):
    fileNameWithPath = os.path.join(folder, filename)   # vollständiger Pfad d. akt. Datei od. Ordner
    
    if os.path.isdir(fileNameWithPath): # Handelt es sich um einen Ordner?
        continue                        # Wenn ja, überspringen: wir wollen keine Ordner verschieben
    
    elif filename.lower().endswith(".png") or filename.lower().endswith(".jpg"): # Falls es unterschiede Groß- & Kleinschreibung in der Dateiendung gibt.
        outFileNameWithPath = os.path.join(imageFolder, filename) # Zielordner, Zielpfad
        shutil.move(fileNameWithPath, outFileNameWithPath, filename) # Verschiebeprozess Kopie&Löschen
    
    elif filename.lower().endswith(".txt") or filename.lower().endswith(".docx"): # Falls es unterschiede Groß- & Kleinschreibung in der Dateiendung gibt.
        outFileNameWithPath = os.path.join(documentsFolder, filename) # Zielordner, Zielpfad
        shutil.move(fileNameWithPath, outFileNameWithPath, filename) # Verschiebeprozess Kopie&Löschen
    
    elif filename.lower().endswith(".cpp") or filename.lower().endswith(".py") or filename.lower().endswith(".php"): # Falls es unterschiede Groß- & Kleinschreibung in der Dateiendung gibt.
        outFileNameWithPath = os.path.join(codeFolder, filename) # Zielordner, Zielpfad
        shutil.move(fileNameWithPath, outFileNameWithPath, filename) # Verschiebeprozess Kopie&Löschen
    
    else:
        outFileNameWithPath = os.path.join(otherFolder, filename) # Zielordner, Zielpfad
        shutil.move(fileNameWithPath, outFileNameWithPath, filename) # Verschiebeprozess Kopie&Löschen
        
    

        
