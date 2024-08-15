import os
from torch.utils.data import Dataset
from PIL import Image

def construct_patch_path(data_path, survey_id):
    """Construct the patch file path based on plot_id as './CD/AB/XXXXABCD.jpeg'"""
    path = data_path
    for d in (str(survey_id)[-2:], str(survey_id)[-4:-2]):
        path = os.path.join(path, d)

    path = os.path.join(path, f"{survey_id}.jpeg")

    return path

class BaselineTrainDataset(Dataset):
    def __init__(self, bioclim_data_dir, landsat_data_dir, sentinel_data_dir, metadata, survey_ids, transform=None):
        self.transform = transform
        self.sentinel_transform = transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.5, 0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5, 0.5)),
        ])
      
        self.bioclim_data_dir = bioclim_data_dir
        self.landsat_data_dir = landsat_data_dir
        self.sentinel_data_dir = sentinel_data_dir
        self.metadata = metadata
        self.metadata = self.metadata.dropna(subset="speciesId").reset_index(drop=True)
        self.metadata['speciesId'] = self.metadata['speciesId'].astype(int)
        self.label_dict = self.metadata.groupby('surveyId')['speciesId'].apply(list).to_dict()
        
        self.metadata = self.metadata.drop_duplicates(subset="surveyId").reset_index(drop=True)

        self.survey_ids = survey_ids

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        
        survey_id = self.survey_ids[idx]
        
        landsat_sample = torch.nan_to_num(torch.load(os.path.join(self.landsat_data_dir, f"GLC24-PA-train-landsat_time_series_{survey_id}_cube.pt")))
        bioclim_sample = torch.nan_to_num(torch.load(os.path.join(self.bioclim_data_dir, f"GLC24-PA-train-bioclimatic_monthly_{survey_id}_cube.pt")))

        rgb_sample = np.array(Image.open(construct_patch_path(self.sentinel_data_dir, survey_id)))
        nir_sample = np.array(Image.open(construct_patch_path(self.sentinel_data_dir.replace("rgb", "nir").replace("RGB", "NIR"), survey_id)))
        sentinel_sample = np.concatenate((rgb_sample, nir_sample[...,None]), axis=2)

        species_ids = self.label_dict.get(survey_id, [])  # Get list of species IDs for the survey ID
        label = torch.zeros(num_classes)  # Initialize label tensor
        for species_id in species_ids:
            label_id = species_id
            label[label_id] = 1  # Set the corresponding class index to 1 for each species
        
        if isinstance(landsat_sample, torch.Tensor):
            landsat_sample = landsat_sample.permute(1, 2, 0)  # Change tensor shape from (C, H, W) to (H, W, C)
            landsat_sample = landsat_sample.numpy()  # Convert tensor to numpy array
            
        if isinstance(bioclim_sample, torch.Tensor):
            bioclim_sample = bioclim_sample.permute(1, 2, 0)  # Change tensor shape from (C, H, W) to (H, W, C)
            bioclim_sample = bioclim_sample.numpy()  # Convert tensor to numpy array   
        
        if self.transform:
            landsat_sample = self.transform(landsat_sample)
            bioclim_sample = self.transform(bioclim_sample)
            sentinel_sample = self.sentinel_transform(sentinel_sample)

        return landsat_sample, bioclim_sample, sentinel_sample, label, survey_id

