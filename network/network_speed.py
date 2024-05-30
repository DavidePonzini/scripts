#!/usr/bin/env python

from speedtest import Speedtest
from dav_tools import messages


s = Speedtest()

messages.progress('Testing download...')
download = s.download()
messages.info(f'Download: {download / (8 * 1024 * 1024):.2f} MB/s')


messages.progress('Testing upload...')
upload = s.upload()
messages.info(f'Upload: {upload / (8 * 1024 * 1024):.2f} MB/s')

