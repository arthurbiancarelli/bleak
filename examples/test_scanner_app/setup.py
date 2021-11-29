from setuptools import setup

setup(
    app=["app.py"],
    data_files=[],
    options=dict(py2app=dict(
        plist="Info.plist",
        arch="x86_64"
    )),
    setup_requires=["py2app"],
)