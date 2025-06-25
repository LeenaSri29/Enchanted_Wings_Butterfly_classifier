import os, shutil, random

def split_data(source_dir, train_dir, val_dir, test_dir, train_split=0.7, val_split=0.15):
    for category in os.listdir(source_dir):
        path = os.path.join(source_dir, category)
        if not os.path.isdir(path): continue
        files = os.listdir(path)
        random.shuffle(files)
        n_total = len(files)
        n_train = int(n_total * train_split)
        n_val = int(n_total * val_split)

        for i, f in enumerate(files):
            src = os.path.join(path, f)
            if i < n_train:
                dest = os.path.join(train_dir, category)
            elif i < n_train + n_val:
                dest = os.path.join(val_dir, category)
            else:
                dest = os.path.join(test_dir, category)
            os.makedirs(dest, exist_ok=True)
            shutil.copy(src, os.path.join(dest, f))
