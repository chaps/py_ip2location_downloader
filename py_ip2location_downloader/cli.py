"""Console script for py_ip2location_downloader."""
import argparse
import sys
from .unzipper import Unzipper
from .downloader import download_free_db_zip, \
    download_auth_db_zip
from .number_to_ip import csv_number_to_ip
import tempfile
import os

class CliUtil:
    def __init__(
        self, download_path=None, download_type="free", ipversion="ipv4", _format="CSV", 
        unzip=True, numbertoipv4=True,
        *args, **kwargs
    ):
        if download_path:
            self.download_path = download_path
        else:
            self.download_path = os.path.join(tempfile.gettempdir(), "ip2location_db.zip")
        
        self.download_type = download_type
        self.ipversion = ipversion
        self.format = _format
        self.unzip = unzip
        self.numbertoipv4 = numbertoipv4


    def exec(self, token=None):
        if self.download_type == "free":
            download_free_db_zip(self.download_path)
        else:
            token = token if token else os.environ.get("IP2LOCATION_AUTH_TOKEN")
            download_auth_db_zip(TOKEN=token)
        if self.unzip:
            output_path = Unzipper(self.download_path).unzip()
            if self.numbertoipv4:
                csv_number_to_ip(output_path)


def main():
    """Console script for py_ip2location_downloader."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--download_path", default=None,help="Free or auth")
    parser.add_argument("--download_type", default="free",help="Free or auth")
    parser.add_argument("--ipversion", default="ipv4", help="IP Version format ")
    parser.add_argument("--format", default="csv", help="DB AVAILABLE FORMATS CSV or BIN")
    parser.add_argument("--product", default="db1", help="PRODUCT")
    parser.add_argument("--token", help="token used in order to authenticate in case of downloading the auth required DBs ")
    parser.add_argument("--unzip", default=True, help="")
    parser.add_argument("--numbertoipv4", default=True, help="")

    args = parser.parse_args()
    
    cli_util = CliUtil( **{x:y for x, y in args._get_kwargs()})
    cli_util.exec()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
