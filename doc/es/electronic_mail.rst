#:after:electronic_mail/electronic_mail:section:electronic_email#

=======
Eventos
=======

En las plantillas de correo dispondremos de un nuevo campo donde podemos escribir
una expresión Python para que anote en los eventos del tercero (historial) los
correos que se le van enviando.

.. tip:: Este módulo añade una pestaña historial a la ficha de terceros en la 
         que añade los correos que se le han enviado.

Configuración
=============

En el campo **Tercero** de la plantilla del correo electrónico, escriba la
expresión Mako para encontrar el identificador del tercero. Por ejemplo:

.. code:: python

    ${record.party.id}
