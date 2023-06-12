from minio import Minio


def uploader(bucket, object_name, object_path):
    # with minio test client
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    # with personal info
    # client = Minio(
    #     "play.min.io",
    #     access_key="Q3AM3UQ867SPQQA43P2F",
    #     secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    # )

    # Make 'bucket' bucket if not exist.
    found = client.bucket_exists(bucket)
    if not found:
        client.make_bucket(bucket)
    else:
        print(f"Bucket '{bucket}' already exists!")

    # Upload object as given name to created or existed bucket.
    client.fput_object(
        bucket,
        object_name,
        object_path,
    )

    print(f"'{object_path}' is successfully uploaded as object '{object_name}' to bucket '{bucket}'.")
