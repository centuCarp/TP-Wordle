create database Wordle;
use Wordle;

create table Usuarios(
	Id	int primary key auto_increment,
    Username varchar(50),
    Email varchar(100),
    Contraseña varchar(50)
);

select * from Usuarios;