from setuptools import setup

setup(
    name='pyramid-medley',
    version='0.0.1',
    author='Dan Jacob',
    author_email='danjac354@gmail.com',
    packages=['pyramid_medley'],
    scripts=[],
    license='LICENSE.txt',
    description='Pyramid/Jinja2/SQLAlchemy scaffold',
    long_description=open('README.md').read(),
    install_requires=[
        'pyramid',
    ],
    entry_points="""
    [pyramid.scaffold]
    medley=pyramid_medley.scaffolds:MedleyTemplate
    """,
)
