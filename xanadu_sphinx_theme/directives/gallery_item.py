"""
This module implements the ``gallery-item`` reST directive.

Derived from https://github.com/pytorch/tutorials/blob/master/custom_directives.py
which carries the following license:

BSD 3-Clause License

Copyright (c) 2017, Pytorch contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from pathlib import Path
import os
from inspect import cleandoc
from shutil import copyfile

from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from docutils import nodes
from sphinx_gallery.gen_rst import scale_image


TEMPLATE = cleandoc(
    """
    .. raw:: html

        <div class="gallery-item-thumbcontainer" data-category="{tags}" tooltip="{tooltip}">

    .. only:: html

        .. figure:: {thumbnail}

            {description}

    .. raw:: html

        </div>
    """
)


class GalleryItemDirective(Directive):
    """Creates a sphinx-gallery-style thumbnail.

    Note that the ``description``option can be a link to a document. Also,
    thumbnails will be created out of figures and stored in ``/_static/thumbs``.
    Therefore, consider ``/_static/thumbs`` as a "built" directory.

    **Example**

    .. gallery-item::
        :tooltip: This tutorial is directed at people who are new to NLP.
        :figure: /_static/img/thumbnails/babel.jpg
        :description: :doc:`/beginner/deep_learning_nlp_tutorial`
    """

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "description": directives.unchanged_required,
        "figure": directives.unchanged_required,
        "tags": directives.unchanged,
        "tooltip": directives.unchanged,
    }

    has_content = False
    add_index = False

    def run(self):
        path_to_root = Path(".").resolve()
        path_to_thumbs = path_to_root / "_static/thumbs"
        path_to_figure = path_to_root / self.options["figure"]
        path_to_thumbnail = path_to_thumbs / path_to_figure.name

        os.makedirs(str(path_to_thumbs), exist_ok=True)

        if path_to_figure.suffix == ".svg":
            copyfile(str(path_to_figure), str(path_to_thumbnail))
        else:
            scale_image(str(path_to_figure), str(path_to_thumbnail), 400, 280)

        thumbnail = "/" + str(path_to_thumbnail.relative_to(path_to_root))

        thumbnail_rst = TEMPLATE.format(
            description=self.options["description"],
            tags=self.options.get("tags", ""),
            thumbnail=thumbnail,
            tooltip=self.options.get("tooltip", "")[:195],
        )
        thumbnail = StringList(thumbnail_rst.split("\n"))
        thumb = nodes.paragraph()
        self.state.nested_parse(thumbnail, self.content_offset, thumb)
        return [thumb]