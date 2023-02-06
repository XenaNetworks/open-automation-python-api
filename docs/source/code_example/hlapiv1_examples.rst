High-Level API (V1)
===================================

The boilerplate code that is used to run the examples in this section:

.. literalinclude:: boilerplate.py
    :language: python
    

Create Tester
--------------------------------

To connect to a tester, create a tester object and the driver will automatically handle the connection. Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

Available tester types are :doc:`L23Tester <../api_ref/hlapiv1/_autosummary/testers/classes/xoa_driver.internals.hli_v1.testers.l23_tester.L23Tester>` , :doc:`L23VeTester <../api_ref/hlapiv1/_autosummary/testers/classes/xoa_driver.internals.hli_v1.testers.l23ve_tester.L23VeTester>`, :doc:`L47Tester <../api_ref/hlapiv1/_autosummary/testers/classes/xoa_driver.internals.hli_v1.testers.l47_tester.L47Tester>`, :doc:`L47VeTester <../api_ref/hlapiv1/_autosummary/testers/classes/xoa_driver.internals.hli_v1.testers.l47ve_tester.L47VeTester>`.

.. literalinclude:: hlapiv1/01_create_tester_from_type.py
    :language: python
    :caption: Create tester instance
    :emphasize-lines: 6-7


Create Tester Using Python Context Manager
-----------------------------------------------------------

You can also create a tester instance using Python Context Manager

.. seealso::

    Read more about `Python Context Manager <https://docs.python.org/3/library/contextlib.html>`_


.. literalinclude:: hlapiv1/02_create_tester_context.py
    :language: python
    :caption: Create tester instance using Python Context Manager
    :emphasize-lines: 6-7


Create Multiple Testers
-----------------------------------------

To create multiple tester instances, you can do:

.. literalinclude:: hlapiv1/03_create_multi_testers.py
    :caption: Create multiple tester instances
    :language: python
    :emphasize-lines: 9-24

.. seealso::
    
    `Learn more about await asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#asyncio.gather>`_.


Access Module
--------------------------------

The examples below help you gain access to a test module on a tester.

.. literalinclude:: hlapiv1/04_obtain_one_module.py
    :caption: Access a single module on a tester
    :language: python
    :emphasize-lines: 10-11


Access Multiple Modules
--------------------------------

The examples below help you gain access to several test modules on a tester.

.. literalinclude:: hlapiv1/05_obtain_multiple_modules.py
    :caption: Access multiple modules on a tester
    :language: python
    :emphasize-lines: 10-11


Access All Modules
--------------------------------

The examples below help you gain access to several test modules on a tester.

.. literalinclude:: hlapiv1/06_obtain_all_modules.py
    :caption: Access all modules on a tester
    :language: python
    :emphasize-lines: 10-15
    

Access Port
--------------------------------

The examples below help you gain access to a test port on a module.

.. literalinclude:: hlapiv1/07_obtain_one_port.py
    :caption: Access a single port on a module
    :language: python
    :emphasize-lines: 15-16
    

Access Multiple Ports
--------------------------------

The examples below help you gain access to several test ports on a module.

The interface of obtaining multiple ports is equivalent to obtaining multiple modules with the following exceptions:

* all ports are of the same type
* all ports are aligned from index ``0`` to ``max_port_count-1``

.. literalinclude:: hlapiv1/08_obtain_multiple_ports.py
    :caption: Access multiple ports on a module
    :language: python
    :emphasize-lines: 11-12


Obtain All Ports
--------------------------------

The examples below help you gain access to all test ports on a module.

.. literalinclude:: hlapiv1/09_obtain_all_ports.py
    :caption: Access all ports on a module
    :language: python
    :emphasize-lines: 11-16


Read Module and Port Config
-------------------------------------

.. note::

    Resource reservation is not required to query information from the tester.

.. literalinclude:: hlapiv1/10_query_parameters.py
    :caption: Query module and port
    :language: python
    :emphasize-lines: 15-16, 20-24


Write Module and Port Config
---------------------------------------

.. note::
    
    Reservation is required to do ``set`` to: :doc:`Testers <../api_ref/hlapiv1/testers>`, :doc:`Modules <../api_ref/hlapiv1/modules>`, and :doc:`Ports <../api_ref/hlapiv1/ports>`.

.. literalinclude:: hlapiv1/11_setting_parameters.py
    :caption: Configure module and port
    :language: python
    :emphasize-lines: 16-26, 28-52


Configure Stream
--------------------------------

To generate L23 stateless traffic, stream configuration is necessary. The example below shows how to create/delete streams on a L23 port.

.. note::
    
    Reservation is required to do :terms: `CRUD`` operations streams on :doc:`Ports <../api_ref/hlapiv1/ports>`.

.. literalinclude:: hlapiv1/12_streams.py
    :caption: Configure streams on a port
    :language: python
    :emphasize-lines: 34-61


Modifiers
--------------------------------

To simulate traffic from many address, or when you want certain fields of a packet to change dynamically on a per packet basis, you can use modifiers. A modifier changes the field value per packet based on how you configure it. The example below shows how to create/delete modifiers on a stream.

.. note::
    
    Port reservation is required to create modifiers on streams.

.. note::
    
    The mechanism of creating and deleting modifiers is different from streams. In order to change the modifiers on a stream packet header, you need to re-configure all the modifiers again. An abstraction will be added to the HL Python API to provide users with the same API syntax, i.e. ``create()``. ``delete()``, and ``remove()`` in a future release of XOA Python API.

.. note::
    
    An easy way to configure the packet header content will be added to the HL Python API in a future release.


.. literalinclude:: hlapiv1/13_modifiers.py
    :caption: Create and delete modifiers on a stream
    :language: python
    :emphasize-lines: 61-92


Control Traffic & Read Statistics
------------------------------------------

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., should be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

To show how to query statistics on-the-fly, the function ``my_awesome_func`` is slightly modified.

.. literalinclude:: hlapiv1/14_traffic_stats.py
    :caption: Traffic and statistics
    :language: python
    :emphasize-lines: 17-45, 95-105, 107-108, 113-114, 116-119


Use Chimera to Impair Certain Traffic Latency/Jitter
-----------------------------------------------------

.. note::

    Only applicable to a Chimera module. This is not meant to generate any traffic.


.. literalinclude:: hlapiv1/15_traffic_impairment.py
    :caption: Traffic drop and latency/jitter impairment
    :language: python
    :emphasize-lines: 108-166
    

Read & Write Transceiver Config
--------------------------------------------

The example demonstrates how to read/write transceiver register of different types in different ways, as well as reading transceiver temperature.

.. literalinclude:: hlapiv1/16_transceiver_reg.py
    :caption: Read/write transceiver values
    :language: python
    :emphasize-lines: 35-37, 39-40, 43-44, 46-48, 50-51, 53-55, 57-58