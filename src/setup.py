# -*- coding:utf-8 -*-
###
# --------------------------------------------------------------
# Modified Date: Thursday, 11th June 2020 12:18:03 am
# Modified By: Ritesh Singh
# --------------------------------------------------------------
###

"""
setup file will configure your Termux. Run this file first time and it will configure downloadbot command into your termux.
"""
import os


def system_default():
    """
    Run this setup file first time and it will configure your termux for youtube_downloader app.
    """
    try:
        packages = ['curl', 'ffmpeg', 'tor', 'git', 'vim']
        for i in packages:
            cmd = "pkg install {0} -y".format(i)
            os.system(cmd)
        os.system('termux-setup-storage')
        os.system('pip install -r requirements.txt')
        os.system(r'echo alias downloaderbot=\"python /data/data/com.termux/files/home/downloaderbot/source'
                  r'/downloaderbot.py\" >> /data/data/com.termux/files/usr/etc/bash.bashrc')

    except (RuntimeError, IOError, FileExistsError) as r:
        print('[-]Error: ' + str(r))


if __name__ == '__main__':
    print('Starting setup process...')
    system_default()
    print('\nProcess completed successfully')
