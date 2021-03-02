import time,sys

  
# define the countdown func. 

      

    
uwnk=input(" သိချင်တာသေချာလား:  ")

aussu =input ("တကယ်လား:  ")

print ("\033[1;33;40m\nဟုတ်ပြီလေ ခဏစောင့် : \n")
def countdown(t):
    time.sleep(4)
countdown(1)
print("\033[1;32;40m This letter is for you and from my heart.  \n")
def countdown(t):
    time.sleep(6)
countdown(1)
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]","[■■■□□□□□□□]","[■■■■□□□□□□]","[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]",
("""\033[1;36;40m
	
	ရပြီ။
	"""),
("""
\033[1;31;40m
IIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIII
        IIIII """),("""
        IIIII
        IIIII
        IIIII"""),("""
        IIIII
        IIIII
        IIIII"""),("""
        IIIII
        IIIII
        IIIII
        IIIII"""),("""
        IIIII
IIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIII


        """),("""
\033[1;35;40m
LLLLL
LLLLL
LLLLL"""),("""
LLLLL
LLLLL
LLLLL"""),("""
LLLLL
LLLLL
LLLLL"""),("""
LLLLL
LLLLL
LLLLL"""),("""
LLLLL
LLLLL
LLLLL"""),("""
LLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL
"""),
        (""" \033[1;34;40m
       OOOOOOO
     OOOOOOOOOOO
   OOOOO     OOOOO"""),("""
  OOOOO       OOOOO
 OOOOO         OOOOO
OOOOO           OOOOO"""),("""
OOOOO           OOOOO
OOOOO           OOOOO
OOOOO           OOOOO"""),("""
OOOOO           OOOOO
OOOOO           OOOOO
OOOOO           OOOOO"""),("""
 OOOOO         OOOOO
  OOOOO       OOOOO
   OOOOO     OOOOO"""),("""
     OOOOOOOOOOO
       OOOOOOO
       """)
           	, ("""\033[1;36;40m
VVVV           VVVV
 VVVV         VVVV
  VVVV       VVVV"""),("""
   VVVV     VVVV
    VVVV   VVVV
     VVVV VVVV"""),("""
      VVVVVVV
       VVVVV
        VVV"""),("""
         V
       """),("""\033[1;31;40m
EEEEEEEEEEEEEEEEEEEE
EEEEEEEEEEEEEEEEEEEE"""),("""
EEEE
EEEE
EEEE"""),("""
EEEE
EEEEEEEEEEEEEEEEEEEE
EEEEEEEEEEEEEEEEEEEE"""),("""
EEEE
EEEE"""),("""
EEEE
EEEE
EEEE"""),("""
EEEEEEEEEEEEEEEEEEEE
EEEEEEEEEEEEEEEEEEEE


"""),("""\033[1;34;40m
YYYY            YYYY
 YYYY          YYYY
  YYYY        YYYY"""),("""
   YYYY      YYYY
    YYYY    YYYY
     YYYY  YYYY"""),("""
      YYYYYYYY
       YYYYYY"""),("""
        YYYY
        YYYY"""),("""
        YYYY"""),("""
        YYYY
        YYYY"""),("""
        YYYY
        YYYY"""),("""
        YYYY
        """),("""    \033[1;32;40m    
       OOOOOOO
     OOOOOOOOOOO
   OOOOO     OOOOO"""),("""
  OOOOO       OOOOO
 OOOOO         OOOOO
OOOOO           OOOOO"""),("""
OOOOO           OOOOO
OOOOO           OOOOO
OOOOO           OOOOO"""),("""
OOOOO           OOOOO
OOOOO           OOOOO
OOOOO           OOOOO"""),("""
 OOOOO         OOOOO
  OOOOO       OOOOO
   OOOOO     OOOOO"""),("""
     OOOOOOOOOOO
       OOOOOOO
       """),("""\033[1;36;40m
UUUUU           UUUUU
UUUUU           UUUUU
UUUUU           UUUUU"""),("""
UUUUU           UUUUU
UUUUU           UUUUU
UUUUU           UUUUU"""),("""
UUUUU           UUUUU
UUUUU           UUUUU
UUUUU           UUUUU"""),("""
UUUUU           UUUUU
UUUUU           UUUUU
UUUUU           UUUUU"""),("""
 UUUUU         UUUUU
  UUUUU       UUUUU
   UUUUU     UUUUU"""),("""
     UUUUUUUUUUU
       UUUUUUU

 """) ]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


  