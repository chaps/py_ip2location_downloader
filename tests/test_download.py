import os

from py_ip2location_downloader.downloader import download_free_db_zip, \
download_auth_db_zip, ProductCodeEnum, FormatEnum, IPVersionEnum
from py_ip2location_downloader.unzipper import Unzipper
from py_ip2location_downloader.number_to_ip import csv_number_to_ip


def test_free_download():
    
    download_free_db_zip("ipv4csv.zip", IP_VERSION=IPVersionEnum.IPV4, FORMAT=FormatEnum.CSV)
    csv_path = Unzipper("ipv4csv.zip").unzip()
    # csv_number_to_ip(csv_path)
    """
    Unzipper("ipv4csv.zip").unzip()
    download_free_db_zip("ipv6csv.zip", IP_VERSION=IPVersionEnum.IPV6, FORMAT=FormatEnum.CSV)
    Unzipper("ipv6csv.zip").unzip()
    download_free_db_zip("ipv4bin.zip", IP_VERSION=IPVersionEnum.IPV4, FORMAT=FormatEnum.BIN)
    Unzipper("ipv4bin.zip").unzip()
    download_free_db_zip("ipv6bin.zip", IP_VERSION=IPVersionEnum.IPV6, FORMAT=FormatEnum.BIN)
    Unzipper("ipv6bin.zip").unzip()
    """
    # csv_number_to_ip("IP2LOCATION-LITE-DB1.CSV", "new.csv")
    csv_number_to_ip("IP2LOCATION-LITE-DB1.CSV")

def test_number2ip():
    
    # download_free_db_zip("ipv4csv.zip", IP_VERSION=IPVersionEnum.IPV4, FORMAT=FormatEnum.CSV)
    # csv_path = Unzipper("ipv4csv.zip").unzip()
    csv_number_to_ip("IP2LOCATION-LITE-DB1.CSV", "new.csv")

def test_account_download():
    token = os.environ.get("IP2LOCATION_AUTH_TOKEN")
    
    download_auth_db_zip(
        "testauth.zip", 
        token,
        ProductCodeEnum.DB1,
        IPVersionEnum.IPV4,
        FormatEnum.CSV
    )
    Unzipper("testauth.zip").unzip()


def test_account_download():
    token = os.environ.get("IP2LOCATION_AUTH_TOKEN")
    
    download_auth_db_zip(
        "testauth.zip", 
        token,
        ProductCodeEnum.DB1,
        IPVersionEnum.IPV4,
        FormatEnum.CSV
    )
    csv_path = Unzipper("testauth.zip").unzip()
    
    Unzipper("testauth.zip").unzip()
