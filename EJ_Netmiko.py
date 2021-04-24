from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.0.10",
    port=22,
    username="cisco",
    password="cisco123!")

config_commands = [
 'int loopback 2',
 'ip address 1.1.1.1 255.255.255.0',
 'description WHATEVER'
 ]

output = sshCli.send_config_set(config_commands)
output = sshCli.send_command("show ip int brief")
print(output)
