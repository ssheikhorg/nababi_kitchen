db:
	docker run --name nababi-db \
		-e POSTGRES_USER=admin \
		-e POSTGRES_PASSWORD=N@babiKitchen \
		-e POSTGRES_DB=nababidb \
		-p 5432:5432 \
		-v db_data:/var/lib/postgresql/data \
		-d postgres
