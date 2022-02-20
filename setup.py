#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2019/12/15
"""
语音处理工具箱。
生成whl格式安装包：python setup.py bdist_wheel

直接上传pypi：python setup.py sdist upload

用twine上传pypi：
生成安装包：python setup.py bdist_wheel
上传安装包：twine upload dist/ahocorasick-0.1.0-py3-none-any.whl

注意：需要在home目录下建立.pypirc配置文件，文件内容格式：
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username: admin
password: admin
"""

from setuptools import setup, find_packages

setup(
    name="ackit",
    version='0.1.0',
    author="kuangdd",
    author_email="kuangdd@foxmail.com",
    description="simple and pure python package and like pyahocorasick.",
    long_description="ackit(aho-corasick kit) is a simple and pure python package and its method like pyahocorasick.",
    long_description_content_type="text/markdown",
    url="https://github.com/KuangDD/aho-corasick",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],  # 指定项目最低限度需要运行的依赖项
    python_requires='>=3.5',  # python的依赖关系
    package_data={
        '': ['*.md'],
    },  # 包数据，通常是与软件包实现密切相关的数据
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],
)

if __name__ == "__main__":
    print(__file__)
