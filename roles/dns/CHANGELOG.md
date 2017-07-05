# Release 2.0.0

* `resolver_dhclient_enabled` has been removed. If DHCP client is running on
  the host, the role should not be used. Use
  [ansible-role-dhclient](https://github.com/reallyenglish/ansible-role-dhclient/)
  instaed.
* `predictable_shuffle` is now optional. You should `predictable_shuffle` yourself.
* Support Ubuntu
* Support CentOS

# Release 1.0.0

* initial release
