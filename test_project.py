"""
Names: Alexander Bonifacio, Kunal Antala
Emails: abonifac1@stevens.edu, kantala@stevens.edu
Date: 5/6/2026
Description: Contains two Pytest test cases that verify Portfolio.total_value() and
Stock.gain_loss() produce correct results given known inputs.
"""

import pytest
from stock import Stock
from portfolio import Portfolio

def test_total_value():
    """Verifies that total_value() returns the correct sum across all holdings."""
    p = Portfolio("Test")
    s1 = Stock("NVDA", 8, 800.0)
    s1.set_current_price(900.0)
    p.add_stock(s1)
    assert p.total_value() == 7200.0 # 8 shares at $900 should be $7200

def test_gain_loss():
    """Verifies that gain_loss() correctly calculates profit based on current vs purchase price."""
    s = Stock("AMD", 10, 120.0)
    s.set_current_price(175.0)
    assert s.gain_loss() == 550.0 # 10 shares gained $55 each, so total should be $550