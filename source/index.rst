Sphinx-Needs Starter
====================

Welcome to the Sphinx-Needs starter template. This page is a minimal, working
example: it defines one requirement and lists it in a table. Replace it with
your own content as you build out your documentation.

Example requirement
-------------------

.. req:: Example requirement
   :id: R_001
   :status: open

   Replace this with your own requirements. Drop your ``.rst`` files into
   ``source/`` and wire them into the toctree below.

Needs overview
--------------

The table below is generated automatically from every need in the project.

.. needtable::
   :columns: id;title;status
   :style: table

Contents
--------

.. Add your documentation pages to the toctree below — one document name per
   line, without the ``.rst`` extension. For example, if you add
   ``source/requirements.rst`` and ``source/design.rst``::

       .. toctree::
          :maxdepth: 2

          requirements
          design

.. toctree::
   :maxdepth: 2
