# gmgnapi-tools

Extended tools for GmGnAPI — Solana memecoin trading automation, sniper, and smart money analytics

## Features

- ✅ GmGnSniper — auto-buy trending Solana tokens
- ✅ SmartMoneyTracker — follow top trader wallets
- ✅ Token analytics with real-time price data
- ✅ Built on top of official GmGnAPI

## Installation

### PyPI
```bash
pip install git+https://github.com/gmgnapi-dev/gmgnapi-tools.git
```

## Quick Start

```python
from gmgnapi_tools import *

# Initialize client
client = Client()

# Get trending tokens
trending = client.get_trending()
print(trending)
```

## Documentation

Full documentation coming soon.

## License

MIT
