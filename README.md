# Launchpad_rgb
The Launchpad MK2 by Novation has 80 24 bit RGB LEDs, but the normal MIDI message protocol only allows for 127 total colors.  
How do you access the full power of 63\*63\*63 colors? System exclusive messages of course!

MIDI System Exclusive messages are messages that are exclusive to a specific device type. The purpose is so that device manufacturers can implement features outside of the MIDI specification while staying in-band.

Awesome! Now what?  
System exclusive messages are more complicated than normal messages. They need a header that includes the device-id, which specifies what device the messages are for, and two sub-ids, which specify what feature to invoke.

This library is a convenient way to create system exclusive messages that can access the full 24 bit RGB color available on the Launchpad MK2.

A Message object stores all the notes that will change and what their new color will be. The instance methods of Message modify that data and return the Message, so you can chain calls. To get the actual sysex data (not including the 0xF0 to start and 0xF7 to end the message), call the object like a function. The returned data is ready to be put into any MIDI message library, such as mido.

Example:  
~~~
msg = Message().row(0, 1, 0.5, 0.25)
msg.note(1, 1, 1, 0.5, 0.25).note(8, 1, 1, 0.5, 0.25)
data = msg()
print(data) -> [0, 32, 41, 2, 24, 11, 11, 63, 31.5, 15.75, 12, 63, 31.5, 15.75,
               13, 63, 31.5, 15.75, 14, 63, 31.5, 15.75, 15, 63, 31.5, 15.75,
               16, 63, 31.5, 15.75, 17, 63, 31.5, 15.75, 18, 63, 31.5, 15.75,
               22, 63, 31.5, 15.75, 29, 63, 31.5, 15.75]
~~~
