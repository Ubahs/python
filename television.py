class Television
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  Max_CHANNEL = 3

def  _init_(self):
     self.__status = False
     self.__muted = False
     self.__volume = Television.Min_VOLUME
     self.__channel = Television.Min_CHANNEL

def power(self):
    if self.__status:
        self.__status = False
    else:
         self.__status = True

def mute(self):
if self.status:
    if self.__muted:
        self.__muted = False
    else:
        slef.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel._channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


     def volume_down(self):
         if self._status:
             self.muted = False
             if self.__volume > Television.Min_VOLUME:
                 self.volume -= 1

     def __str_(self):
         if self.__muted:
             volume = Television.Min_VOLUME
         else:
             volume = self.__volume

             return f"Power = {self._status}, Channel = {Self._channel},Volume = {volume}"
       
