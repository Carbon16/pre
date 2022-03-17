import json #line:5
from datetime import date #line:6
from pickle import FALSE #line:7
from re import I #line:8
import os #line:9
member ={}#line:12
spons ={}#line:13
newMem =True #line:14
fName =0 #line:15
count =1 #line:16
c0 =1 #line:17
Valid =False #line:18
Valid0 =False #line:19
sName =0 #line:20
vol =0 #line:21
loc =0 #line:22
paid =False #line:23
nUse =False #line:24
today =date .today ()#line:25
d1 =today .strftime ("%d/%m")#line:26
y1 =int (today .strftime ("%y"))#line:27
y2 =y1 +1 #line:28
get =True #line:29
go =True #line:30
k =[]#line:31
v =[]#line:32
def add (OOO0OO0OOOOOOOOOO ):#line:34
    O0OO000OO00OO0OOO =True #line:35
    while O0OO000OO00OO0OOO ==True :#line:36
        member ["A"+str (OOO0OO0OOOOOOOOOO )]={}#line:37
        OO000O0OOO0O0O000 =False #line:39
        OO0OO0O000OO0O000 =False #line:40
        O0OOOOO0O0O0OOO0O =False #line:41
        OO0OO0OO00OO000O0 =input ("Please enter your first name:")#line:43
        OOO00OOOO000O00OO =input ("Please enter your surname:")#line:44
        while len (str (OO0OO0OO00OO000O0 ))==0 or len (str (OOO00OOOO000O00OO ))==0 :#line:46
            print ("Please enter your name.")#line:47
            OO0OO0OO00OO000O0 =input ("Please enter your first name:")#line:48
            OOO00OOOO000O00OO =input ("Please enter your surname:")#line:49
        member [OOO0OO0OOOOOOOOOO ]["Prename"]=OO0OO0OO00OO000O0 #line:51
        member [OOO0OO0OOOOOOOOOO ]["Surname"]=OOO00OOOO000O00OO #line:52
        member [OOO0OO0OOOOOOOOOO ]["Date"]=d1 #line:53
        member [OOO0OO0OOOOOOOOOO ]["Expiry"]=y2 #line:54
        O00O00O00OO000OOO =input ("Do you wish to volunteer? (y/n):")#line:56
        if O00O00O00OO000OOO =="y":#line:58
            while OO000O0OOO0O0O000 ==False :#line:59
                OOOO0OOOOO0000O00 =int (input ("Where do you want to volunteer? \n1. Shop\n2. Gate\n3. Painting & Decorating\nSelect:"))#line:60
                if OOOO0OOOOO0000O00 ==1 :#line:61
                    member [OOO0OO0OOOOOOOOOO ]["Volunteer"]=True #line:62
                    member [OOO0OO0OOOOOOOOOO ]["Location"]="Shop"#line:63
                    OO000O0OOO0O0O000 =True #line:64
                if OOOO0OOOOO0000O00 ==2 :#line:65
                    member [OOO0OO0OOOOOOOOOO ]["Volunteer"]=True #line:66
                    member [OOO0OO0OOOOOOOOOO ]["Location"]="Gate"#line:67
                    OO000O0OOO0O0O000 =True #line:68
                if OOOO0OOOOO0000O00 ==3 :#line:69
                    member [OOO0OO0OOOOOOOOOO ]["Volunteer"]=True #line:70
                    member [OOO0OO0OOOOOOOOOO ]["Location"]="Painting & Decorating"#line:71
                    OO000O0OOO0O0O000 =True #line:72
        while OO0OO0O000OO0O000 ==False :#line:75
            OOO0OOO00O00OO0O0 =input ("Has user paid the fee? (y/n):")#line:76
            if OOO0OOO00O00OO0O0 =="y":#line:77
                member [OOO0OO0OOOOOOOOOO ]["Paid"]=True #line:78
                OO0OO0O000OO0O000 =True #line:79
            if OOO0OOO00O00OO0O0 =="n":#line:80
                member [OOO0OO0OOOOOOOOOO ]["Paid"]=False #line:81
                OO0OO0O000OO0O000 =True #line:82
        while O0OOOOO0O0O0OOO0O ==False :#line:84
            OO0OO00O00O00O000 =input ("Add new member? (y/n):")#line:85
            if OO0OO00O00O00O000 =="y":#line:86
                O0OO000OO00OO0OOO =True #line:87
                O0OOOOO0O0O0OOO0O =True #line:88
                OOO0OO0OOOOOOOOOO =OOO0OO0OOOOOOOOOO +1 #line:89
                return OOO0OO0OOOOOOOOOO #line:90
            if OO0OO00O00O00O000 =="n":#line:92
                O0OO000OO00OO0OOO =False #line:93
                OOO0OO0OOOOOOOOOO =OOO0OO0OOOOOOOOOO +1 #line:94
                O0OOOOO0O0O0OOO0O =True #line:95
                print ("Goodbye")#line:96
                return OOO0OO0OOOOOOOOOO #line:97
            else :#line:98
                print ("Please enter only y or n")#line:99
    return member #line:100
def get (O00OOOOO0OOO000OO ):#line:102
    O0O0OO0OO0OOOO00O =True #line:104
    OOO0OO0O00O00OOOO =False #line:105
    O0OO00OO0O00OOO0O =False #line:106
    O0OO0O0O000O0OOO0 =False #line:107
    while O0O0OO0OO0OOOO00O ==True :#line:109
        while OOO0OO0O00O00OOOO ==False :#line:110
                OO0O00OO00OO00O0O =int (input ("What do you want to search? \n1. Voulenteers\n2. Expired\n3. Not paid\nSelect:"))#line:111
                if OO0O00OO00OO00O0O ==1 :#line:112
                    O0000OO00000OO00O =int (input ("What do you want to search? \n1. Gate\n2. Shop\n3. Painting\n4. All\nSelect:"))#line:113
                    if O0000OO00000OO00O ==1 :#line:114
                        for OO0O000OO00OOO000 in O00OOOOO0OOO000OO :#line:115
                            try :#line:116
                                if O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Location"]=="Gate":#line:117
                                    print ("Name: "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Surname"])+", "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Prename"]))#line:118
                            except KeyError :#line:119
                                print ("**End**")#line:120
                    if O0000OO00000OO00O ==2 :#line:121
                        try :#line:122
                            for OO0O000OO00OOO000 in O00OOOOO0OOO000OO :#line:123
                                if O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Location"]=="Shop":#line:124
                                    print ("Name: "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Surname"])+", "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Prename"]))#line:125
                        except KeyError :#line:126
                                print ("**End**")#line:127
                    if O0000OO00000OO00O ==3 :#line:128
                        try :#line:129
                            for OO0O000OO00OOO000 in O00OOOOO0OOO000OO :#line:130
                                if O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Location"]=="Painting & Decorating":#line:131
                                    print ("Name: "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Surname"])+", "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Prename"]))#line:132
                        except KeyError :#line:133
                                print ("**End**")#line:134
                    if O0000OO00000OO00O ==4 :#line:135
                        try :#line:136
                            for OO0O000OO00OOO000 in O00OOOOO0OOO000OO :#line:137
                                if O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Volunteer"]==True :#line:138
                                    print ("Name: "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Surname"])+", "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Prename"]))#line:139
                        except KeyError :#line:140
                            print ("**End**")#line:141
                if OO0O00OO00OO00O0O ==2 :#line:143
                    try :#line:144
                        for OO0O000OO00OOO000 in O00OOOOO0OOO000OO :#line:145
                                if O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Date"]>d1 and O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Expiry"]>y1 :#line:146
                                    print ("Name: "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Surname"])+", "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Prename"]))#line:147
                    except KeyError :#line:148
                        print ("**End**")#line:149
                if OO0O00OO00OO00O0O ==3 :#line:150
                    try :#line:151
                        for OO0O000OO00OOO000 in O00OOOOO0OOO000OO :#line:152
                            if O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Paid"]==False :#line:153
                                print ("Name: "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Surname"])+", "+str (O00OOOOO0OOO000OO [OO0O000OO00OOO000 ]["Prename"]))#line:154
                    except KeyError :#line:155
                        print ("**End**")#line:156
def spon (O000OO0OOO00O000O ):#line:158
    OO00OOO000000O000 =True #line:160
    O0000000O0O0OO0O0 =False #line:161
    global c0 #line:162
    while OO00OOO000000O000 ==True :#line:164
        while O0000000O0O0OO0O0 ==False :#line:165
            print ("PLEASE BE AWARE THAT THIS SPONSORSHIP WILL COST $200")#line:166
            OO0OO000OO0OO0000 =input ("Please enter your name:")#line:167
            O00O00000O0OO00OO =input ("Please enter the message you would like:")#line:168
            print ("PLEASE CONFIRM THE FOLLOWING DETAILS ARE CORRECT")#line:169
            print ("Name:"+OO0OO000OO0OO0000 +" | Message:"+O00O00000O0OO00OO )#line:170
            OOOO0OO0OO0O00O0O =str (input ("Please confirm (y/n):"))#line:171
            if OOOO0OO0OO0O00O0O =="y":#line:172
                O000OO0OOO00O000O .update ({c0 :[str (OO0OO000OO0OO0000 ),str (O00O00000O0OO00OO )]})#line:173
                print ("Sponsorship sucess!")#line:174
                OO00OOO000000O000 =False #line:175
                O0000000O0O0OO0O0 =True #line:176
                c0 =c0 +1 #line:177
            if OOOO0OO0OO0O00O0O =="n":#line:178
                print ("Please try again")#line:179
                O0000000O0O0OO0O0 =False #line:180
    return O000OO0OOO00O000O #line:181
while go ==True :#line:184
    menu =int (input ('1. Add new member\n2. Get a member\n3. Sponsor\n4. Display sponsors\n5. EXIT\nSELECT: '))#line:185
    if menu ==1 :#line:186
        add (count )#line:187
    if menu ==2 :#line:188
        get (member )#line:189
    if menu ==3 :#line:190
        spon (spons )#line:191
    if menu ==4 :#line:192
        print (spons )#line:193
    if menu ==5 :#line:194
        go =False #line:195
        print ("Goodbye!")