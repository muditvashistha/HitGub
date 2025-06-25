import os, shutil, datetime
import sys
import os
import difflib

if os.name == "nt":
    sys.stdout.reconfigure(encoding='utf-8')

def create_checkpoint(file_to_save, checkpoint_directory=".checkpoints"):
    current_file = os.path.abspath(file_to_save)
    base_name = os.path.basename(file_to_save)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    cp_dir = checkpoint_directory
    reference,file_extension=os.path.splitext(file_to_save)
    os.makedirs(cp_dir, exist_ok=True)

    
    cp_file = os.path.join(cp_dir, f"{timestamp}_{base_name}")
    log_file = os.path.join(cp_dir, f"{timestamp}_diff.log")

    
    files = [
        os.path.join(cp_dir, f)
        for f in os.listdir(cp_dir)
        if f.endswith(file_extension) and os.path.isfile(os.path.join(cp_dir, f))
    ]

    
    if not files:
        shutil.copy2(current_file, cp_file)
        print(f"🟢 First checkpoint saved: {cp_file}")
        return

    
    most_recent = max(files, key=os.path.getctime)

    
    with open(current_file, 'r', encoding='utf-8') as f1, open(most_recent, 'r', encoding='utf-8') as f2:
        current_lines = f1.readlines()
        recent_lines = f2.readlines()

    diff = list(difflib.unified_diff(
        recent_lines,
        current_lines,
        fromfile='Checkpoint',
        tofile='Current Version',
        lineterm=''
    ))

    
    with open(log_file, 'w', encoding='utf-8') as log:
        log.write("=== Checkpoint Created ===\n")
        log.write(f"Timestamp: {timestamp}\n")
        log.write(f"Compared: {most_recent} ↔ {current_file}\n\n")
        log.write("\n".join(diff))

    
    shutil.copy2(current_file, cp_file)
    print(f"✅ Checkpoint saved: {cp_file}")
    print(f"📄 Diff log saved: {log_file}")



def revert(current_file,checkpoint_directory=".checkpoints"):
    reference,file_extension=os.path.splitext(current_file)
    cp_dir=checkpoint_directory
    files = [
        os.path.join(cp_dir, f)
        for f in os.listdir(cp_dir)
        if f.endswith(file_extension) and os.path.isfile(os.path.join(cp_dir, f))
    ]

    if not files:
        print(f"🟡 Checkpoint Directory Empty : No file to revert to!")
        return
    
    most_recent = max(files, key=os.path.getctime)
    shutil.copy2(most_recent,current_file)
    print(f"✅ Reverted to last created checkpoint!")