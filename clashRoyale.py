import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('clash-royale-season-18-dec-0320-dataset', path='.', unzip=True)
#