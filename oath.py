# -*- coding: utf-8 -*-
#last update:2014/10/10

#import tweepy
import sys
import codecs
import os
import webbrowser
import wx
import urllib
import os.path
from PIL import Image


    
def download(url):
    #url の画像をurlのbasename(拡張子無し)で保存する

    #python 3にてurllib の名前空間を整理した
    img = urllib.request.urlopen(url)

    # mastodon (maud.io のみ?) の場合 (なんとか).png の後に
    # "?(うんたら)" が付くので、取り除く
    hyo=url.split('?')
    print(hyo)
    # '?' の前まで
    CleanUrl=hyo[0]
    print("CleanUrl:" + CleanUrl)

    filename=os.path.basename(CleanUrl)
    localfile = open( filename, 'wb')
    localfile.write(img.read())
    img.close()
    localfile.close()
    print("filename:" + filename)
    return filename
    


