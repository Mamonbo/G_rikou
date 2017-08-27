# -*- coding: utf-8 -*-
#.split(',')
#last update:2014/10/10

import wx
#import tweepy
import mastodon
tag_array1=[]
tag_array2=[]
import sys, codecs
import oath
import os
import os.path
from PIL import Image
import json


# SOMEDAY 使用している場所を見て適切なファイル名に変更する
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
otaku1exist=os.path.exists("./otaku1.txt")
otaku2exist=os.path.exists("./otaku2.txt")

if otaku1exist:
    f = open("otaku1.txt","r")
else:
    f = open("otaku1.txt","w")
    f.write("\n")
    
    f.close()
    f = open("otaku1.txt","r")

for row in f:
    #row=row.encode('utf-8')
    tag_array1.append(row.decode('utf-8'))
    tag_array1.sort()

f.close()
if otaku2exist:
    g = open("otaku2.txt","r")
else:
    g = open("otaku2.txt","w")
    g.write("\n")
    g.close()
    g = open("otaku2.txt","r")
    

for row in g:
    #row=row.encode('utf-8')
    tag_array2.append(row.decode('utf-8'))

g.close()


# ユーザー情報を読み込む
FilePointer=open('user.json','r')

Setting=json.load(FilePointer)
#print(Setting)
FilePointer.close()


# mastodon をする準備
mstdn_handler=mastodon.Mastodon(
    client_id='client_cred.txt',
    access_token='user_cred.txt',
    api_base_url=Setting['url']
)

# old twitter
# create API                                                                
api = tweepy.API(auth_handler=auth)

if __name__ == "__main__":
    #---------------使うもの諸々定義----------------------------------------

    application = wx.App()

    #---------------レイアウト定義--------------------------------------------
    layout_toukou=wx.BoxSizer(wx.VERTICAL)
    
    post_sizer=wx.GridSizer(1,1)
    #add1_sizer=wx.GridSizer(1,1)
    #add2_sizer=wx.GridSizer(1,1)

    #frame = wx.Frame(None,wx.ID_ANY,u"テストフレーム")
    frame = wx.Frame(None,wx.ID_ANY,u"グローバル理工丼",
                     style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
                     | wx.CLIP_CHILDREN,size=(360,235))#デフォは横400、たて220ちょい
    # Hint:mastodonは暗めの背景が多めなのでそれ系の背景色にするかも
    frame.SetBackgroundColour("#e8e8e8")
    frame.CreateStatusBar()
    frame.SetStatusText(u"ready")

#--------------------------関数群定義-------------------------------
def post_event(event):
    # toot する
    bun=toukou.GetValue()
    # tag1:番組名を入れる欄
    tag1=combobox_1.GetValue()
    # tag2:テレビ局名を入れる欄
    tag2=combobox_2.GetValue()
    try:        
        api.update_status(bun+" "+tag1.rstrip("\n") +" "+tag2)
        toukou.Clear()
    except:
        frame.SetStatusText(u"投稿失敗:"+bun+" "+tag1.rstrip("\n") +"
        "+tag2)

        
def OnKeyChar(event):
    key = event.GetKeyCode()
    if key  ==  wx.WXK_RETURN and checkbox.GetValue():
        post_event(event)

    else: event.Skip()


def add1(event):
    #タグ1(番組名)に現在入力してある文字列をプリセットに追加

    NewTag=combobox_1.GetValue()#.GetValue()で現在のcomboboxの値を取得可
    #能
    print(NewTag)
    
    #ファイル書き込み
    f = open( "otaku1.txt", "a" )
    try:
        
        # 文字列を追記
        f.write( (u"\n"+NewTag).encode('utf-8') )
          
    finally:
        f.close()
    #f = open("otaku1.txt","r")

    #UIへ追加
    tag_array1.append(NewTag)
    combobox_1.Append(NewTag)
    #print "add"

def add2(event):
    #タグ2(テレビ局名)に現在入力してある文字列をプリセットに追加
    NewTag=combobox_2.GetValue()#.GetValue()で現在のcomboboxの値を取得
    #可能
    print(NewTag)

    #ファイル書き込み
    f = open( "otaku2.txt", "a" )
    #print type(add_)
    try:
        
        # 文字列を追記
        f.write( (u"\n"+NewTag).encode('utf-8') )
          
    finally:
        f.close()
    #f = open("otaku2.txt","r")

    #UIへ追加
    tag_array2.append(NewTag)
    combobox_2.Append(NewTag)
    #print "add"
    
def geticon():
    os.remove("./icon.png")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key,access_secret)
    #api=tweepy.API(auth)
    me=api.me()
    iconurl=me.profile_image_url
    iconspl=iconurl.split("/")
    iconname=iconspl[-1]
    oath.download(iconurl)
    root, ext = os.path.splitext(iconurl)
    #print ext
    os.rename(iconname,'icon'+ext)
    #os.remove(iconname)
    return ext
def reauth(event):
    os.remove("./access.txt")
    #os.system("C:\Users\ymduu\Desktop\otaku_client_public\dist\otaku_client.exe")
    cd=os.getcwdu()
    #os.system(cd+"\otaku_client.exe")
    os.execl(cd+u"\グローバル理工兄弟.exe","a")

    #sys.exit()




                






if __name__ == "__main__":

    def ExitHandler(self):
        frame.Destroy()
        #os.remove("./icon.png")
        
        sys.exit()
        
    frame.Bind(wx.EVT_CLOSE, ExitHandler)

     

    #--------------------------panel------------------------------------------------------
    write_panel = wx.Panel(frame,wx.ID_ANY,pos=(10,10),size=(250,80))
    post_panel = wx.Panel(frame,wx.ID_ANY,pos=(180,100),size=(80,20))
    add1_panel = wx.Panel(frame,wx.ID_ANY,pos=(15,160),size=(160,20))
    add2_panel = wx.Panel(frame,wx.ID_ANY,pos=(180,160),size=(160,20))
    check_panel = wx.Panel(frame,wx.ID_ANY,pos=(20,100),size=(150,20))
    choice_1_panel = wx.Panel(frame,wx.ID_ANY,pos=(15,130),size=(160,26))
    choice_2_panel = wx.Panel(frame,wx.ID_ANY,pos=(180,130),size=(160,26))
    add1_panel.SetBackgroundColour("#FF0000")
    add2_panel.SetBackgroundColour("#FF0000")
    #-------------------------------button他パーツ--------------------------------------------------
    button_post = wx.Button(post_panel,wx.ID_ANY,"post",size=(80,20))
    button_add1 = wx.Button(add1_panel,wx.ID_ANY,u"タグ1追加",size=(160,20))
    button_add2 = wx.Button(add2_panel,wx.ID_ANY,u"タグ2追加",size=(160,20))
    toukou = wx.TextCtrl(write_panel,wx.ID_ANY,style=wx.TE_MULTILINE,size=(270,80))
    checkbox = wx.CheckBox(check_panel,wx.ID_ANY,u"Enterキーで投稿する")
    checkbox.SetValue(True)
    combobox_1 = wx.ComboBox(choice_1_panel,wx.ID_ANY,u"タグ1",choices=tag_array1,style=wx.CB_DROPDOWN,size=(160,26))
    combobox_2 = wx.ComboBox(choice_2_panel,wx.ID_ANY,u"タグ2",choices=tag_array2,style=wx.CB_DROPDOWN,size=(160,26))
    image = wx.Image("icon.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    button_account = wx.BitmapButton(frame, -1, image, pos=(278, 20))
    button_reauth = wx.Button(frame,wx.ID_ANY,u"再認証",size=(80,20),pos=(265, 100))
    #-------------------------------layoutに追加---------------------------------------------------
    layout_toukou.Add(toukou,flag=wx.EXPAND)
    post_sizer.Add(button_post,flag=wx.GROW)

    #----------------------------------イベント----------------------------------
    button_post.Bind(wx.EVT_BUTTON,post_event)
    button_add1.Bind(wx.EVT_BUTTON,add1)
    button_add2.Bind(wx.EVT_BUTTON,add2)
    toukou.Bind(wx.EVT_KEY_DOWN, OnKeyChar)
    button_reauth.Bind(wx.EVT_BUTTON,reauth)
    
    #write_panel.SetSizer(layout_toukou)
    

    #g_panel = wx.Panel(frame,wx.ID_ANY,pos=(270,0),size=(80,220))
    #g_panel.SetBackgroundColour("#00FF00")

    #b_panel = wx.Panel(frame,wx.ID_ANY,pos=(160,0),size=(80,300))
    #b_panel.SetBackgroundColour("#0000FF")

    frame.Show()
    
    application.MainLoop()
   
    
