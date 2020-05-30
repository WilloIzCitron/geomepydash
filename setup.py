from distutils.core import setup
setup(
    name = 'gd-api',
    packages = ['gd-api'],
    version = '0.1',
    license='MIT',
    description = 'Simple python wrapper for Geometry Dash API and some GD Tools (Originally made by GD Colon)',   # Give a short description about your library
    author = 'vierofernando',
    author_email = 'vierofernando9@gmail.com',
    url = 'https://github.com/vierofernando/gd-api',
    download_url = 'https://github.com/vierofernando/gd-api/archive/0.1.tar.gz',
    keywords = ['API', 'WRAPPER', 'GAMES', 'GD'],
    install_requires=[
        'urllib3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)