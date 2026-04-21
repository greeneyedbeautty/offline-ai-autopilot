"""
🤖 Offline AI Autopilot CLI
A powerful, privacy-first AI assistant for developers
"""

__version__ = "0.1.0"
__author__ = "Autopilot Contributors"
__description__ = "Offline AI-Assisted Autopilot CLI - No internet required"
__license__ = "MIT"

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from .main import app

__all__ = ["app", "logger"]