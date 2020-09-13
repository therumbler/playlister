build:
	docker build -t therumbler/playlister .
	
run:
	docker stop playlister && docker rm playlister
	docker run -p ${PORT}:${PORT} --name playlister --env-file=.env  therumbler/playlister