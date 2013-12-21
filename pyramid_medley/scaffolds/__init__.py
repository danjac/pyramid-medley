import os
import shutil

from pyramid.scaffolds import PyramidTemplate


class MedleyTemplate(PyramidTemplate):
    _template_dir = 'medley'
    summary = 'Pyramid/Jinja2/SQLAlchemy and more.'

    def post(self, command, output_dir, vars):
        # is there an easier way to deal with hidden files?
        self.makedirs(os.path.join(output_dir,
                                   vars['package'],
                                   'alembic', 'versions'))
        shutil.move(os.path.join(output_dir, "hgignore"),
                    os.path.join(output_dir, ".hgignore"))
        shutil.move(os.path.join(output_dir, "gitignore"),
                    os.path.join(output_dir, ".gitignore"))
        print("Let's get this party started, yo.")
