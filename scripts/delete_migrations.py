"""
delete all migration files, run it at the top of project folder
run with the virtualenvwrapper virtualenv activated
"""
import os
import argparse


def delete_migrations(folder_path=None):
    """
    delete migrations given a folder, if not given,
    delete migration_files under current folder directory
    """
    # find all migration folders
    if not folder_path:
        folder_path = os.getcwd()
    for a,b,c in os.walk(folder_path):
        if a.endswith('migrations'):
            # find all migration files
            migration_files = [f for f in c if '__init__' not in f]
            for f in migration_files:
                print(os.path.join(a, f))
                # delete migration files
                os.remove(os.path.join(a, f))

if __name__ == '__main__':
    delete_migrations()
