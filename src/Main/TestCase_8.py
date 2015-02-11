'''
Created on Feb 9, 2015

@author: Dipesh
'''
import urllib2
import telnetlib
import time
import paramiko

# Check if you can start presentation and then stop it

HOST1 = "192.168.202.114"
USER1 = "admin"
PASSWORD1 = "1234"

HOST2 = "192.168.202.68"
USER2 = "admin"
PASSWORD2 = ""

# HOST2 = "192.168.202.57"
# USER2 = "admin"
# PASSWORD2 = "1234"

result = "Fail"
client2 = paramiko.SSHClient()

class TestCase_8:

    def internet_on(self):
      
        client2 = paramiko.SSHClient()
        self.connects(client2, HOST2, USER2, PASSWORD2)

        try:
            remote_conn2 = client2.invoke_shell()
           
            remote_conn2.send('xcommand Presentation Start PresentationSource: 1 \n')
            time.sleep(10)
            output = remote_conn2.recv(5000)
   
            if "OK" not in output:
                self.result= "Fail"
   
            remote_conn2.send('xcommand Presentation Stop \n')
            time.sleep(2)
            output = remote_conn2.recv(5000)
   
            if "OK" not in output:
                self.result= "Fail"
   
            client2.close()            
            return self.result;

        except paramiko.AuthenticationException:
            return "Fail"
    

    def connects(self, client, host, username, password):
        try:
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy())
            client.connect(host, username=username, password= password)      
            self.result = "Pass"              
        except paramiko.AuthenticationException:
            self.result= "Fail"