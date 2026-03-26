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
         <h2 style="font-size: 24px;">
            <i class="fas fa-angle-down rotate" style="float: right;"></i> Attributes
         </h2>
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
         <h2 style="font-size: 24px;">
            <i class="fas fa-angle-down rotate" style="float: right;"></i> Methods
         </h2>
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
                 const icon = header.querySelector("h2 i");
                 if (icon !== null) {
                     icon.classList.toggle("up");
                 }
             });
         });
      </script>
