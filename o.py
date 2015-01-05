#!/usr/bin/python
import os,sys,subprocess,datetime,re,time
from time import strftime

def wirte_file(ST,pc,pt,pr,ET):
    
    w_file = open("ping_log.txt",'a')
    w_file.write(ST+'\n')
    w_file.write(pc)
    w_file.write(pt)
    w_file.write(pr)
    w_file.write(ET)
    w_file.close()

def get_des(host):
 
    ph1 = subprocess.Popen(['ping', '-c 1', '-w 1', host], stdout=subprocess.PIPE).communicate()[0]
    tph1 = list(list(str(ph1.split()[2]).split("("))[1].split(")"))[0]
    return tph1

def ping_time(host,nu):
    fm1 = 0.0
    count = 0
    count_loss = 0
    i = int(nu)
    min = strftime('%M')
    sec = strftime('%S')
    new_sec = int(sec)
    new_min = int(min) + i
#    print new_min, new_sec
#    print strftime('%S')
    #while int(strftime('%M')) != new_min and int(strftime('%S')) != new_sec :
    while i > 0 :
    #      print "time start with : ", i
          j = 2
          while j > 0 :
                fs = subprocess.Popen(['ping', '-c 1', '-w 1', host], stdout=subprocess.PIPE).communicate()[0]
                if re.search('100%',fs) :
                   count_loss += 1
                   j -= 1
                else:
                   fm = float(str(fs.split()[13]).split("=")[1])
                   fm1 += fm
                   count += 1
                   time.sleep(1)
                   j -= 1
          i -=1
    fp = fm1 / count
    return round(fp,2), count, count_loss

def chkhost(host):

    result = subprocess.call(["ping","-c","1","-W","1",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if result == 0:
        return True
    elif result == 1:
        raise Exception 

def chktime(time):
    
    if int(time) > 0 and int(time)<=60 : 
        return True 
    elif int(time) > 60 or int(time) <= 0 :
#        raise Exception
        raise ValueError

#    try:
#        if int(time) > 0 and int(time)<=60 :
#           return time
#    except Exception:
#        print "please don't over a hour or less a minute"
#        raise ValueError
#        raise Exception


#def 
   #check url and ip address result
   #host = subprocess.Popen(['host', target], stdout = subprocess.PIPE).communicate()[0]

   #print host 



if __name__ == '__main__':
   dstp = raw_input("Enter a host to ping: ")
   nu = raw_input("How many time: ")
   pur = get_des(dstp)
   ping_result = ('NA','NA','NA')

   try:
       chktime(nu)
       chkhost(dstp)
#   except Exception:
   except ValueError:
        print "please don't over a hour or less a minute"
        raise 
   except Exception:
       print "Host not found"


#   try:
#       chkhost(dstp)
#       Start_time = "Start time :"+strftime('%Y-%m-%d %H:%M:%S')
#       print Start_time
#       ping_result = ping_time(pur,nu)
#   except Exception:
#       Start_time = "Start time :"+strftime('%Y-%m-%d %H:%M:%S')
#       print Start_time
#       print "Host not found"
#       raise Exception


#   ping_result = ping_time(pur,nu)
#   print "The ping result from :",pur,"Average time is :",ping_result[0],"ms"

   Start_time = "Start time :"+strftime('%Y-%m-%d %H:%M:%S')
   print Start_time
   ping_result = ping_time(pur,nu)
   ping_caption = "The ping result"+'\n'
   ping_time = "From :"+pur+" Average time is :"+str(ping_result[0])+" ms"+'\n'
#   print "Packet Success :",ping_result[1],"Packet loss :",ping_result[2]
   ping_result = "Packet Success :"+str(ping_result[1])+" Packet loss :"+str(ping_result[2])+'\n'
   End_of_time = "End of time :"+strftime('%Y-%m-%d %H:%M:%S')+'\n\n'
   print ping_caption+ping_time+ping_result+End_of_time
  

   wirte_file(Start_time,ping_caption,ping_time,ping_result,End_of_time) 





