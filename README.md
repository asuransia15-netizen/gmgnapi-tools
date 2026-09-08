# gmgnapi-tools

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![Solana](https://img.shields.io/badge/solana-1.18%2B-orange)](https://solana.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Extended tools for [GmGnAPI](https://gmgn.ai) — Solana memecoin trading automation, sniper, and smart money analytics.**

> ⚡ Real-time WebSocket streaming · Smart money wallet tracking · Auto-snipe new pairs · PnL analytics

## Features

- **WebSocket Streaming** — Real-time trade data, new pair detection, and whale alerts
- **Smart Money Tracker** — Follow profitable wallets, copy-trade their entries
- **Auto Sniper** — Snipe new pairs with configurable slippage, gas, and take-profit
- **PnL Dashboard** — Track your wallet performance across multiple protocols
- **Multi-DEX Support** — Raydium, Orca, Jupiter, Meteora

## Quick Start

```bash
pip install git+https://github.com/asuransia15-netizen/gmgnapi-tools.git
```

```python
from gmgnapi_tools import GmGnSniper, SmartMoneyTracker

# Track smart money wallets
tracker = SmartMoneyTracker()
whales = tracker.get_top_traders(token="SOL", limit=10)

# Auto-snipe new pairs
sniper = GmGnSniper(
    min_liquidity=10_000,      # $10k minimum
    max_slippage=15,            # 15%
    take_profit=2.0,            # 2x
    stop_loss=0.7               # -30%
)
sniper.start()
```

## CLI

```bash
# Snipe new tokens
gmgn-sniper --token SOL --min-liquidity 10000 --slippage 15

# Track wallet PnL
gmgn-sniper track --wallet YOUR_WALLET_ADDRESS
```

## Dependencies

- `gmgnapi>=0.1.0` — Core GmGn API client
- `solana>=0.30.0` — Solana blockchain interaction
- `solders>=0.18.0` — Rust-powered Solana serialization
- `websocket-client>=1.6.0` — Real-time data streaming

## Documentation

Full documentation at [gmgnapi-tools.readthedocs.io](https://gmgnapi-tools.readthedocs.io)

## Disclaimer

This is an unofficial third-party tool. Not affiliated with GmGn. Use at your own risk. Trading memecoins is high-risk — never trade more than you can afford to lose.

## License

MIT © gmgnapi-dev