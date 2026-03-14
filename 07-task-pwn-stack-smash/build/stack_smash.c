#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Hidden "win" function — reads and prints the flag.
 * Players must redirect execution here via buffer overflow.
 */
void unlock_vault(void)
{
	FILE *f = fopen("/home/ctf/flag", "r");
	if (f == NULL) {
		puts("[VAULT] ERROR: Flag file not found!");
		exit(1);
	}
	char flag[128];
	if (fgets(flag, sizeof(flag), f) != NULL)
		printf("[VAULT] ACCESS GRANTED: %s\n", flag);
	fclose(f);
	exit(0);
}

int main(void)
{
	char passphrase[64];

	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);

	puts("========================================");
	puts("   ROBO-VAULT SECURITY SYSTEM v1.33.7   ");
	puts("========================================");
	puts("");
	puts("[SYSTEM] Warning: This vault is protected");
	puts("         by state-of-the-art security.");
	puts("");
	printf("[SYSTEM] Enter passphrase: ");

	gets(passphrase);

	printf("[SYSTEM] Checking passphrase: \"%s\"\n", passphrase);
	puts("[SYSTEM] ACCESS DENIED. Invalid passphrase.");

	return 0;
}
