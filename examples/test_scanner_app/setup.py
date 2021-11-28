from setuptools import setup

setup(
    app=["app.py"],
    data_files=[],
    options=dict(py2app=dict(
        plist="Info.plist",
    )),
    setup_requires=["py2app"],
)