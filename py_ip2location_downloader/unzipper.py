

import zipfile
import os

import tempfile


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
        # TODO: implement rename DB file: os.rename(src, dst)
        with zipfile.ZipFile(self.target_zip, 'r') as zip_ref:
            file_name_ref = self.get_db_file_ref(zip_ref.namelist())
            if only_db:
                zip_ref.extract(file_name_ref, path=target_path)
            else:
                zip_ref.extractall(path=target_path)
        if delete_zip:
            os.remove(self.target_zip)
        if target_path:
            output_path = os.path.join(target_path, file_name_ref)
        else:
            output_path = os.path.join(os.getcwd(), file_name_ref)
        # LOG
        print("DB unzipped and located at {}".format(output_path))    
        
        return output_path
        