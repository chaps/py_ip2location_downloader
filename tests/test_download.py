import os

from py_ip2location_downloader.downloader import download_free_db_zip, \
download_auth_db_zip, ProductCodeEnum, FormatEnum, IPVersionEnum


def test_download():
    download_free_db_zip("test.zip")


def test_account_download():
    token = os.environ.get("IP2LOCATION_AUTH_TOKEN")
    
    download_auth_db_zip(
        "testauth.zip", 
        token,
        ProductCodeEnum.DB1,
        IPVersionEnum.IPV4,
        FormatEnum.CSV
    )
