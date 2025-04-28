# demo
https://chatgpt.com/share/68100578-a848-8007-83a3-23da11b54779
## EXP-1

download orcal virtual box 

ubantu, downloade-lts file  , iso file download

new- name (ubuntu) - type (linux)- version  (64bit ubuntu)  

settings - storage - controller ide (choose iso file )

start -install ubuntu- name ,password - restart 


## EXP-2 Google app engine

install python 2.7 version

install google app engine 
https://www.npackd.org/p/com.google.AppEnginePythonSDK/1.9.62
( App engine sdk for python 1.9 62)

Edit - **preference** - choose python path -path of app engine 

create new folder on desktop 

file - create new application - application name (helloworld) -parent(select  new folder created on desktop) -runtime (python 2.7) - port 

select project and run button 

open browser - type   localhost:port(8080)


## EXP-5 virtual network

ubuntu and kali put them in same subnet so that they communicate 

file -host network manager -  create -  

dhcp server - enable server - server address(192.168.100.2) - upper address (192.168.100.254) -apply

adapter - configure adapter automatically -apply -close 

ubuntu 

setting-network 

make sure adapter 1 disable 

adapter 2 -enable  -select host only 

varify 

#ip addr show

#ping (host address of kali ) -c 5 ## to see whether kali and ubuntu communicate

 

## EXP-8

install winscp
https://winscp.net/eng/download.php

start ubuntu

terminal 

#sudo apt install  openssh-server

#ifconfig (note inet number ,like 172.16.7.231 )

open winscp

hostname( inet ) -username (given hai ) -password

net 2 virtual machine are open , just file copy and paste to another machine

## EXP 6:KVM

sudo apt update   # update the system

sudo apt upgrade  # upgrade 

egrep -c ‘(vmx|svm)’   /proc/cpuinfo         #check kvm compatibility in system 

##if the output is greater than zero then kevm can be install

## verify if the kvm virtualization is enable by the running the following command 

kvm-ok  # if not found

sudo apt install cpu-checker

check again 

kvm-ok  #output  is kVm acceleration can be used

##Install KVM

sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y

#enable virtaual demon service

sudo  systemctl enable —now libvirtd

sudo systemctl start libvirtd

sudo systemctl status libvertd

sudo username -aG kvm $USER

sudo username -aG libvirt $USER

search virtual machine manager






## EXP 3:Hadoop

# Step 1: Install Java
Check if Java is already installed by running:
java -version

If Java is not installed, install it using the following command (for Ubuntu):
sudo apt update
sudo apt install openjdk-8-jdk

Set Java environment variables:
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc
echo "export PATH=$JAVA_HOME/bin:$PATH" >> ~/.bashrc
source ~/.bashrc

# Step 2: Install Hadoop
Download Hadoop:
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz

Extract Hadoop:
tar -xvzf hadoop-3.3.0.tar.gz
sudo mv hadoop-3.3.0 /opt/hadoop

Set Hadoop environment variables: Add the following lines to your ~/.bashrc:
export HADOOP_HOME=/opt/hadoop
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_HOME=$HADOOP_HOME

Source the .bashrc file to apply the changes:
source ~/.bashrc
Step 3: Configure Hadoop

Navigate to the Hadoop configuration directory:
cd $HADOOP_HOME/etc/hadoop

# Edit the following files:
core-site.xml:
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>

hdfs-site.xml:
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>

mapred-site.xml:
cp mapred-site.xml.template mapred-site.xml

Edit mapred-site.xml and add the following:
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>

yarn-site.xml:
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>

# Step 4: Format HDFS
hdfs namenode -format

# Step 5: Start Hadoop Daemons
start-dfs.sh
start-yarn.sh
jps

# Step 6: Run WordCount Application
echo "hello hadoop hello world" > input.txt

hdfs dfs -mkdir /user/hadoop/input
hdfs dfs -put input.txt /user/hadoop/input

hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.0.jar wordcount /user/hadoop/input /user/hadoop/output

hdfs dfs -cat /user/hadoop/output/part-r-00000

# Step 7: Stop Hadoop

stop-yarn.sh
stop-dfs.sh








