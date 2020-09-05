

import zipfile
import os

from .downloader import download_auth_db_zip, \
    download_free_db_zip


class Unzipper:
    """
    """
    def __init__(self, target_zip):
        self.target_zip = target_zip


    def get_db_file_ref(self, zip_ref_namelist):
        for name in zip_ref_namelist:
            lowered_case_name = name.lower()
            if lowered_case_name.endswith(".bin") or lowered_case_name.endswith(".csv"):
                return name
        raise Exception("No database file found.")


    def unzip(self, target_path=None, only_db=True, delete_zip=True):
        """
        """
        with zipfile.ZipFile(self.target_zip, 'r') as zip_ref:
            
            if only_db:
                print(zip_ref.namelist())
                file_name_ref = self.get_db_file_ref(zip_ref.namelist())

                zip_ref.extract(file_name_ref, path=target_path)
            else:
                zip_ref.extractall(path=target_path)
        if delete_zip:
            os.remove(self.target_zip)
