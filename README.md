# What is this? 

This simple script can be used to extract an NThash of the `krb5key` base64 string that can be extracted out of a Univention UCS LDAP instance, if you have enhanced permissions.

For more info, a blogpost about this topic will be linked here:

# How to use? 

The usage using a docker container is recommended. The script has a dependency to univetions version of `heimdal`. At time of the repo creation, the dep package or source code can be found [here](https://download.univention.de/pool/main/u/univention-python-heimdal/).
The .deb file depends on python3 below 3.8.

If you downloaded the .deb package you can use the following calls for debian-based or fedora:

```bash
# debian-based
docker run --rm -it $(docker buildx build -q .) -d 'your krb5key'
# fedora
podman run --rm -it $(podman build -q .) -d 'your krb5key'
```
