# Beta Randomized Obfuscation
BRO is a zero-delay website fingerprinting defense. Traces are padded by sampling dummy packet timestamps from a randomized beta distribution scaled by a randomized padding window.
## Trace Collection
Clone the [tor-capture](https://github.com/csmcguan/tor-capture) repository. Follow the instructions for setup and trace capture provided in the README. After collecting traces, move the ./tor-capture/log directory to ./bro
## Configurations
The configurations and their parameters are listed in ./util/config.ini. They can be split into 3 categories.
### Finalized Defense
The finalized defense configurations are b1 and b2. They both share the same parameters with the exception that b2 is allocated a larger padding budget.
### Beta Distribution Parameter Testing
There are 3 configurations, tb[1-3], which test the effect of randomizing the beta distribution. The shape of the beta distribution in tb1 is fully randomized and can skew to the extreme left and right. The shape of tb2 and tb3 are static; tb2 is skewed to the left and tb3 has the shape of a normal distribution.
### Padding Budget Testing
There are 12 configurations, tp[1-12], which increment the padding budget at intervals of 250 from 250 to 3000.
## Script Definitions
### sim.sh
This script simulates the BRO defense on previously collected traces.
### bwoh.sh
This script calculates the mean and median bandwidth overhead induced by the defense on the dataset. Bandwidth overhead of individual traces is calculated by taking the difference in length between a defended traces and the original, and dividing that by the length of the original trace.
### loh.sh
This script calculates the mean and median latency overhead induced by the defense on the dataset. The latency overhead of individual traces is calculated by taking the difference between the final timestamp of a defended trace and the original trace, and dividing by the original.
## Script Usage
All scripts (sim.sh, bwoh.sh, and loh.sh) are written in a way that enable simulating all configurations, the finalized defense configurations, testing configurations for tuning the defense grouped by type, and any comination of individual and/or any of the previously mentioned batched inputs. An example is given with the sim.sh script.
### All Configurations
When running all configurations, the bwoh.sh and loh.sh scripts log the results to bwoh.txt and loh.txt respectively.
```
bash sim.sh
```
### Finalized Defense
```
bash sim.sh b
```
### Beta Distribution Parameters
```
bash sim.sh tb
```
### Padding Budget
```
bash sim.sh tp
```
### Any Combination
```
bash sim.sh <config1> <config2> ...
```
