# sepolicy-httpd-rtmp

SELinux policy for allowing the `httpd_t` domain to connect to RTMP ports,
controlled via an SELinux boolean.

## Usage

To use the SELinux policy, run `./httpd-flash-server.sh` as root. It will
compile and load the policy and create an rpm that can be loaded on other
systems.

To allow a process in the `httpd_t` domain to connect to port 1935, enable the
`httpd_enable_flash_server` boolean.

Note that the RTMP port (1935) is referred to as flash in SELinux, since that's
where RTMP originated.
