



playerList = ["Rohit","Virat","Shubamn","Ayyar","KLRahul"];
print(playerList);

playerFind = input("enter the player name form list : ");




for player in playerList:
    if(player == playerFind):
        print(playerFind ," is present ");
        #break;
        pass;
    else:
        print("%s is not present "%playerFind);

