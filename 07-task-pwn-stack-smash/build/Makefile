CFLAGS = -fno-PIC -Wall -fno-stack-protector -Wno-unused-function -Wno-deprecated-declarations
LDFLAGS = -no-pie

.PHONY: all clean

all: stack_smash
	cp /lib/x86_64-linux-gnu/libc.so.6 .
	cp /lib64/ld-linux-x86-64.so.2 .

stack_smash: stack_smash.o
	$(CC) $(LDFLAGS) -o $@ $^

stack_smash.o: stack_smash.c
	$(CC) $(CFLAGS) -c $<

clean:
	-rm -f *~ *.o
	-rm -f stack_smash
	-rm -f libc.so.6
	-rm -f ld-linux-x86-64.so.2
