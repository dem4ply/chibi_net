import mmap
import os
from chibi_file import current_dir, join
from urllib import request


def download( url, directory=None, file_name=None ):
    if directory is None:
        directory = current_dir()

    if file_name is None:
        file_name = url.rsplit( '/', 1 )[1]
    response = request.urlopen( url )
    with open( join( directory, file_name ), 'wb' ) as file:
        file.write( response.read() )
