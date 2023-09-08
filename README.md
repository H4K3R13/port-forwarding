# port-forwarding
Files Used for a port forwarding experiment

To add iptable rule

```bash
sudo iptables -t nat -A OUTPUT -p tcp --dport 8909 -j DNAT --to-destination 15.0.0.1:8765
```

To run the docker file
```bash
sh build_run.sh
```
