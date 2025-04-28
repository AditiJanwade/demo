# demo

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
