import os
import pytest
from app.calculator_config import ConfigManager


def test_config_valid(monkeypatch):

    monkeypatch.setenv("HISTORY_FILE", "test.csv")
    monkeypatch.setenv("AUTO_SAVE", "true")

    config = ConfigManager()

    assert config.history_file == "test.csv"
    assert config.auto_save is True


def test_config_missing_history(monkeypatch):

    monkeypatch.delenv("HISTORY_FILE", raising=False)

    with pytest.raises(ValueError):
        ConfigManager()