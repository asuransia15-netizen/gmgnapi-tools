#!/usr/bin/env python3
"""gmgn-sniper CLI — command-line interface for GmGnAPI Tools"""

import argparse
import sys
from gmgnapi_tools import GmGnSniper, SmartMoneyTracker

def main():
    parser = argparse.ArgumentParser(description="GmGnAPI Tools — Solana Memecoin Sniper")
    parser.add_argument("--api-key", help="GmGnAPI key")
    parser.add_argument("--trending", help="Get trending tokens (timeframe: 1h, 6h, 24h)", default="1h")
    parser.add_argument("--token", help="Get token info by contract address")
    parser.add_argument("--wallet", help="Get wallet info/PnL")
    parser.add_argument("--top-traders", help="Get top traders for a token")
    parser.add_argument("--pnl", help="Get wallet PnL")

    args = parser.parse_args()

    if args.token:
        sniper = GmGnSniper(api_key=args.api_key)
        result = sniper.get_token_info(args.token)
        print(result)
    elif args.wallet:
        sniper = GmGnSniper(api_key=args.api_key)
        result = sniper.get_wallet_info(args.wallet)
        print(result)
    elif args.top_traders:
        tracker = SmartMoneyTracker(api_key=args.api_key)
        result = tracker.get_top_traders(args.top_traders)
        print(result)
    elif args.pnl:
        tracker = SmartMoneyTracker(api_key=args.api_key)
        result = tracker.get_wallet_pnl(args.pnl)
        print(result)
    else:
        sniper = GmGnSniper(api_key=args.api_key)
        result = sniper.get_trending(args.trending)
        print(result)

if __name__ == "__main__":
    main()