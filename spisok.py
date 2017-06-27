#!/usr/bin/python
#!/opt/zimbra/bin
import re
import subprocess
import time
import datetime


start = time.time()
with open('myfile.txt', 'a') as foo:
    print('\nScript started at {0} .\n'.format(datetime.datetime.now()))
    foo.write('\nScript started at {0} .\n'.format(datetime.datetime.now()))

#Bash command that displays list of emails in zimbra
list_splitted = subprocess.check_output('zmprov -l gaa', shell=True).splitlines()

#print(list_splitted)

#print(type(list_splitted))

#l = 7

#Loop that parse email and delete blocks with ID's that contains @fmrest.com
for email in list_splitted:
    #adds logging to a file
    with open('myfile.txt', 'a') as f:
        #for id in ids:
        f.write('mail to parse {0} \n'.format(email))
    #skips a 'galsync' user
    if email.find('galsync') != -1:
        print('galsync')
        continue

    print(email)
    #l -= 1

    #get list of ID blocks for exact email
    it = subprocess.check_output('zmmailbox -z -m {0} gact'.format(email), shell=True)
    #print(type(it))

    #splits list to a lines
    it = it.split('\n\n')
    #print(it)
    # Magic that parses blocks with ID's and returns neded ID's
    ids = [m.groups()[0] for m in [re.search("^Id: (\d+).+email: (.+fmrest.com)$", x, re.M + re.DOTALL) for x in it] if m]
    print('print id ' + str(ids))
    #print(type(ids))
    for id_to_del in ids:
        print('id to delete {0} \n'.format(id_to_del))

        print(subprocess.check_output('zmmailbox -z -m {0} getContacts {1}'.format(email, id_to_del), shell=True))

        with open('myfile.txt', 'a') as file:
            file.write(subprocess.check_output('zmmailbox -z -m {0} getContacts {1} \n'.format(email, id_to_del), shell=True))
        try:
            #Bash command that delete ID of concrete email
            subprocess.check_output('zmmailbox -z -m {0} deleteContact {1}'.format(email, id_to_del), shell=True)
        except subprocess.CalledProcessError as e:
            with open('myfile.txt', 'a') as foo:
                foo.write('\n {0} \n'.format(e))


    # if l == 0:
    #     break
# time.sleep(10)

# Here we have timer
end = time.time()
elapsed = round((end-start)/60, 2)

with open('myfile.txt', 'a') as foo:
    print('\nTime spend on script work {0} minutes. \n'.format(elapsed))
    foo.write('\nTime spend on script work {0} minutes. \n'.format(elapsed))
    print('\nScript stopped at {0} .\n'.format(datetime.datetime.now()))
    foo.write('\nScript stopped at {0} .\n'.format(datetime.datetime.now()))

