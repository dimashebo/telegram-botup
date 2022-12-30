from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    name='telegram-botup',
    version='0.11.0',
    author='Dima Shebotinov',
    author_email='groovestreetmagic@gmail.com',
    description='Telegram bot API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['botup'],
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=[
        'aiohttp'
    ],
    extras_require={
        'redis': ['aioredis']
    },
    project_urls={
        'Source Code': 'https://github.com/spirtum/telegram-botup'
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)
