# openfaas_animal_db
Repository for the OpenFaas function that generates some useful statistics to analyze a database containing all ENA available nucleotide reads for a given organism, accessing it from a S3 object storage URL.
The function automatically scales based on the number of invocations per second.
