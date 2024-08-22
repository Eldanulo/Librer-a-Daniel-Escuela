use sys;

drop database if exists Librería;

create database Librería;

use Librería;

create table Usuario(
	id_usuario int unsigned auto_increment,
	nom_usuario varchar(25) not null,
	apell_usuario varchar(25) not null,
	prov_usuario varchar(20) not null,
	pob_usuario varchar(20) not null,
	tel_usuario varchar(9) not null,
	nac_usuario date not null,
	
	constraint Usuario_id_usuario_pk primary key (id_usuario)
);

create table Autores(
	id_autor int unsigned auto_increment,
	nom_autor varchar(25) not null,
	apell_autor varchar(25),
	pais_autor varchar(25),
	
	constraint Autores_id_autor_pk primary key (id_autor)
);

create table Libros(
	id_libro int unsigned auto_increment,
	id_autor int unsigned,
	nom_libro varchar(50)not null,
	gen_libro varchar(20) not null,
	edit_libro varchar(25) not null,
	idiom_libro varchar(20) not null,
	coment_libro varchar(200),
	
	constraint Libros_id_libro_pk primary key (id_libro),
	constraint Libros_id_autor_fk foreign key (id_autor)
		references Autores (id_autor)
);

create table Prestamos(
	id_prestamo int unsigned auto_increment,
	id_libro int unsigned,
	id_usuario int unsigned,
	fec_prestamo date not null,
	fec_devolucion date not null,
	
	constraint Prestamos_id_prestamo_pk primary key (id_prestamo),
	constraint Prestamos_id_libro_fk foreign key (id_libro)
		references Libros(id_libro),
	constraint Prestamos_id_usuario_fk foreign key (id_usuario)
		references Usuario (id_usuario)
);


 
/*INSERT INTO Registros (id_producto, cantidad, tipo_pago, pagado, producto_entregado, cambio_entregado) VALUES
		 (1, 1, "Efectivo", 0, "Sí", "No"),
(2, 1, "Efectivo", 0, "No", "Sí"),
    (3, 1, "Tarjeta", 12.50, "Sí", "No"),
    (4, 3, "Efectivo", 45.00, "Sí", "Sí ($3.00)"),
    (5, 2, "Tarjeta", 18.00, "No", "No"),
    (6, 1, "Efectivo", 7.50, "Sí", "No"),
    (7, 4, "Transferencia", 41.00, "Sí", "No"),
    (8, 2, "Tarjeta", 11.98, "Sí", "No"),
    (9, 5, "Efectivo", 20.00, "Sí", "Sí ($0.80)"),
    (10, 1, "Efectivo", 3.99, "Sí", "No"),
    (11, 1, "Tarjeta", 11.50, "No", "No"),
    (12, 2, "Efectivo", 18.30, "Sí", "Sí ($1.70)"),
    (13, 1, "Transferencia", 6.80, "Sí", "No"),
    (14, 3, "Tarjeta", 21.00, "Sí", "No"),
    (15, 1, "Efectivo", 7.60, "Sí", "No"),
    (16, 2, "Efectivo", 10.40, "Sí", "Sí ($0.60)"),
    (17, 1, "Transferencia", 15.99, "No", "No"),
    (18, 2, "Efectivo", 10.40, "Sí", "No"),
    (19, 1, "Tarjeta", 4.70, "Sí", "No"),
    (20, 4, "Efectivo", 20.80, "Sí", "Sí ($1.20)"),
    (21, 1, "Transferencia", 13.75, "No", "No"),
    (22, 2, "Efectivo", 16.00, "Sí", "Sí ($0.50)");             
*/


INSERT INTO Autores (nom_autor, apell_autor, pais_autor) VALUES
    ("Marieta", "Zumbado", "Panamá"),
    ("Elvis", "Mora", "Panamá"),
    ("Laura", "Pérez", "México"),
    ("Tomás", "Gutiérrez", "Argentina"),
    ("Emily", "Thompson", "Estados Unidos"),
    ("Sofía", "Fernández", "España"),
    ("Ryo", "Nakamura", "Japón"),
    ("Beatriz", "Castillo", "Colombia"),
    ("Marco", "Rossi", "Italia"),
    ("Ana", "García", "Perú"),
    ("Jean", "Dupont", "Francia"),
    ("Maria", "Silva", "Brasil"),
    ("Dmitri", "Ivanov", "Rusia"),
    ("Julia", "Martínez", "Chile"),
    ("Carlos", "Ramírez", "Venezuela"),
    ("Isabella", "Costa", "Portugal"),
    ("Li", "Wei", "China"),
    ("Hans", "Müller", "Alemania"),
    ("Ingrid", "Johansson", "Suecia"),
    ("Amina", "Al-Farsi", "Marruecos"),
    ("William", "Davies", "Reino Unido"),
    ("Kofi", "Mensah", "Ghana");


select * from Autores;

INSERT INTO Libros (id_autor, nom_libro, gen_libro, edit_libro, idiom_libro, coment_libro) VALUES
    (1, "Español 8", "Escolar", "Santillana", "Español", "Buen libro"),
    (2, "Dominios de Español 8", "Escolar", "Eduvision Panamá", "Español", "pereza xd"),
    (1, "El Misterio de la Luna Roja", "Suspenso", "Editorial Planeta", "Español", "Una novela llena de intriga y sorpresas."),
    (2, "Caminos Cruzados", "Drama", "Alfaguara", "Español", "Personajes complejos con un trasfondo emocional."),
    (3, "The Lost Kingdom", "Fantasía", "Penguin Books", "Inglés", "Un viaje épico a un reino olvidado."),
    (4, "La Fortaleza Invisible", "Ciencia Ficción", "Nova", "Español", "Innovadora y llena de tecnología avanzada."),
    (5, "Under the Stars", "Romance", "HarperCollins", "Inglés", "Una historia de amor bajo el cielo estrellado."),
    (6, "El Vuelo de las Águilas", "Historia", "Anagrama", "Español", "Un fascinante relato histórico ambientado en la Edad Media."),
    (7, "El Último Suspiro", "Thriller", "Ediciones B", "Español", "Lleno de giros inesperados y suspenso."),
    (8, "La Isla de los Perdidos", "Aventura", "Salamandra", "Español", "Aventura en una isla llena de secretos."),
    (9, "Shadow in the Night", "Misterio", "Random House", "Inglés", "Misterioso y atrapante, con un final sorprendente."),
    (10, "El Silencio del Bosque", "Terror", "Tusquets Editores", "Español", "Terrorífica historia ambientada en un bosque oscuro."),
    (11, "El Arte de la Guerra Interior", "Filosofía", "Ediciones Paidós", "Español", "Reflexiones profundas sobre la batalla interna."),
    (12, "Beyond the Horizon", "Ciencia Ficción", "Simon & Schuster", "Inglés", "Futurista y emocionante."),
    (13, "La Casa de los Espejos", "Drama", "Siruela", "Español", "Drama familiar lleno de secretos."),
    (14, "The Wind and the Sea", "Aventuras", "Macmillan", "Inglés", "Una travesía en alta mar llena de emoción."),
    (15, "La Revolución Silenciosa", "Política", "Akal", "Español", "Un análisis incisivo de movimientos políticos."),
    (16, "Sombras de un Imperio", "Historia", "Debate", "Español", "Historia del auge y caída de un gran imperio."),
    (17, "El Jardín de los Poetas", "Poesía", "Visor Libros", "Español", "Poemas íntimos que conectan con la naturaleza."),
    (18, "Memories of Tomorrow", "Ciencia Ficción", "Del Rey", "Inglés", "Una novela futurista que desafía la percepción del tiempo."),
    (19, "El Guardián de los Sueños", "Fantasía", "Roca Editorial", "Español", "Fantasía mágica con personajes inolvidables."),
    (20, "A Light in the Darkness", "Biografía", "Bloomsbury", "Inglés", "Inspiradora biografía de un líder revolucionario.");

select * from Libros;

INSERT INTO Usuario (nom_usuario, apell_usuario, prov_usuario, pob_usuario, tel_usuario, nac_usuario) VALUES
    ("Daniel", "Lopez", "Panamá", "San Miguelito", "9999-9999", "01-01-01"),
    ("Laura", "García", "Madrid", "Madrid", "612345678", "1990-03-15"),
    ("Tomás", "Pérez", "Buenos Aires", "La Plata", "221654321", "1985-08-22"),
    ("Emily", "Johnson", "California", "Los Ángeles", "323987654", "1992-06-10"),
    ("Sofía", "Fernández", "Barcelona", "Sabadell", "669876543", "1988-11-03"),
    ("Ryo", "Nakamura", "Tokio", "Shibuya", "803456789", "1995-07-25"),
    ("Beatriz", "Castillo", "Antioquia", "Medellín", "302123456", "1991-01-18"),
    ("Marco", "Rossi", "Lombardía", "Milán", "393654789", "1980-09-30"),
    ("Ana", "García", "Lima", "Miraflores", "911234567", "1993-05-12"),
    ("Jean", "Dupont", "Île-de-France", "París", "014987653", "1987-02-28"),
    ("Maria", "Silva", "São Paulo", "Campinas", "551123456", "1994-12-07"),
    ("Dmitri", "Ivanov", "Moscú", "Moscú", "701234567", "1989-04-14"),
    ("Julia", "Martínez", "Santiago", "Providencia", "569876543", "1990-07-21"),
    ("Carlos", "Ramírez", "Zulia", "Maracaibo", "412345678", "1983-10-01"),
    ("Isabella", "Costa", "Lisboa", "Oeiras", "218765432", "1996-06-19"),
    ("Li", "Wei", "Pekín", "Chaoyang", "861234567", "1984-09-09"),
    ("Hans", "Müller", "Baviera", "Múnich", "491234567", "1991-12-05"),
    ("Ingrid", "Johansson", "Estocolmo", "Norrmalm", "461234567", "1986-11-23"),
    ("Amina", "Al-Farsi", "Casablanca", "Maarif", "212987654", "1992-08-31"),
    ("William", "Davies", "Londres", "Camden", "207654321", "1990-02-11"),
    ("Kofi", "Mensah", "Gran Accra", "Accra", "233987654", "1988-05-26");

	
select * from Usuario;

-- fecha(date) y-m-d

INSERT INTO Prestamos (id_libro, id_usuario, fec_prestamo, fec_devolucion) VALUES
    (1, 1, "2023-01-15", "2023-02-15"),
    (2, 2, "2023-01-20", "2023-02-20"),
    (3, 3, "2023-02-01", "2023-03-01"),
    (4, 4, "2023-02-05", "2023-03-05"),
    (5, 5, "2023-03-10", "2023-04-10"),
    (6, 6, "2023-03-15", "2023-04-15"),
    (7, 7, "2023-04-01", "2023-05-01"),
    (8, 8, "2023-04-10", "2023-05-10"),
    (9, 9, "2023-05-05", "2023-06-05"),
    (10, 10, "2023-05-15", "2023-06-15"),
    (11, 11, "2023-06-01", "2023-07-01"),
    (12, 12, "2023-06-10", "2023-07-10"),
    (13, 13, "2023-07-05", "2023-08-05"),
    (14, 14, "2023-07-15", "2023-08-15"),
    (15, 15, "2023-08-01", "2023-09-01"),
    (16, 16, "2023-08-10", "2023-09-10"),
    (17, 17, "2023-09-05", "2023-10-05"),
    (18, 18, "2023-09-15", "2023-10-15"),
    (19, 19, "2023-10-01", "2023-11-01"),
    (20, 20, "2023-10-10", "2023-11-10");

select * from Prestamos;



