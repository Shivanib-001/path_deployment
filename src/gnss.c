#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> 

int main() {
    FILE *file;

    srand((unsigned int)time(NULL));

    while (1) {
        file = fopen("../data/gnss.buf", "a"); 
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
        }

        double lat = 28+(double)rand() / RAND_MAX;
        double lon = 77+ (double)rand() / RAND_MAX;

        // Write data to file
        fprintf(file, "Lat : %.4f,Lon:%.4f\n", lat, lon);
        fclose(file);

        //printf("Wrote: Lat : %.4f,Lon:%.4f\n", lat, lon);

        usleep(500000);
    }

    return 0;
}

