#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年2月27日 下午2:07
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : 远程控制.py
# @Software: PyCharm

import paramiko

# 通过密码
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('114.67.11.22', 22, 'root', '123qwe')
stdin, stdout, stderr = ssh.exec_command('ifconfig')
print(stdout.read())
ssh.close()

# 通过密钥
# private_key_path = '/home/lipeijing/.ssh/id_rsa'
# key = paramiko.RSAKey.from_private_key(private_key_path)
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('114.67.11.22', 22, 'root', key)
# stdin, stdout, stderr = ssh.exec_command('ifconfig')
# print(stdout.read())
# ssh.close()

# 文件传输
import os, sys

t = paramiko.Transport(('114.67.11.22', 22))
t.connect(username='root', password='123qwe')
sftp = paramiko.SFTPClient.from_transport(t)
# 远端的文件/helloworld.txt, 拷贝到本地的/tmp/test.txt
sftp.get('/tmp/helloworld.txt', '/tmp/test.txt')
t.close()

pravie_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test3.py','/tmp/test3.py')

t.close()

# 通过密钥的形式
import paramiko

pravie_key_path = '/home/auto/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test3.py','/tmp/test4.py')

t.close()
