from distutils.core import setup
setup(
    name = 'geomepydash',
    package_dir={'': 'C:\/Users/user/documents/githubsite'}, 
    packages = ['geomepydash'],
    version = '0.2.3',
    license='MIT',
    description = 'Simple python wrapper for Geometry Dash API and some GD Tools (Originally made by GD Colon)',   # Give a short description about your library
    author = 'vierofernando',
    author_email = 'vierofernando9@gmail.com',
    url = 'https://github.com/vierofernando/geomepydash',
    download_url = 'https://github.com/vierofernando/geomepydash/archive/0.2.3.tar.gz',
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
        'Programming Language :: Python :: 3.8'
    ],
)