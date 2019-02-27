# hashing-automation
Creating clusters and matrices's utilizing pandas hashing algorithms

# SSDEEP quickstart
Installing SSDEEP for linux:
(Ubuntu, Fedora, Debian, CentOS, ArchLinux, FreeBSD)
apt get ssdeep (or how they list it on their website)

Installing SSDEEP of WINDOWS:
Download compiled binaries from github page (https://github.com/ssdeep-project/ssdeep/releases)
Add SSDEEP anywhere on any hard drive
ADD that folder to PATH, then you will be able to to use ssdeep from either cmd, gitbash, or buntu WSL shell


Comparing against itself in current directory in CSV format:
ssdeep -bpac * 
ssdeep -bpac * > [filename.(txt)can be anything]

Saving all hashes to a file to be used later for comparison
ssdeep * > [filename.(txt)can be anything]

Clustering say a sample size of 18 by itself (18x18)
ssdeep -g -m 18filehashes.txt 18filehashes.txt

If you want to set a threshold with clustering
ssdeep -gt [##] -m 18filehashes.txt 18filehashes.txt 
