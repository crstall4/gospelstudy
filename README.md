sudo docker build -t gospelstudy /home/clayton/git/gospelstudy
sudo docker run --rm -v /home/clayton/git/gospelstudy:/app -dp 80:5000 gospelstudy

OR:
sudo docker build -t ghcr.io/crstall4/gospelstudy /home/clayton/git/gospelstudy
sudo docker push ghcr.io/crstall4/gospelstudy

OR:
sudo docker pull ghcr.io/crstall4/gospelstudy
sudo docker run -dp 80:5000 --restart always ghcr.io/crstall4/gospelstudy