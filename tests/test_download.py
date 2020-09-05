import os

from py_ip2location_downloader.downloader import download_free_db_zip, \
download_auth_db_zip, ProductCodeEnum, FormatEnum, IPVersionEnum
from py_ip2location_downloader.unzipper import Unzipper
import zipfile


def test_free_download():
    
    download_free_db_zip("ipv4csv.zip", IP_VERSION=IPVersionEnum.IPV4, FORMAT=FormatEnum.CSV)
    Unzipper("ipv4csv.zip").unzip()
    download_free_db_zip("ipv6csv.zip", IP_VERSION=IPVersionEnum.IPV6, FORMAT=FormatEnum.CSV)
    Unzipper("ipv6csv.zip").unzip()
    download_free_db_zip("ipv4bin.zip", IP_VERSION=IPVersionEnum.IPV4, FORMAT=FormatEnum.BIN)
    Unzipper("ipv4bin.zip").unzip()
    download_free_db_zip("ipv6bin.zip", IP_VERSION=IPVersionEnum.IPV6, FORMAT=FormatEnum.BIN)
    Unzipper("ipv6bin.zip").unzip()


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
