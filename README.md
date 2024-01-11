##Proyecto Hamburgueseria

El proyecto tratara sobre una hamburgueseria que ofrece pedidos mediante una web. 
En la misma podemos encontrar las consignas necesitadas para el proyecto en:

                - Modelos: Los modelos que se crearan son 6:
                                                              - Hamburguesas (el usuario en el proyecto puede agregar hamburguesas pero no debería ya que seria una DB de productos disponibles.
                                                              - Bebidas (idem hamburguesas)
                                                              - Combos
                                                              - Pedido
                                                              - Reseña de la comida
                                                              - Sugerencias 
                - Formularios: Cada modelo menos 'Combos' tienen la posibilidad de agregar elementos en la DB.
                  Los mismos tienen las siguientes funcionalidades:
                                                                    - Hamburguesas: Para agregar hamburguesas a la DB.
                                                                    - Bebidas: idem
                                                                    - Pedido: Realizar el pedido de la hamburguesa que se almacenara en la DB. 
                                                                    - Reseña: La reseña esta enfocada en intentar obtener un feedback del cliente y tener en cuenta la post-venta.
                                                                              Tiene una vista donde podemos apreciar las diferentes valoraciones o reseñas de los clientes que se actualizara cada vez que agreguen datos.
                                                                                No está limitada la cantidad de valoraciones que apareceran en la view, pero de seguir con este proyecto se tendrá en cuenta.
                                                                              
                                                                    - Sugerencias: Dentro del Footer y dentro de algunos urls el cliente puede acceder y dejar una sugerencia a la empresa.
                                                                                  Tambien tendra una vista para ver las diferentes sugerencias 
                                                                    
                - Busqueda de datos: En algunos urls tendremos la opcion para buscar datos.
                  Los mismos se encuentran en:

                                                  - Tanto en /hamburguesas como en /bebidas que se pueden acceder desde la barra de navegación.
                                                  - en /buscarSugerencia -----> No tiene boton dentro de la web. Está pensado para que administradores de la web puedan buscar entre las sugerencias alojadas en la DB.

                - Herencia HTML:
                                  La misma está presente en mayor o menor medida en varios templates en la web para que pueda encontrarlo facilmente lo mismos son:
                                   
                                    - #clase padre    ---> hereda a
                                    -base_light.html   ---> pedido_realizado.html  //  valoraciones.html  //  agregar_bebida.html  // agregar_burger.html  // sugerencias.html  
                                    -pedidos.html ---> realizar_sugerencia.html  //
                                    -busqueda.html ---> busqueda_burger.html  //  busqueda_bebida.html   //  busqueda_bebida_resultado.html  //  busqueda_hamburguesa_resultado.html  //  busqueda_sugerencia.html  //  resultados_sugerencias.html
                                    -prod.html ---> bebidas.html  //  combos.html  //   hamburguesas.html  // 



Espero que le guste y que el readme le sea de utilidad, desde ya. Muchas gracias!
                                    

                                            
