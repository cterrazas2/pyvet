# Usage

To retrieve veteran data from the API, ensure your VA API key is set.
You should store your API key in an environment variable named `VA_API_KEY`
or in `creds.py` if you are developing locally.

You can also a download a Jupyter Notebook that uses pyvet [here]("https://github.com/cterrazas2/pyvet-jupyter/blob/main/explore_pyvet.ipynb").

## Veteran Benefits Intake

You can upload multiple files to the Veteran Benefits Administration (VBA) with
`pyvet`.

```python
from pyvet.benefits.intake.api import create_path_to_upload_files, upload_files

params = create_path_to_upload_files()
metadata = {
    "veteranFirstName": "Jane",
    "veteranLastName": "Doe",
    "fileNumber": "012345678",
    "zipCode": "97202",
    "source": "MyVSO",
    "docType": "21-22",
    "businessLine": "CMP",
}
uploaded_files = upload_files(
    params=params,
    uploads_dir="uploads",
    metadata=metadata,
)
```
