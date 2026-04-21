"""
Offline AI Autopilot CLI

Author: greeneyedbeautty
Version: 0.2.0
License: MIT
Description: A command-line interface for the Offline AI Autopilot.
"""

import logging

# Setup logging
def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

setup_logging()

# Exports
__all__ = ['setup_logging']