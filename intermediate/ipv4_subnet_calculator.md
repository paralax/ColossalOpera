# Title 

IPv4 Subnet Calculator

# Difficulty

Intermediate

# Description

In IPv4 networking, classless inter-domain routing (CIDR) notation is used to specific network addresses that fall outside of the historic "class A", "class B" and "class C" desigation. Instead it's denoted in an IPv4 network address with a bit-lenegth mask. For example, the historic class A network of 10.0.0.0 is expressed as `10.0.0.0/8`, meaning only the first 8 bits of the network address are specified. CIDR notation allows you to specify networks outside of the classic octet boundaries.

For this challenge, you'll be given various IPv4 addresses and subnets and asked to remove ones already covered by a covering CIDR representation. 

# Input Description

You'll be given a single integer and then list of IPv4 host and addresses addresses, containing that many lines of input. Examples:

3
172.26.32.162/32
172.26.32.0/24
172.26.0.0/16

# Output Description

Your program should emit the minimal covering set of the network addresses to remove ones already specified by the network addresses. From the above example only `172.26.0.0/16` would remain.

# Challenge Input

	12
	192.168.0.0/16
	172.24.96.17/32
	172.50.137.225/32
	202.139.219.192/32
	172.24.68.0/24
	192.183.125.71/32
	201.45.111.138/32
	192.168.59.211/32
	192.168.26.13/32
	172.24.0.0/17
	172.24.5.1/32
	172.24.68.37/32

# Challenge Output

	192.168.0.0/16
	172.24.0.0/17	
	172.50.137.225/32
	202.139.219.192/32
	192.183.125.71/32
	201.45.111.138/32
