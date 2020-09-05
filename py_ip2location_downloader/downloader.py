import requests
from enum import Enum

class IPVersionEnum(Enum):
    IPV4 = ""
    IPV6 = ".IPV6"

class FormatEnum(Enum):
    CSV = "CSV"
    BIN = "BIN"

class ProductCodeEnum(Enum):
    DB1 = "DB1"
    DB3 = "DB3"
    DB5 = "DB5"
    DB9 = "DB9"
    DB11 = "DB11"
    

URL_DOWNLOAD_DB_URL = "http://download.ip2location.com/lite/IP2LOCATION-LITE-DB1{IP_VERSION}.{FORMAT}.ZIP"

URL_AUTH_DOWNLOAD_DB_URL = "https://www.ip2location.com/download/"


def download_free_db_zip(target, IP_VERSION=IPVersionEnum.IPV4, FORMAT=FormatEnum.CSV):
    """
    """
    download_url = URL_DOWNLOAD_DB_URL.format(IP_VERSION=IP_VERSION.value, FORMAT=FORMAT.value)
    response = requests.get(download_url)
    
    with open(target, "wb") as file_object:
        file_object.write(response.content)
    return response


def build_product_code_format(PRODUCT, IP_VERSION, FORMAT):

    format_value = "" if FORMAT == FormatEnum.CSV else FORMAT.value
    ip_version =  "" if IP_VERSION == IPVersionEnum.IPV4 else IP_VERSION.value
    
    return "{product}LITE{format}{ip_version}".format(
        product=PRODUCT.value,
        format=format_value,
        ip_version=ip_version
    )


def download_auth_db_zip(target, TOKEN, PRODUCT, IP_VERSION, FORMAT):
    file_code = build_product_code_format(PRODUCT, IP_VERSION, FORMAT)
    response = requests.get(
        URL_AUTH_DOWNLOAD_DB_URL,
        params={"token": TOKEN , "file": file_code},
        stream=True
    )
    with open(target, "wb") as file_object:
        for chunk in response.iter_content(chunk_size=128):
            file_object.write(chunk)
    return response
