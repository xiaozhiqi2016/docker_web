#采用python3 + tornado + sqlchemy
#前端使用bootstap和一些js插件
#需要安装sqlalchemy,docker-py,pycurl,pymysql,tornado


＃数据库可以手动建，也可以用sqlalchemy创建,model下有个db.py可以用
user表：
create database if not exists shipman default character set utf8 collate utf8_general_ci;

use shipman;

create table if not exists user (id int(11) not null unsigned auto_increment primary key,\
                                 name varchar(32),\
                                 password varchar(64),\
                                 user_group varchar(32));



node表：
create table if not exists node (id int(11) unsigned not null auto_increment primary key,\
                                 name varchar(32),\
                                 node_ip varchar(32),
                                 port varchar(32),\
                                 cpus varchar(32),\
                                 mem varchar(32),\
                                 images varchar(32),\
                                 state enum('0','1'),\
                                 node_group varchar(32),\
                                 containers varchar(32),\
                                 os_version varchar(32),\
                                 kernel_version varchar(32),\
                                 docker_version varchar(32));




con_usage表：
create table if not exists con_usage (id int(11) unsigned not null auto_increment primary key,\
                                      con_id varchar(64),\
                                      con_addr varchar(32),\
                                      node_ip varchar(32),\
                                      username varchar(32),\
                                      con_app varchar(32),\
                                      con_desc varchar(256));


ip表：


