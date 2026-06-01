Diagrams
========

This page demonstrates the three diagram tools wired into the build. It is an
example — delete it once you've confirmed diagrams render for your project.

Graphviz (``sphinx.ext.graphviz``)
----------------------------------

Rendered with the ``dot`` binary (installed in the dev container).

.. graphviz::

   digraph traceability {
      rankdir=LR;
      node [shape=box, style=rounded];
      "R_001" -> "S_001" -> "T_001";
   }

PlantUML (``sphinxcontrib.plantuml``)
-------------------------------------

Rendered with the ``plantuml`` binary + Java (installed in the dev container).

.. uml::

   @startuml
   actor Author
   Author -> "Sphinx-Needs" : writes requirement
   "Sphinx-Needs" -> "ubTrace" : exports traceability
   @enduml

Mermaid (``sphinxcontrib.mermaid``)
-----------------------------------

Rendered client-side in the browser — no build-time binary required.

.. mermaid::

   flowchart LR
       R[Requirement] --> S[Specification] --> T[Test]
