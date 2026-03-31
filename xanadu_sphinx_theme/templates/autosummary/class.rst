{{ fullname }}
{{ underline }}

.. autoclass:: {{ fullname }}
   :show-inheritance:

   {% if '__init__' in methods %}
     {% set caught_result = methods.remove('__init__') %}
   {% endif %}

   {% block attributes_documentation %}
   {% if attributes %}

   .. raw:: html

      <a class="attr-details-header collapse-header" data-bs-toggle="collapse" href="#attrDetails" aria-expanded="false" aria-controls="attrDetails">
         <h2>Attributes</h2>
         <i class="bx bx-chevron-down rotate"></i>
      </a>
      <div class="collapse" id="attrDetails">

   {% block attributes_summary %}
   {% if attributes %}

   .. autosummary::
      :nosignatures:
   {% for item in attributes %}
      ~{{ name }}.{{ item }}
   {%- endfor %}

   {% endif %}
   {% endblock %}

   {% for item in attributes %}
   .. autoattribute:: {{ item }}
   {%- endfor %}

   .. raw:: html

      </div>

   {% endif %}
   {% endblock %}

   {% block methods_documentation %}
   {% if methods %}

   .. raw:: html

      <a class="meth-details-header collapse-header" data-bs-toggle="collapse" href="#methDetails" aria-expanded="false" aria-controls="methDetails">
         <h2>Methods</h2>
         <i class="bx bx-chevron-down rotate"></i>
      </a>
      <div class="collapse" id="methDetails">

   {% block methods_summary %}
   {% if methods %}

   .. autosummary::
   {% for item in methods %}
      ~{{ name }}.{{ item }}
   {%- endfor %}

   {% endif %}
   {% endblock %}

   {% for item in methods %}
   .. automethod:: {{ item }}
   {%- endfor %}

   .. raw:: html

      </div>

   {% endif %}
   {% endblock %}

   .. raw:: html

      <script type="text/javascript">
         document.querySelectorAll(".collapse-header").forEach((header) => {
             header.addEventListener("click", () => {
                 const icon = header.querySelector("i.rotate");
                 if (icon !== null) {
                     icon.classList.toggle("up");
                 }
             });
         });
      </script>
