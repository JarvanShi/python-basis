import os

libs = ['pyinstaller', 'jieba', 'wordcloud', 'sympy', 'wheel',
        'requests', 'beautifulsoup4','pyspider', 'python-goose',
        'numpy', 'pandas','matplotlib', 'seaborn', 'mayavi', 'scipy', 'pillow',
        'sklearn', 'tensorflow', 'mxnet',
        'django', 'pyramid', 'flask', 'networkx',
        'pygame', 'cocos2d', 'panda3d',
        'werobot', 'aip',
        'nltk', 'pypdf2', 'python-docx', 'docopt',
        'pyqt5', 'wxpython', 'pygobject', 'pyopengl', 'myqr',
        'vrzero', 'pyovr', 'vizard',
        'quads', 'ascii_art']
try:
    for lib in libs:
        os.system('pip install' + lib)
    print('Successfully Installed')
except:
    print('Failed')