create database Wordle;
use Wordle;

create table Usuarios(
	Id	int primary key auto_increment,
    Nombre varchar(50),
    Username varchar(50),
    Email varchar(100),
    Contraseña varchar(50)
);