from brownie import AdvancedCollectable, network
from scripts.helpful_script import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json


ACTIVE_NETWORK = network.show_active()


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"

        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri


def main():
    advanced_collectable = AdvancedCollectable[-1]
    number_of_advanced_collectable = advanced_collectable.tokenCounter()
    print(f"You have created {number_of_advanced_collectable} collectables")
    for token_id in range(number_of_advanced_collectable):
        breed = get_breed(advanced_collectable.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{ACTIVE_NETWORK}/{token_id}-{breed}.json"

        collectable_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it or overwrite")
        else:
            print(f"Creating! metadata file: {metadata_file_name}")
            collectable_metadata["name"] = breed
            collectable_metadata["descriptoin"] = f"An adorable {breed} pup!"
            image_file_name = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_url = upload_to_ipfs(image_file_name)
            collectable_metadata["image_url"] = image_url

            with open(metadata_file_name, "w") as file:
                json.dump(metadata_file_name, file)
            metadata_url = upload_to_ipfs(metadata_file_name)
