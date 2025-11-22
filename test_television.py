import pytest
from television import Television


class TestTelevision:
    """Test suite for the Television class."""
    
    def test_init(self):
        """Test that a new Television initializes with correct default values."""
        tv = Television()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
    def test_power(self):
        """Test that power() toggles the television on and off."""
        tv = Television()
        tv.power()
        assert "Power = True" in str(tv)
        tv.power()
        assert "Power = False" in str(tv)
    
    def test_mute(self):
        """Test that mute() toggles mute status when TV is on."""
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        assert "Volume = 0" in str(tv)
        tv.mute()
        assert "Volume = 1" in str(tv)
    
    def test_channel_up(self):
        """Test that channel_up() increases the channel when TV is on."""
        tv = Television()
        tv.power()
        tv.channel_up()
        assert "Channel = 1" in str(tv)
    
    def test_channel_down(self):
        """Test that channel_down() decreases the channel when TV is on."""
        tv = Television()
        tv.power()
        tv.channel_up()
        tv.channel_down()
        assert "Channel = 0" in str(tv)
    
    def test_volume_up(self):
        """Test that volume_up() increases the volume when TV is on."""
        tv = Television()
        tv.power()
        tv.volume_up()
        assert "Volume = 1" in str(tv)
    
    def test_volume_down(self):
        """Test that volume_down() decreases the volume when TV is on."""
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_down()
        assert "Volume = 0" in str(tv)
