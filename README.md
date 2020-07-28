# openfaas_animal_db
Repository for the OpenFaas function that generates some useful statistics to analyze a database containing all ENA available nucleotide reads for a given organism, accessing it from a S3 object storage URL.  
The function is implemented on docker swarm; it could also be implemented on kubernetes.
The function automatically scales based on the number of invocations per second; on kubernetes it could also be programmed to autoscale based on CPU or memory usage.
To test autoscaling, the function is scaled down to zero replicas with the following command:
docker service scale animal-db=0
Invoking the function will trigger the scaling up to the necessary number of replicas.

The function container is available at https://hub.docker.com/repository/docker/matteobolner/animal-db  
The source databases are obtained from ENA (https://www.ebi.ac.uk/ena) and available on an S3 bucket  

Links:  https://animal-db-bucket.s3.amazonaws.com/9668_database.csv   
        https://animal-db-bucket.s3.amazonaws.com/9823_database.csv
