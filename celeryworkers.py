__author__ = 'Rene'

import boto.ec2
import aws_keys
import os
import time
from fabric.tasks import execute
from fabric.api import *
import matplotlib.pyplot as plt

print boto.ec2.regions()

conn = boto.ec2.connect_to_region("us-east-1",
                                  aws_access_key_id=aws_keys.aws_access_key_id,
                                  aws_secret_access_key=aws_keys.aws_secret_access_key)


reservations = conn.run_instances(
        'ami-64566e0c', min_count=2, max_count=2,
        key_name='rene',
        instance_type='m3.medium',
        security_groups=['launch-wizard-1'])

time.sleep(10)

for instance in reservations.instances:
    while instance.state != "running":
        time.sleep(5)
        instance.update()
        print instance.state
    print instance.state
    print "running"


# print "waiting..."
# time.sleep(40)

con=conn.get_all_instance_status()
for i,ins in enumerate(con):
    while str(con[i].system_status) != "Status:ok":
        time.sleep(5)
        con=conn.get_all_instance_status()
        print "Waiting"
    print "Iniciadas"

def execute_task():
    put(local_path="C:\Users\Rene\Desktop\mazon\conf\conf.yaml", remote_path="EvoPar2015/code/conf/conf.yaml")
    put(local_path="C:\Users\Rene\Desktop\deap\deap\one_diversidad.py", remote_path="EvoPar2015/code/one_diversidad.py")
    put(local_path="C:\Users\Rene\Desktop\deap\deap\one_all_cloud_n3.py", remote_path="EvoPar2015/code/one_all_cloud_n3.py")
    #sudo('mkdir EvoPar2015/code/data')
    #run("celery -A one_rastrigin worker --loglevel=info")
    put(local_path='celeryd', remote_path="/etc/default/celeryd",  use_sudo=True, mode=0640)
    sudo("chown root /etc/default/celeryd")
    sudo("service celeryd start")

def get_files(host):
     env.hosts=[host]
     env.user = 'ubuntu'
     env.key_filename = 'rene.cer'
     get(remote_path="EvoPar2015/code/data", local_path="C:\Users\Rene\Desktop\experientos\data"+ins.id)
     path="C:\Users\Rene\Desktop\experientos\data"+ins.id+"\data"

     # for filename in os.listdir(path):
     #    w12_file = open("%s/%s" % (path,filename))
     #    w12_records = [line.split(",") for line in w12_file if len(line.split(",")) == 3]
     #    y=tuple(x[1] for x in w12_records)
     #    x=range(0,len(w12_records))
     #    plt.plot(x,y)
     #    plt.ylabel('Tiempo Segundos')
     #    plt.xlabel('Experimento')
     #    plt.show()
     print "Ok"

def execute_celery():
    host=str(reservations.instances[0].public_dns_name)
    env.hosts=[host]
    env.user = 'ubuntu'
    env.key_filename = 'rene.cer'
    sudo('chown root EvoPar2015/code/conf')
    sudo('chown root EvoPar2015/code/data')
    sudo('python EvoPar2015/code/one_all_cloud_n3.py')
    #get_files(host)

def tomar():
    host=str(reservations.instances[0].public_dns_name)
    env.hosts=[host]
    env.user = 'ubuntu'
    env.key_filename = 'rene.cer'
    get_files(host)

for i, ins in enumerate(reservations.instances):
    host=str(ins.public_dns_name)
    env.hosts=[host]
    env.user = 'ubuntu'
    env.password='masterkey2010'
    env.key_filename = 'rene.cer'
    execute(execute_task)
    print str(ins.public_dns_name) + 'Ok'

raw_input("Press enter to continue")

for i in range(100):
    execute(execute_celery)
    time.sleep(1)
    if i == 1:
        raw_input("Finished")
    else:
        pass

# execute(execute_celery)
#
# raw_input("Otra vez")
#
# execute(execute_celery)