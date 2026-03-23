# Service

postgis
```bash
docker exec edge-compose-postgres-1 pg_dump -U edge -t "patrol_*" -Fc wildfire-edge > patrol.dump

type patrol.dump | docker exec -i edge-compose-postgres-1 pg_restore -U edge -d wildfire-edge -v --clean --if-exists
```