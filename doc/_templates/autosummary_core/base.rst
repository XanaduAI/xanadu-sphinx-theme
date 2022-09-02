{% if referencefile %}
.. include:: {{ referencefile }}
{% endif %}

{{ objname }}
={% for i in range(objname|length) %}={% endfor %}{{ underline }}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}
