docker-download:
	@which docker || ( \
		echo "Docker not found. Installing Docker..." && \
		sudo apt update \
		&& sudo apt install apt-transport-https ca-certificates curl software-properties-common -y \
		&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
		&& sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
		&& sudo apt update \
		&& sudo apt install docker-ce -y \
		&& sudo systemctl enable docker \
		&& sudo systemctl start docker \
	)

