//crear bd

CREATE TABLESPACE GESTION
LOGGING
DATAFILE 'C:\app\ye_yo\product\18.0.0\oradata\GESTION.dbf'
SIZE 40M REUSE
AUTOEXTEND ON NEXT 640 K MAXSIZE 100M;


//crear usuario
create user GESTION identified by GESTION	
       DEFAULT TABLESPACE GESTION
       TEMPORARY TABLESPACE TEMP;
GRANT DBA TO GESTION WITH ADMIN OPTION;

alter session set "_ORACLE_SCRIPT"=true;


//crear tabla

create table USUARIOS
(
  NOMBRE_USUARIO     NUMBER(15) not null,
  CONTRASEÑA		 VARCHAR2(50) not null,
  TIPO_USUARIO       VARCHAR2(1) not null,
  NOMBRE             VARCHAR2(20) not null,
  APELLIDO           VARCHAR2(20),
  TELEFONO           VARCHAR2(20) not null,
  CORREO_ELECTRONICO VARCHAR2(40) not null
)
;
alter table USUARIOS
  add constraint PKUSUARIOS primary key (NOMBRE_USUARIO);

