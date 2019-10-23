# -*- mode: ruby -*-
# vi: set ft=ruby :

# Python test VM's address
PYA = "192.168.56.223"

Vagrant.configure("2") do |config|
	config.vm.box_check_update = false
	config.vm.box = "sbeliakou/centos"
	
	config.vm.define "kea-python" do |cl|
        	cl.vm.host_name="kea-python"
        	cl.vm.network "private_network", ip: PYA
        	cl.vm.provider "virtualbox" do |vm|
         	       	vm.gui = false
                	vm.memory = "2048"
                	vm.name = "kea-python"
                	end
        	cl.vm.provision "shell", path: "./pyenv-install.sh"
		cl.vm.provision "shell", path: "./pyinterpreters-install.sh"
	end
end
