import json
import socket
import sqlite3 as sql
import pickle
from types import NoneType
import urllib.request
from fun import update_account_highscore
from settings import load_account_settings, write_logged
import time

def main(fun, username, password=None, public_username=None, highscore=None, settings=None):
    print(highscore, "in main")
    def loop():
        while 1:
            data = server.recv(1024)

            if data != None and data != b'':
                print(data)
                data_decoded = data.decode()
                print(data_decoded)
                data_split = data_decoded.split(" ")
                print(data_split)
                command = data_split[0]
                print(command)
                
                
                if command == "sync":
                    with open("Snake.sqlite3","wb") as f:
                        while 1:
                            f_reading = server.recv(4096)
                            # print(f_reading)
                            if not f_reading:
                                print("not reading")
                                if fun == "create_user":
                                    return "good", "good"
                                break
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
        server.send(b"sync")

    def update_highscore(username, highscore):
        print(highscore,"in highscore")
        server.send(f"update_highscore {username} {highscore}".encode("utf-8"))
        loop()

    def login_user(username, password):
        if connect():
            sync()
            loop()
        else:
            print("Can not acsess the internet, so using the newset database on this computer")
        con = sql.connect("Snake.sqlite3")
        cur = con.cursor()

        get_username = f"SELECT username, password FROM Snake WHERE username = '{username}' and password = '{password}'"
        cur.execute(get_username)
        fetch = cur.fetchone()
        print(fetch)
        if type(fetch) != NoneType:
            get_highscore  = f"SELECT highscore FROM Snake WHERE username = '{username}'"
            cur.execute(get_highscore)
            fetch_highscore = cur.fetchone()
            print(fetch_highscore[0], "test")
            update_account_highscore(fetch_highscore[0])
            load_account_settings(username)
            write_logged(True)
            return True
        else:
            con.close()
            return False




    def create_user(username, public_username, password):

        # con = sql.connect("Snake.sqlite3")
        # cur = con.cursor()

        for i in range(1):
            # online database code
            # print(f"create_user {username} {public_username} {password} {0}")
            server.sendall(f"create_user {username} {public_username} {password} {0}".encode("utf-8"))#in the furture replcace the zero with the local highscore
            loop_test = loop()
            print(loop_test)
            return loop_test


            
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

    elif fun == "create_user":
        print("create_user")
        print(username, public_username)
        return create_user(username, public_username, password)

    elif fun == "sync":
        print(highscore, "in sync")
        update_highscore(username, highscore)
        sync()
        loop()
        print(f"{settings}")
        server.send(f"sync_settings {username}".encode("utf-8"))
        pickled_settings = pickle.dumps(settings)
        #print(pickled_settings)
        server.send(pickled_settings)
        


    if connect():
        server.close()



if __name__ == "__main__":
    main()
