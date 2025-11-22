class Television:
    """A class representing a television with basic controls.
    
    Attributes:
        MIN_VOLUME (int): Minimum volume level (0)
        MAX_VOLUME (int): Maximum volume level (2)
        MIN_CHANNEL (int): Minimum channel number (0)
        MAX_CHANNEL (int): Maximum channel number (3)
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        """Initialize a Television object with default settings.
        
        The TV starts powered off, unmuted, at minimum volume and minimum channel.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
    
    def power(self) -> None:
        """Toggle the power status of the television."""
        self.__status = not self.__status
    
    def mute(self) -> None:
        """Toggle the mute status if the television is powered on."""
        if self.__status:
            self.__muted = not self.__muted
    
    def channel_up(self) -> None:
        """Increase the channel by 1, wrapping to MIN_CHANNEL if at MAX_CHANNEL.
        
        Only functions when the television is powered on.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    
    def channel_down(self) -> None:
        """Decrease the channel by 1, wrapping to MAX_CHANNEL if at MIN_CHANNEL.
        
        Only functions when the television is powered on.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    def volume_up(self) -> None:
        """Increase the volume by 1 if not at MAX_VOLUME and unmute.
        
        Only functions when the television is powered on.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """Decrease the volume by 1 if not at MIN_VOLUME and unmute.
        
        Only functions when the television is powered on.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        """Return a string representation of the television's current state.
        
        Returns:
            str: A string showing power status, channel, and volume (0 if muted)
        """
        volume_display: int = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"