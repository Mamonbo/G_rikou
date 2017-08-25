#!/usr/bin/env python
# -*- coding: utf-8 -*-
#last update:2014/10/10

#import tweepy
import sys
import codecs
import os
import webbrowser
import wx



#.rstrip("\n")
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
global Verifier
Verifier=0
#GUIいじりその1----------------------------------------------------------------------------------------------------------------------------
applicationoath = wx.App()
frame = wx.Frame(None,wx.ID_ANY,u"認証", style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,size=(400,225))#デフォは横400、たて220ちょい
frame.SetBackgroundColour("#e8e8e8")
        
panel = wx.Panel(frame,wx.ID_ANY,pos=(50,80),size=(300,30))
text = wx.TextCtrl(panel,wx.ID_ANY,u"ブラウザに表示されるPIN番号を入力してください",size=(300,20))
#GUIいじりその1-----------------------------------------------------------------------------------------------------------------------------------
def pinsend(event):
    global Verifier
    Verifier=text.GetValue()
    print(text.GetValue())
    wx.Exit()
    frame.Destroy()
    #Close()
    


def oath(CK,CS):

    auth = tweepy.OAuthHandler(CK, CS)

    access=os.path.exists("./access.txt")
    if access==False:
        try:
            redirect_url = auth.get_authorization_url()
            print("Redirect URL: " + redirect_url)
            webbrowser.open(redirect_url)
        except tweepy.TweepError:
            print("Error! Failed to get request token.")

    # Example w/o callback (desktop)
    #verifier = raw_input("Verifier: ")

    # Get access token
    if access==False:
        #verifier = raw_input("Verifier: ")
#----------------------------------------------GUIいじり2---------------------------------------------------------------------------

        
        PIN_panel = wx.Panel(frame,wx.ID_ANY,pos=(160,150),size=(80,20))
        button_PIN = wx.Button(PIN_panel,wx.ID_ANY,u"送信",size=(80,20))
        #Verifier=text.GetValue()
        button_PIN.Bind(wx.EVT_BUTTON,pinsend)
        frame.Show()
        applicationoath.MainLoop()
        
        
#-----------------------------------------------GUIいじり2-------------------------------------------------------------------------------
        print(Verifier)
        auth.get_access_token(Verifier)
        
        key=auth.access_token.key
        f = open("access.txt", "a")
        f.write(key.encode('base64'))
        f.close()
        key = auth.access_token.key
        print("OAuth access token (key): " + key)

        secret = auth.access_token.secret
        f = open("access.txt", "a")
        f.write(secret.encode('base64'))
        f.close()
        print("OAuth access token (secret): " + secret)
    else:
        f = open("access.txt","r")
        line=f.readlines()
        key,secret=line[0].rstrip("\n"),line[1]
        key=key.decode('base64')
        secret=secret.decode('base64')
        
        f.close()
    return key,secret

#auth.set_access_token(oath(consumer_key,consumer_secret))これはダメ(返り値が二つの値のペアになってるため？)

