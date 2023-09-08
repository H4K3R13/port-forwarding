echo "Building Dokcer Image fakeport"
sudo docker rm -f fakeportContainer
sudo docker build -t fakeport .
sudo docker run  -v  "$(pwd):/code"  --network host --name fakeportContainer fakeport
sudo docker logs -f fakeportContainer
