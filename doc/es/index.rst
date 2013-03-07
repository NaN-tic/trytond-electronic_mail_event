=============================
Eventos de correo electrónico
=============================

Este módulo añade en las plantillas un nuevo campo donde podemos escribir una
expresión Python para que anote en los eventos del tercero (historial) los
correos que se le van enviando.

.. tip:: Este módulo añade una pestaña historial a la ficha de terceros en la 
         que añade los correos que se le han enviado.

Configuración
=============

En el campo **Tercero** de la plantilla del correo electrónico, escriba la
expresión Mako para encontrar el identificador del tercero. Por ejemplo:

.. code:: python
    ${record.party.id}

Módulos que dependen
====================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /electronic_mail/index
   /electronic_mail_template/index

Dependencias
------------

* `Correo electrónico`_
* `Plantilla de correo electrónico`_

.. _Correo electrónico: ../electronic_mail/index.html
.. _Plantilla de correo electrónico: ../electronic_mail_template/index.html
