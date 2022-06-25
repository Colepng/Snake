import json
import socket
import sqlite3 as sql
import pickle
from types import NoneType
import urllib.request
from fun import get_highscore, update_account_highscore
from settings import load_account_settings, write_logged
import time


def main(fun, username, password=None, public_username=None, highscore=None, settings=None):

    #A loop that recives data from the server and decodes it
    def loop():

        while 1:
            data = server.recv(1024)


            if data != None and data != b'':
                #decodes the data
                data_decoded = data.decode('utf-8')
                print(data_decoded)

                #splits the data
                data_split = data_decoded.split(" ")
                print(data_split)
                command = data_split[0]
                print(command)
                
                
                if command == "sync":
                    #Opens the database
                    with open("Snake.sqlite3","wb") as f:
                        while 1:
                            print("im stuck in sync")
                            f_reading = server.recv(4096)
                            if not f_reading:
                                print("not reading")
                                if fun == "create_user":
                                    return "good", "good"
                                break
                            #Writes the data sent from sever to the file
                            f.write(f_reading)
                    break

                
                
                elif command == "invaild_valid":
                    username_good_bad = data_split[1]
                    p_username_good_bad = data_split[2]
                    print(data_split)

                    return username_good_bad, p_username_good_bad
                    
                elif command == "created_user":
                    print("user created")
                    sync()

                elif command == "sync_done":
                    return "good", "good"
                
                elif command == "updated_highscore":
                    return "updated_highscore"
                    
    #Checks if the computer has a internet connection
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    def connect_server(return_server=False):
        print(socket.gethostbyname(socket.gethostname()))

        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 8081

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.connect((HOST,PORT))
        if return_server:
            return server

    if connect():
        server = connect_server(True)

    else:
        print("Cant connect to the server with out an internet connection")

    def sync():
        server.send("sync".encode("utf-16"))

    def update_highscore(username, highscore):
        server.send(f"update_highscore {username} {highscore}".encode("utf-16"))
        loop()

    def login_user(username, password):
        #If the computer has a internet connection then it will try and sync the local database
        if connect():
            sync()
            loop()
        else:
            print("Can not acsess the internet, so using the newest database on this computer")
        #Connects to the database
        con = sql.connect("Snake.sqlite3")
        cur = con.cursor()

        get_username = f"SELECT username, password FROM Snake WHERE username = '{username}' and password = '{password}'"
        cur.execute(get_username)#Executes the sql code
        fetch = cur.fetchone()#Fetchs what the sql code returned
        print(fetch)
        if type(fetch) != NoneType:
            select_highscore  = f"SELECT highscore FROM Snake WHERE username = '{username}'"
            cur.execute(select_highscore)
            fetch_highscore = cur.fetchone()
            print(fetch_highscore[0], "test")
            update_account_highscore(fetch_highscore[0])
            load_account_settings(username)
            write_logged(True)
            return True
        else:
            con.close()
            return False



    #A function that creates a user
    def create_user(username, public_username, password):
        server.sendall(f"create_user {username} {public_username} {password} {0}".encode("utf-16"))
        loop_test = loop()
        print(loop_test)
        return loop_test


    #Logins the user
    if fun == "login":
        print("login")
        print(username,password)
        if login_user(username,password):
            print("username and password correct welcome")
            with open("username.json","w") as f:
                json.dump(username,f)
            return True
        else:
            print("username or password incorrect")
            return False

    #Creates the user
    elif fun == "create_user":
        print("create_user")
        print(username, public_username)
        return create_user(username, public_username, password)

    #syncs the database
    elif fun == "sync":
        update_highscore(username, highscore)
        sync()
        loop()
        print("ending sync function")
        return "done"

    #Updates the settings on the server
    elif fun == "update_settings":
        server.sendall(f"sync_settings {username}".encode("utf-16"))
        while 1:
            data = server.recv(1024)
            if data == b'ready':
                break
        pickled_settings = pickle.dumps(settings)

        server.sendall(pickled_settings)

    #Load the settings from the cloud
    elif fun == "load_settings":
        if connect():
            sync()
            loop()
        else:
            print("Can not acsess the internet, so using the newset database on this computer")
        con = sql.connect("Snake.sqlite3")
        cur = con.cursor()
        select_highscore  = f"SELECT highscore FROM Snake WHERE username = '{username}'"
        cur.execute(select_highscore)
        fetch_highscore = cur.fetchone()
        print(fetch_highscore[0], "test")
        print(get_highscore(), "get highscore")
        if get_highscore() < fetch_highscore[0]:
            update_account_highscore(fetch_highscore[0])
            print("updated highscore")
        load_account_settings(username)
    if connect():
        server.close()
