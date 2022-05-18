import time
import main_menu
import socket
import sqlite3 as sql
from types import NoneType
import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

if connect():
    print(socket.gethostbyname(socket.gethostname()))

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 8081

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.connect((HOST,PORT))
    # server.sendall(b"Hello world")
    run = True
    with open("Snake.sqlite3","wb") as f:
        while run:
            f_reading = server.recv(4096)
            # print(f_reading)
            if not f_reading:
                # print("not reading")
                break

            f.write(f_reading)

    #server.shutdown(socket.SHUT_WR)
else:
    print("Cant connect to the server with out an internet connection")



def check_username(username,password):
    con = sql.connect("Snake.sqlite3")
    cur = con.cursor()

    get_username = f"SELECT username, password FROM Snake WHERE username = '{username}' and password = '{password}'"
    cur.execute(get_username)
    fetch = cur.fetchone()
    print(fetch)
    if type(fetch) != NoneType:
        con.close()
        return True
    else:
        con.close()
        return False



def create_user():

    con = sql.connect("Snake.sqlite3")
    cur = con.cursor()

    username = input("input a username ")
    public_username = input("input a public username ")
    password = input("input a password ")
    highscore = input("input a highscore ")
    while 1:
        
        get_username = f"SELECT username FROM Snake WHERE username = '{username}';"
        cur.execute(get_username)
        fetch = cur.fetchall()
        print(type(fetch))
        print(fetch)
        if type(fetch) != NoneType:
            print("user name taken")
            username = input("input a differnt username ")
        else:
            print("username not taken")
            add_new_user = f"INSERT INTO Snake VALUES ('{username}','{password}','{public_username}','{highscore}')"
            cur.execute(add_new_user)
            con.commit()
            con.close()
            break

account_yes_no = input("Do you have an account? ")

if account_yes_no.lower() == "no":

        if input("Would you like to make an account ").lower() == "yes":
            if connect(): create_user()
            else: print("Can not make an account with no internect connection")

        else: print("Ok you can make an account and anytime to get acces to your progress anywhere and acces the leaderboarsd")

    

elif account_yes_no.lower() == "yes":
    if_password = check_username(input("Enter your username? "),input("Enter your password? "))
    while not if_password:
        if_password = check_username(input("Enter your username? "),input("Enter your password? "))
        print("testing")
    print("username and password correct welcome")
    # print("Ok you can make an account and anytime to get acces to your progress anywhere and acces the leaderboarsd")



server.sendall(b'update_highscore png')
print("sent")
server.close()

# main_menu.run_game()