INSERT INTO cafeteria.personas (per_run, per_nombre, per_app, per_apm, per_tel, per_email, per_fnac) VALUE (666666666, 'Rodrigo', 'Aguirre', 'Pizarro','876322456', 'rodrigo.aguirre@gmail.com', '1995-05-12' );

/*INSERT CLIENTE CON RUT*/
INSERT INTO cafeteria.clientes (cli_puntos, cli_descto, cli_frecuente, per_run) VALUE (4, 0, 0, FALSE, 666666666);
/*INSERT CLIENTE SIN RUT*/
INSERT INTO cafeteria.clientes (cli_puntos, cli_descto, cli_frecuente) VALUE (4, 0, 0, FALSE);


INSERT INTO cafeteria.perfiles (perf_nom, perf_desc) VALUE (3, 'Garzón', 'Mesero');


INSERT INTO cafeteria.trabajadores ( tra_inicio_turno,tra_termino_turno, tra_fcontr, per_run, perf_cod) VALUE ('2022-10-03 08:00:00', '2022-10-08 18:00:00',2022-09-30, 333333333, 3);

/* INSERT USUARIOS CON TRABAJADOR */
INSERT INTO cafeteria.usuarios (usu_nom, usu_pass,tra_cod) VALUE (5, 'dani.rocco', '123456',2);

/* INSERT USUARIOS CON CLIENTE*/
INSERT INTO cafeteria.usuarios (usu_nom, usu_pass, cli_cod) VALUE (5, 'dani.rocco', '123456',2);

INSERT INTO cafeteria.productos ( pro_nombre, pro_descripcion, pro_stock, pro_precio) VALUE (9, 'Café Latte', 'Poca Leche y Mucha Espuma',10, 1990);

/*INSERT VENTAS CON CLIENTE*/
INSERT INTO cafeteria.ventas (ven_descrip,ven_fecha,ven_subtotal,cli_cod) VALUE (1, 'Cappuchino + Trozo Torta', '2022-11-23', 4980,4);

/* INSERT VENTAS CON USUARIO */
INSERT INTO cafeteria.ventas (ven_descrip,ven_fecha,ven_subtotal, usu_cod) VALUE (2, 'Latte + Donuts', '2022-11-27', 3990,5);

INSERT INTO cafeteria.boletas (bol_iva, bol_total, ven_cod) VALUE (1, 95.6, 5926, 1);

INSERT INTO cafeteria.comandas (com_cant,com_hora,pro_cod,ven_cod) VALUE (1, 1, '2022-11-23 09:00:00', 2,1);



SELECT * FROM cafeteria.personas;

SELECT * FROM cafeteria.clientes;

SELECT * FROM cafeteria.perfiles;

SELECT * FROM cafeteria.trabajadores;

SELECT * FROM cafeteria.usuarios;

SELECT * FROM cafeteria.productos;

SELECT * FROM cafeteria.comandas;

SELECT * FROM cafeteria.ventas;

SELECT * FROM cafeteria.boletas;