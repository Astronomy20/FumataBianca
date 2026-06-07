# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import re


def load_properties(filepath="app.properties"):
    props = {}
    if not os.path.exists(filepath):
        print(f"Errore: Il file di configurazione '{filepath}' non esiste!")
        sys.exit(1)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(filepath, "r", encoding="cp1252") as f:
            lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            props[key.strip()] = value.strip()
    return props


def validate_version(version_str):
    return bool(re.match(r'^\d+\.\d+\.\d+$', version_str))


def create_windows_version_file(config, filename="file_versione_temp.txt"):
    version_str = config.get("app_version", "0.0.0")
    app_name = config.get("app_name", "fumatabianca").lower()

    digits = version_str.split('.')
    win_version = f"{digits[0]}, {digits[1]}, {digits[2]}, 0"

    # NOTA: PyInstaller vuole 'StringStruct' e 'VarStruct'
    content = f"""VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({win_version}),
    prodvers=({win_version}),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '041004b0',
        [StringStruct('CompanyName', '{config.get("company_name", "Team")}'),
        StringStruct('FileDescription', '{config.get("file_description", "App")}'),
        StringStruct('FileVersion', '{version_str}'),
        StringStruct('InternalName', '{app_name}'),
        StringStruct('LegalCopyright', '{config.get("legal_copyright", "Copyright")}'),
        StringStruct('OriginalFilename', '{app_name}-{version_str}.exe'),
        StringStruct('ProductName', '{config.get("app_display_name", "App")}'),
        StringStruct('ProductVersion', '{version_str}')])
      ]), 
    VarFileInfo([VarStruct('Translation', [1040, 1200])])
  ]
)
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("=== Config-driven Executable Builder ===")

    config = load_properties("app.properties")

    version = config.get("app_version", "")
    spec_filename = config.get("spec_name", "FumataBianca.spec")
    version_file = "file_versione_temp.txt"

    if not version:
        print("Errore: 'app_version' non definita in app.properties!")
        sys.exit(1)

    if not validate_version(version):
        print(f"Errore: Il formato di app_version '{version}' in app.properties non è nel formato x.x.x!")
        sys.exit(1)

    if not os.path.exists(spec_filename):
        print(f"Errore: Il file '{spec_filename}' indicato nelle proprietà non esiste!")
        sys.exit(1)

    print(f"\n[1/2] Generazione risorse dettagli versione Windows ({version})...")
    create_windows_version_file(config, version_file)

    print(f"[2/2] Avvio di PyInstaller tramite {spec_filename}...")
    try:
        subprocess.run(["pyinstaller", spec_filename, "--noconfirm"], check=True)
        ext = ".exe" if os.name == "nt" else ""
        output_name = f"{config.get('app_name', 'fumatabianca').lower()}-{version}{ext}"
        print(f"\n[COMPLETATO] L'eseguibile è pronto in: dist/{output_name}")

    except subprocess.CalledProcessError as e:
        print(f"\nErrore durante la compilazione: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(version_file):
            os.remove(version_file)


if __name__ == "__main__":
    main()