build:
	docker build -t therumbler/playlister .
run:
	docker stop playlister && docker rm playlister
	docker run -p 8000:8000 --name playlister therumbler/playlister