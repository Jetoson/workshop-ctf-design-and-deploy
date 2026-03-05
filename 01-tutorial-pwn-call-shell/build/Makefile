CFLAGS = -fno-PIC -Wall -fno-stack-protector -Wno-unused-function
LDFLAGS = -no-pie

.PHONY: all clean

all: piece_of_pie
	cp /lib/x86_64-linux-gnu/libc.so.6 .
	cp /lib64/ld-linux-x86-64.so.2 .

piece_of_pie: piece_of_pie.o
	$(CC) $(LDFLAGS) -o $@ $^

piece_of_pie.o: piece_of_pie.c
	$(CC) $(CFLAGS) -c $<

clean:
	-rm -f *~ *.o
	-rm -f piece_of_pie
	-rm -f libc.so.6
	-rm -f ld-linux-x86-64.so.2
