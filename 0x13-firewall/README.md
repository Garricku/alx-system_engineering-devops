<h1>Firewall</h1>
<h2>DevOps, SysAdmin, Security</h2>

This project is centered around firewalls. How to use them, how to configure them using UFW on an Ubuntu machine.

<h2>Warning!</h2>
Containers on demand cannot be used for this project (Docker container limitation)

Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.
