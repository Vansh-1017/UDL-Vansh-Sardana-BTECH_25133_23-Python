**ANSWERS**

**Q1**
Byte Limit
1 byte=8 bits,it can represent max value of 255(2^8-1)
Since 2850 is larger than 255,so it cannot fit in a single byte and must be split into different bytes

**Q2**
For Value=2850

**value>>8**= it shifts binary bits 8 places to the right,leaving only the **upper** part,which equals **11**

**value & 0xFF**= ignore everything except the last 8 bits,leaving the **lower** part,which equals **34**

**Q3**
The operation (high<<8) shifts the high byte 8 position to left,returning to its **msb** position

The | low operation then merges the low byte into remaining 8 empty bits

This reverses the encode() process by **stitching** the two seprated bytes

**Q4**
A running average calculates the mean of the last 10 values

A total average accounts for every value received since the start

For live data,a running avg is essential because it allows the system to trigger immediate safety warning for real time fluctuations

**Q5**
Because a plain python list would risk a crash or data loss because it cannot safely handle read and write from different threads